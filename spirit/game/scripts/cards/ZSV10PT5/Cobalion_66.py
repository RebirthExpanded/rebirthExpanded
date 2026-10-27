"""Cobalion (ZSV10PT5 66 -- JP SV11B 068; English BLK/144, BLK/66). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


def _tooled(ctx) -> bool:
    return ac.has_tool(ctx.attacker)


card = PokemonCardDef(
    guid="5ed80eec-9a8b-53c2-9d61-55cef4309540",
    key="ZSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cobalion.Name",
    display_name="Cobalion",
    searchable_by=["Cobalion", "Basic"],
    subtypes=["Basic"],
    collector_number=66,
    set_code="ZSV10PT5",
    regulation_mark="I",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    family_id=638,
    abilities=[
        Attack(
            title="Righteous Edge",
            game_text="Discard a Special Energy from your opponent's Active Pokémon.",
            cost={PokemonTypes.METAL: 1},
            damage=20,
            effect=ac.discard_opponent_energy_attack(1, special_only=True),
        ),
        Attack(
            title="Metal Arms",
            game_text="If this Pokémon has a Pokémon Tool attached, this attack does 40 more damage.",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
            damage_operator="+",
            effect=ac.bonus_if(_tooled, 40),
        ),
    ],
)
