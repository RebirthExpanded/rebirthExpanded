"""Mega Gallade ex (ME4 48 -- JP MP 068; English CRI/48). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


def _undamaged(ctx) -> bool:
    return not ac.has_damage("self")(ctx)


card = PokemonCardDef(
    guid="8c9087b9-955e-5033-8aa8-1bb1d54d81cf",
    key="ME4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MegaGalladeex.Name",
    display_name="Mega Gallade ex",
    searchable_by=["Mega Gallade ex", "Stage 2", "ex", "SV_Mega"],
    subtypes=["Stage 2", "ex", "SV_Mega"],
    collector_number=48,
    set_code="ME4",
    regulation_mark="J",
    rarity=Rarities.RareHoloEX,
    hp=350,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Kirlia.Name",
    family_id=280,
    abilities=[
        Attack(
            title="Gale Slash",
            game_text="If this Pokémon has no damage counters on it, this attack does 150 more damage.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=50,
            damage_operator="+",
            effect=ac.bonus_if(_undamaged, 150),
        ),
        Attack(
            title="Marvelous Edge",
            game_text="",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=240,
        ),
    ],
)
