"""Chandelure (RSV10PT5 18 -- JP SV11B 017; English WHT/103, WHT/18). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card


def _basic_fire(card):
    return is_basic_energy_card(card) and is_energy_of_type(card, PokemonTypes.FIRE)


def _ten_fire(ctx) -> bool:
    return sum(1 for c in ctx.discard_pile() if _basic_fire(c)) >= 10


card = PokemonCardDef(
    guid="24dc9184-9c90-5597-83ae-75f3be6c7e10",
    key="RSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Chandelure.Name",
    display_name="Chandelure",
    searchable_by=["Chandelure", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=18,
    set_code="RSV10PT5",
    regulation_mark="I",
    rarity=Rarities.Rare,
    hp=150,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Lampent.Name",
    family_id=607,
    abilities=[
        Attack(
            title="Incendiary Pillar",
            game_text="If you have 10 or more Basic Fire Energy cards in your discard pile, this attack does 100 more damage.",
            cost={PokemonTypes.FIRE: 1},
            damage=50,
            damage_operator="+",
            effect=ac.bonus_if(_ten_fire, 100),
        ),
        Attack(
            title="Burn It All Up",
            game_text="Discard all Energy from this Pokémon.",
            cost={PokemonTypes.FIRE: 2},
            damage=180,
            effect=ac.self_energy_discard_attack(all_energy=True),
        ),
    ],
)
