"""Yveltal (SV065 35 -- JP SV6a 035; English SFA/35). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES

from spirit.game.session.passives import effective_max_hp


def _counters(board, pokemon) -> int:
    return max(0, effective_max_hp(board, pokemon) - pokemon.get_attribute(AttrID.HP, 0)) // 10


async def _flip_discard_energy(ctx):
    await ctx.deal_damage()
    results = await ctx.flip_coins(1, ctx.ability.title if ctx.ability else "")
    target = ctx.opponent_active()
    if results and results[0] and target is not None and not ctx.effects_blocked(target) \
            and ctx.attached_energies(target):
        await ctx.discard_energy_from(target, 1, minimum=1,
                                      prompt="Choose an Energy to discard from your opponent's Active Pokémon")


async def corrosive_winds(ctx):
    for p in list(ctx.opponent_pokemon_in_play()):
        if _counters(ctx.board, p) > 0:
            await ctx.deal_damage(20, target=p, apply_modifiers=False, as_counters=True)


card = PokemonCardDef(
    guid="2b46810d-77d2-50c5-83b1-cc618a98dc45",
    key="SV065",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Yveltal.Name",
    display_name="Yveltal",
    searchable_by=["Yveltal", "Basic"],
    subtypes=["Basic"],
    collector_number=35,
    set_code="SV065",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=717,
    abilities=[
        Attack(
            title="Corrosive Winds",
            game_text="Put 2 damage counters on each of your opponent's Pokémon that has any damage counters on it.",
            cost={PokemonTypes.DARKNESS: 1},
            effect=corrosive_winds,
        ),
        Attack(
            title="Destructive Beam",
            game_text="Flip a coin. If heads, discard an Energy from your opponent's Active Pokémon.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
            effect=_flip_discard_energy,
        ),
    ],
)
