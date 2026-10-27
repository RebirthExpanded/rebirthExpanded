"""Zacian (ME6A 85 -- JP M6a 085; English 30C/106). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


def _tooled(ctx) -> bool:
    return ac.has_tool(ctx.attacker)


card = PokemonCardDef(
    guid="20892c3a-61ab-55c9-8a9d-b5e3946d0338",
    key="ME6A",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Zacian.Name",
    display_name="Zacian",
    searchable_by=["Zacian", "Basic"],
    subtypes=["Basic"],
    collector_number=85,
    set_code="ME6A",
    regulation_mark="J",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    family_id=888,
    abilities=[
        Attack(
            title="Hardened Blade",
            game_text="If this Pokémon has a Pokémon Tool attached, this attack does 40 more damage.",
            cost={PokemonTypes.METAL: 1},
            damage=20,
            damage_operator="+",
            effect=ac.bonus_if(_tooled, 40),
        ),
        Attack(
            title="Slashing Strike",
            game_text="During your next turn, this Pokémon can't use Slashing Strike",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            locks_next_turn=True,
        ),
    ],
)
