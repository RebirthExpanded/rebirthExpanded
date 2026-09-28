from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.session.effects import full_stack, is_pokemon_tool, is_special_energy


async def corrosive_liquid(ctx):
    """Discard every Pokemon Tool and Special Energy on the opponent's Pokemon."""
    doomed = []
    for pokemon in ctx.opponent_pokemon_in_play():
        if ctx.effects_blocked(pokemon):
            continue
        doomed += [c for c in full_stack(pokemon)
                   if c is not pokemon and (is_pokemon_tool(c) or is_special_energy(c))]
    if doomed:
        await ctx.discard_cards(doomed)

card = PokemonCardDef(
    guid="7ce0a7b8-49d6-57c4-aafe-73bfe37f6979",
    key="ME4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MegaDragalgeex.Name",
    display_name="Mega Dragalge ex",
    searchable_by=["Mega Dragalge ex", "Stage 1", "ex", "SV_Mega", "MegaDragalgeex"],
    subtypes=["Stage 1", "ex", "SV_Mega"],
    collector_number=65,
    set_code="ME4",
    regulation_mark="J",
    rarity=Rarities.RareHoloEX,
    hp=330,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Skrelp.Name",
    family_id=690,
    abilities=[
        Attack(
            title="Corrosive Liquid",
            game_text="Discard all Pok\u00e9mon Tools and Special Energy from all of your opponent's Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=0,
            effect=corrosive_liquid,
        ),
        Attack(
            title="Pernicious Poison",
            game_text="Your opponent's Active Pok\u00e9mon is now Poisoned. During Pok\u00e9mon Checkup, place 16 damage counters on that Pok\u00e9mon instead of 1.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.DARKNESS: 1},
            damage=0,
            effect=condition_attack(SpecialConditions.POISONED, counters=16),
        ),
    ],
)
