"""Aipom (SV4 145 -- JP SV4M 051; English PAR/145, PAR/211). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su


card = PokemonCardDef(
    guid="a54fdaf4-ad82-59ad-bbaf-0ad79135822c",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Aipom.Name",
    display_name="Aipom",
    searchable_by=["Aipom", "Basic"],
    subtypes=["Basic"],
    collector_number=145,
    set_code="SV4",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=190,
    abilities=[
        Attack(
            title="Filch",
            game_text="Draw a card.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=su.draw_attack(1),
        ),
        Attack(
            title="Smack",
            game_text="",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
