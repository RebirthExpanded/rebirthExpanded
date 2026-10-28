"""Mr. Mime (SV035 122 -- JP SV2a 122; English MEW/122, MEW/179). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.session.passives import Passive, carrier_pokemon



class MimicBarrierPassive(Passive):
    """Same Energy count as the opponent's Active: no damage from their attacks."""

    def prevents_damage(self, calc, carrier):
        me = carrier_pokemon(carrier)
        if not (calc.is_attack and calc.is_opposing and calc.target is me):
            return False
        other = calc.board.active_pokemon(calc.attacker.owning_player_id) if calc.attacker is not None else None
        from spirit.game.models.board import EnergyEntity
        mine = sum(1 for c in me.children if isinstance(c, EnergyEntity))
        theirs = sum(1 for c in other.children if isinstance(c, EnergyEntity)) if other is not None else -1
        return mine == theirs


async def psypower(ctx):
    for _ in range(3):
        pool = ctx.opponent_pokemon_in_play()
        if not pool:
            return
        target = await ctx.choose_pokemon(pool, "Choose 1 of your opponent's Pokémon to put a damage counter on")
        if target is None:
            return
        await ctx.deal_damage(10, target=target, apply_modifiers=False, as_counters=True)


card = PokemonCardDef(
    guid="8ef59398-1f20-5685-812f-3824798c2a75",
    key="SV035",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MrMime.Name",
    display_name="Mr. Mime",
    searchable_by=["Mr. Mime", "Basic"],
    subtypes=["Basic"],
    collector_number=122,
    set_code="SV035",
    regulation_mark="G",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=439,
    abilities=[
        Ability(
            title="Mimic Barrier",
            game_text="If this Pokémon and your opponent's Active Pokémon have the same amount of Energy attached, prevent all damage done to this Pokémon by attacks from your opponent's Pokémon.",
            passive=MimicBarrierPassive(),
        ),
        Attack(
            title="Psypower",
            game_text="Put 3 damage counters on your opponent's Pokémon in any way you like.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=psypower,
        ),
    ],
)
