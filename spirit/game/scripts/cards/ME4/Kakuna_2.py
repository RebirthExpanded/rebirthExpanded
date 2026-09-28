from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.passives_common import takes_less_passive

card = PokemonCardDef(
    guid="3979acd2-0219-555b-84fe-b5fa49694b6b",
    key="ME4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kakuna.Name",
    display_name="Kakuna",
    searchable_by=["Kakuna", "Stage 1", "Kakuna"],
    subtypes=["Stage 1"],
    collector_number=2,
    set_code="ME4",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Weedle.Name",
    family_id=13,
    abilities=[
        Ability(
            title="Exoskeleton",
            game_text="This Pok\u00e9mon takes 20 less damage from attacks (after applying Weakness and Resistance).",
            passive=takes_less_passive(20),
        ),
        Attack(
            title="Hang Down",
            cost={PokemonTypes.GRASS: 1},
            damage=20,
        ),
    ],
)
