from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack

card = PokemonCardDef(
    guid="1e5ac7fe-78f2-5c32-97f7-2fb849d0c727",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Wailordex.Name",
    display_name="Wailord ex",
    searchable_by=["Wailord ex", "Stage 1", "ex", "Wailordex"],
    subtypes=["Stage 1", "ex"],
    collector_number=16,
    set_code="ME5",
    regulation_mark="J",
    rarity=Rarities.RareHoloEX,
    hp=380,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Wailmer.Name",
    family_id=320,
    abilities=[
        Attack(
            title="Surf",
            cost={PokemonTypes.WATER: 3},
            damage=120,
        ),
        Attack(
            title="Falling Down",
            game_text="This Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.WATER: 5},
            damage=270,
            effect=condition_attack(self_conditions=(SpecialConditions.ASLEEP,)),
        ),
    ],
)
