from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="2b6ff334-f8b8-5265-bcee-9065fc6c14b7",
    key="ME4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Skrelp.Name",
    display_name="Skrelp",
    searchable_by=["Skrelp", "Basic", "Skrelp"],
    subtypes=["Basic"],
    collector_number=58,
    set_code="ME4",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=690,
    abilities=[
        Attack(
            title="Hook",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)
