from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="518586c2-b431-5462-a4a8-a97ef8901292",
    key="SV09",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Piloswine.Name",
    display_name="Piloswine",
    searchable_by=["Piloswine", "Stage 1", "Piloswine"],
    subtypes=["Stage 1"],
    collector_number=78,
    set_code="SV09",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Swinub.Name",
    family_id=220,
    abilities=[
        Attack(
            title="Strength",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
        Attack(
            title="Impaling Tusk",
            cost={PokemonTypes.FIGHTING: 2},
            damage=50,
        ),
    ],
)
