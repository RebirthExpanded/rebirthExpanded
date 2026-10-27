"""Dialga ex (SVP 180 -- JP SVM 083; English SVP/180). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac

from spirit.game.attributes import PokemonTypes as _PT


async def time_bellow(ctx):
    await ctx.deal_damage()
    await ctx.draw_cards(1)


card = PokemonCardDef(
    guid="69fdb94f-bd20-5854-b05b-448760cd0551",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dialgaex.Name",
    display_name="Dialga ex",
    searchable_by=["Dialga ex", "Basic", "ex"],
    subtypes=["Basic", "ex"],
    collector_number=180,
    set_code="SVP",
    regulation_mark="H",
    rarity=Rarities.RarePromo,
    hp=220,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    family_id=483,
    abilities=[
        Attack(
            title="Time Bellow",
            game_text="Draw a card.",
            cost={PokemonTypes.METAL: 1},
            damage=20,
            effect=time_bellow,
        ),
        Attack(
            title="Metal Blast",
            game_text="This attack does 20 more damage for each [M] Energy attached to this Pokémon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=100,
            damage_operator="+",
            effect=ac.damage_per(ac.count_energy("self", _PT.METAL), 20, base=100),
        ),
    ],
)
