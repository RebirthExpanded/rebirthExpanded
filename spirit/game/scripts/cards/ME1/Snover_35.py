from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="31f9ae5d-961a-5e52-b49e-d05262c98461",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Snover.Name",
    display_name="Snover",
    searchable_by=["Snover", "Basic", "Snover"],
    subtypes=["Basic"],
    collector_number=35,
    set_code="ME1",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.METAL,
    family_id=459,
    abilities=[
        Attack(
            title="Beat",
            cost={PokemonTypes.WATER: 1},
            damage=10,
        ),
        Attack(
            title="Icy Snow",
            cost={PokemonTypes.WATER: 2},
            damage=30,
        ),
    ],
)
