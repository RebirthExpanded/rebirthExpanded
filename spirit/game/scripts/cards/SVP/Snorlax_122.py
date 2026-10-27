"""Snorlax (SVP 122 -- JP SVI 046; English SVP/122). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="c719ea96-a287-502c-8a6f-96f51c91d5e1",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Snorlax.Name",
    display_name="Snorlax",
    searchable_by=["Snorlax", "Basic"],
    subtypes=["Basic"],
    collector_number=122,
    set_code="SVP",
    regulation_mark="H",
    rarity=Rarities.RarePromo,
    hp=160,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=446,
    abilities=[
        Attack(
            title="Lazy Press",
            game_text="",
            cost={PokemonTypes.COLORLESS: 4},
            damage=120,
        ),
    ],
)
