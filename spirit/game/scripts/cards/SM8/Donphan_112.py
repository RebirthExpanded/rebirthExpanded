"""Donphan (SM - Lost Thunder 112/214 -- JP SM8 051/095, the art here).

Stage 1 Fighting Pokemon (evolves from Phanpy). HP 130, weakness Water
x2, retreat 4.

  Sturdy        (Ability)  If this Pokemon has full HP and would be
                           Knocked Out by damage from an attack, this
                           Pokemon is not Knocked Out, and its remaining
                           HP becomes 10.
  Rolling Spin  [FC] 70    During your next turn, this Pokemon's Rolling
                           Spin attack does 70 more damage (before
                           applying Weakness and Resistance).

Sturdy is the pool's KO-survive interceptor with no coin and the full-HP
gate; the Rolling Spin rider is Scyther's next-turn boost keyed to this
entity and this attack title, so only the same Donphan's same attack
grows.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.passives_common import (boost_own_next_turn,
                                                       guts_survive_passive)
from spirit.game.data_utils import Ability, Attack, PokemonCardDef

BONUS = 70


card = PokemonCardDef(
    guid="45d1bdc4-b468-5919-9cf1-a2aca9915652",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Donphan.Name",
    display_name="Donphan",
    searchable_by=["Donphan", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=112,
    set_code="SM8",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Phanpy.Name",
    family_id=231,
    abilities=[
        Ability(
            title="Sturdy",
            game_text="If this Pokémon has full HP and would be Knocked Out by damage from an attack, this Pokémon is not Knocked Out, and its remaining HP becomes 10.",
            passive=guts_survive_passive(hp_floor=10, title="Sturdy", flip=False,
                                         require_full_hp=True),
        ),
        Attack(
            title="Rolling Spin",
            game_text="During your next turn, this Pokémon's Rolling Spin attack does 70 more damage (before applying Weakness and Resistance).",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=70,
            effect=boost_own_next_turn(BONUS, attack_title="Rolling Spin"),
        ),
    ],
)
