from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="a1dd728f-876c-54bf-8227-325288454b0b",
    key="SV09",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.IonosTadbulb.Name",
    display_name="Iono's Tadbulb",
    searchable_by=["Iono's Tadbulb", "Basic", "IonosTadbulb"],
    subtypes=["Basic"],
    collector_number=52,
    set_code="SV09",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=938,
    abilities=[
        Attack(
            title="Tiny Charge",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)
