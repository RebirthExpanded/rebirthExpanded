"""Sudowoodo (ME4 43 -- JP M4 043; English CRI/43). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su
from spirit.game.data_utils import def_for, subtypes_for


def _tome(card) -> bool:
    return getattr(def_for(card.archetype_id), "display_name", None) == "Transformation Tome"


async def rock_hurl(ctx):
    await ctx.deal_damage(ignore_resistance=True)


card = PokemonCardDef(
    guid="0c63bbff-52d8-5df5-819d-b9cf94f4fe2f",
    key="ME4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sudowoodo.Name",
    display_name="Sudowoodo",
    searchable_by=["Sudowoodo", "Basic"],
    subtypes=["Basic"],
    collector_number=43,
    set_code="ME4",
    regulation_mark="J",
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=438,
    abilities=[
        Attack(
            title="Trials and Trip-ulations",
            game_text="Search your deck for up to 2 Transformation Tome cards, reveal them, and put them into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=su.search_to_hand(_tome, count=2, reveal=True, prompt="Choose up to 2 Transformation Tome cards."),
        ),
        Attack(
            title="Rock Hurl",
            game_text="This attack's damage isn't affected by Resistance.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=30,
            effect=rock_hurl,
        ),
    ],
)
