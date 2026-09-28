from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="b3e1adfc-4d28-50c4-8051-316241f81698",
    key="ME4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bergmite.Name",
    display_name="Bergmite",
    searchable_by=["Bergmite", "Basic", "Bergmite"],
    subtypes=["Basic"],
    collector_number=23,
    set_code="ME4",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    family_id=712,
    abilities=[
        Attack(
            title="Chilly",
            cost={PokemonTypes.WATER: 1},
            damage=10,
        ),
        Attack(
            title="Frost Breath",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
    ],
)
