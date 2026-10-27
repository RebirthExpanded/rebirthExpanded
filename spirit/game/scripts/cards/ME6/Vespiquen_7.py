"""Vespiquen (ME6 7 -- JP M6 007; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac

from spirit.game.session.effects import is_evolution_pokemon


def _evolved_defender(ctx) -> bool:
    return ctx.defender is not None and is_evolution_pokemon(ctx.defender)


card = PokemonCardDef(
    guid="6889b099-ecc8-58f4-ba5a-2663d1b7869a",
    key="ME6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Vespiquen.Name",
    display_name="Vespiquen",
    searchable_by=["Vespiquen", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=7,
    set_code="ME6",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=120,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Combee.Name",
    family_id=415,
    abilities=[
        Attack(
            title="Pierce",
            game_text="",
            cost={PokemonTypes.GRASS: 1},
            damage=40,
        ),
        Attack(
            title="Clean Hit",
            game_text="If your opponent's Active Pokémon is an Evolution Pokémon, this attack does 80 more damage.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=80,
            damage_operator="+",
            effect=ac.bonus_if(_evolved_defender, 80),
        ),
    ],
)
