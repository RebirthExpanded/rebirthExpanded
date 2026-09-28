from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.data_utils import def_for
from spirit.game.card_effects.attacks_common import count_in_play, damage_per


def _beedrill(pokemon) -> bool:
    return getattr(def_for(pokemon.archetype_id), "display_name", None) in ("Beedrill", "Beedrill ex")

card = PokemonCardDef(
    guid="d3f6a29e-a098-532c-8ed2-742c5ac7b2da",
    key="ME4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Beedrillex.Name",
    display_name="Beedrill ex",
    searchable_by=["Beedrill ex", "Stage 2", "ex", "Beedrillex"],
    subtypes=["Stage 2", "ex"],
    collector_number=3,
    set_code="ME4",
    regulation_mark="J",
    rarity=Rarities.RareHoloEX,
    hp=310,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Kakuna.Name",
    family_id=13,
    abilities=[
        Attack(
            title="Rumbling Bees",
            game_text="This attack does 110 damage for each of your Beedrill and Beedrill ex in play.",
            cost={PokemonTypes.GRASS: 1},
            damage=110,
            damage_operator="x",
            effect=damage_per(count_in_play("mine", _beedrill), 110),
        ),
    ],
)
