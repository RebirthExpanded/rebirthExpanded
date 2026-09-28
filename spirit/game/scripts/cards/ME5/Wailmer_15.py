from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="c3c37f43-61d4-5331-a5e2-b392f4ad4f04",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Wailmer.Name",
    display_name="Wailmer",
    searchable_by=["Wailmer", "Basic", "Wailmer"],
    subtypes=["Basic"],
    collector_number=15,
    set_code="ME5",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=130,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=320,
    abilities=[
        Attack(
            title="Water Gun",
            cost={PokemonTypes.WATER: 2},
            damage=40,
        ),
        Attack(
            title="Wave Splash",
            cost={PokemonTypes.WATER: 3},
            damage=80,
        ),
    ],
)
