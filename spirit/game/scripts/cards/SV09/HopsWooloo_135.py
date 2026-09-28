from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="605d51fa-f920-5031-b915-956af4df5e02",
    key="SV09",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HopsWooloo.Name",
    display_name="Hop's Wooloo",
    searchable_by=["Hop's Wooloo", "Basic", "HopsWooloo"],
    subtypes=["Basic"],
    collector_number=135,
    set_code="SV09",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=831,
    abilities=[
        Attack(
            title="Smash Kick",
            cost={PokemonTypes.COLORLESS: 3},
            damage=50,
        ),
    ],
)
