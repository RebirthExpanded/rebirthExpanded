from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import damage_counters_on, damage_per

card = PokemonCardDef(
    guid="83c6eec0-9492-5679-9de2-0ce80c5ede12",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tyrunt.Name",
    display_name="Tyrunt",
    searchable_by=["Tyrunt", "Stage 1", "Tyrunt"],
    subtypes=["Stage 1"],
    collector_number=44,
    set_code="ME3",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.trainer.AntiqueJawFossil.Name",
    family_id=696,
    abilities=[
        Attack(
            title="Get Angry",
            game_text="This attack does 20 damage for each damage counter on this Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="x",
            effect=damage_per(damage_counters_on("self"), 20),
        ),
    ],
)
