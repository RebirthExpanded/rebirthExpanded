from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="87f3e4e9-8cf0-54cd-9e96-2c45fc36a8cc",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.CynthiasRoselia.Name",
    display_name="Cynthia's Roselia",
    searchable_by=["Cynthia's Roselia", "Basic", "CynthiasRoselia"],
    subtypes=["Basic"],
    collector_number=7,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=315,
    abilities=[
        Attack(
            title="Spike Sting",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)
