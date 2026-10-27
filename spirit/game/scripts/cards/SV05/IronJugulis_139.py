"""Iron Jugulis (SV05 139 -- JP SVHM 017; English TEF/139). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import passives_common as pc


def _revenge(n):
    async def effect(ctx):
        attacker = ctx.damaged_by
        if attacker is not None:
            await ctx.deal_damage(10 * n, target=attacker, apply_modifiers=False, as_counters=True, is_attack=False)
    return effect


card = PokemonCardDef(
    guid="2acd008d-3f9a-5ca3-975f-9c6d5b3bad74",
    key="SV05",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.IronJugulis.Name",
    display_name="Iron Jugulis",
    searchable_by=["Iron Jugulis", "Basic", "Future"],
    subtypes=["Basic", "Future"],
    collector_number=139,
    set_code="SV05",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=993,
    abilities=[
        Ability(
            title="Automated Combat",
            game_text="If this Pokémon is in the Active Spot and is damaged by an attack from your opponent's Pokémon (even if this Pokémon is Knocked Out), put 3 damage counters on the Attacking Pokémon.",
            trigger=Triggers.ON_DAMAGED_BY_ATTACK,
            trigger_applies=pc.hit_in_active_by_opponent,
            effect=_revenge(3),
        ),
        Attack(
            title="Blasting Wind",
            game_text="",
            cost={PokemonTypes.COLORLESS: 3},
            damage=110,
        ),
    ],
)
