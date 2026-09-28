from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="c06e65a6-d59a-5045-9a57-19316e546c40",
    key="MEM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dolliv.Name",
    display_name="Dolliv",
    searchable_by=["Dolliv", "Stage 1", "Dolliv"],
    subtypes=["Stage 1"],
    collector_number=7,
    set_code="MEM",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Smoliv.Name",
    family_id=928,
    abilities=[
        Attack(
            title="Leaf Step",
            cost={PokemonTypes.GRASS: 1},
            damage=40,
        ),
    ],
)
