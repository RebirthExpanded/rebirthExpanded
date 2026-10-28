"""Greedent (SV1 152 -- JP SV1V 062; English PAF/206, SVI/152). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


def _tooled(ctx) -> bool:
    return ac.has_tool(ctx.attacker)


card = PokemonCardDef(
    guid="72a8ce94-b3f2-59d9-a6a4-44a8aed07030",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Greedent.Name",
    display_name="Greedent",
    searchable_by=["Greedent", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=152,
    set_code="SV1",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Skwovet.Name",
    family_id=819,
    abilities=[
        Attack(
            title="Bite",
            game_text="",
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
        Attack(
            title="Enhanced Fang",
            game_text="If this Pokémon has a Pokémon Tool attached, this attack does 80 more damage.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=80,
            damage_operator="+",
            effect=ac.bonus_if(_tooled, 80),
        ),
    ],
)
