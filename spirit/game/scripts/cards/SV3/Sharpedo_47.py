"""Sharpedo (SV3 47 -- JP SV3 022; English OBF/47). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac

from spirit.game.session.passives import effective_retreat_cost


def _defender_retreat(ctx) -> int:
    d = ctx.opponent_active()
    return effective_retreat_cost(ctx.board, d) if d is not None else 0


card = PokemonCardDef(
    guid="45558ee9-4f8b-57bf-922f-a63e15fc6c53",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sharpedo.Name",
    display_name="Sharpedo",
    searchable_by=["Sharpedo", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=47,
    set_code="SV3",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Carvanha.Name",
    family_id=318,
    abilities=[
        Attack(
            title="Aqua Impact",
            game_text="This attack does 30 more damage for each Colorless in your opponent's Active Pokémon's Retreat Cost.",
            cost={PokemonTypes.WATER: 1},
            damage=10,
            damage_operator="+",
            effect=ac.damage_per(_defender_retreat, 30, base=10),
        ),
        Attack(
            title="Jet Headbutt",
            game_text="",
            cost={PokemonTypes.WATER: 2},
            damage=60,
        ),
    ],
)
