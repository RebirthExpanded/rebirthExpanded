"""Octillery (SV4 34 -- JP SV3a 004; English PAR/34). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


async def suction_cup_draw(ctx):
    if not getattr(ctx, "evolved_from_hand", True):
        return
    if ctx.deck_top(1) and await ctx.ask_yes_no("Use Suction Cup Draw?"):
        await ctx.draw_cards(3)


card = PokemonCardDef(
    guid="5e63a830-49c4-533c-8924-869d0cef1256",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Octillery.Name",
    display_name="Octillery",
    searchable_by=["Octillery", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=34,
    set_code="SV4",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=110,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Remoraid.Name",
    family_id=223,
    abilities=[
        Ability(
            title="Suction Cup Draw",
            game_text="When you play this Pokémon from your hand to evolve 1 of your Pokémon during your turn, you may draw 3 cards.",
            trigger=Triggers.ON_EVOLVE,
            effect=suction_cup_draw,
        ),
        Attack(
            title="Smokescreen Shot",
            game_text="During your opponent's next turn, if the Defending Pokémon tries to use an attack, your opponent flips a coin. If tails, that attack doesn't happen.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
            effect=ac.smokescreen_attack(),
        ),
    ],
)
