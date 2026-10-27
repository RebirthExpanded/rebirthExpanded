"""Cinccino (SV09 126 -- JP SVM 108; English JTG/126). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="3f0fb2d7-fb74-5e3d-8db3-7eb7693a2b69",
    key="SV09",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cinccino.Name",
    display_name="Cinccino",
    searchable_by=["Cinccino", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=126,
    set_code="SV09",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Minccino.Name",
    family_id=572,
    abilities=[
        Attack(
            title="Tail Smack",
            game_text="",
            cost={PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
    ],
)
