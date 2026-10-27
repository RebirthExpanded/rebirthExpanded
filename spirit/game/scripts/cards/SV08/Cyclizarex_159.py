"""Cyclizar ex (SV08 159 -- JP SV7a 051; English SSP/159, SSP/228). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers
from spirit.game.card_effects.pokemon import TeraRulePassive

from spirit.game.card_effects import attacks_common as ac


async def zircon_road(ctx):
    await ctx.deal_damage()
    if await ctx.ask_yes_no("Draw 5 cards?"):
        await ctx.draw_cards(5)


card = PokemonCardDef(
    guid="4aee4b6b-2d6e-566d-bc73-57667aed55b7",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cyclizarex.Name",
    display_name="Cyclizar ex",
    searchable_by=["Cyclizar ex", "Basic", "ex", "Tera"],
    subtypes=["Basic", "ex", "Tera"],
    collector_number=159,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.RareHoloEX,
    hp=210,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=967,
    passive=TeraRulePassive(),
    abilities=[
        Attack(
            title="Break Through",
            game_text="This attack also does 30 damage to 1 of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.COLORLESS: 3},
            damage=130,
            effect=ac.snipe_attack(30, pool="bench", also_base=True),
        ),
        Attack(
            title="Zircon Road",
            game_text="You may draw 5 cards.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.FIRE: 1, PokemonTypes.PSYCHIC: 1},
            damage=180,
            effect=zircon_road,
        ),
    ],
)
