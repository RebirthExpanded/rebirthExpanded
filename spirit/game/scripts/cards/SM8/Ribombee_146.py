"""Ribombee (SM - Lost Thunder 146/214 -- JP SM7b 035/050).

Stage 1 Fairy Pokemon, evolves from Cutiefly. HP 60, weakness Metal x2,
resistance Darkness -20, retreat 0.

  Ability  Mysterious Buzz  As long as this Pokemon is on your Bench,
                            whenever your opponent plays a Supporter card
                            from their hand, prevent all effects of that
                            card done to your [Y] Pokemon in play.
  Stampede  [Y] 20

Princess's Curtain for Fairy Pokemon: the same Supporter shield, gated on
Ribombee being Benched, protecting every in-play [Y] Pokemon (live types)
of its owner -- attachments included, as effects done to their holder.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.passives_common import (is_in_active_spot,
                                                       trainer_effect_shield_passive)
from spirit.game.data_utils import Ability, Attack, PokemonCardDef
from spirit.game.session.effects import is_pokemon_of_type
from spirit.game.session.passives import carrier_pokemon


def _my_fairy_pokemon(entity, carrier):
    holder = carrier_pokemon(entity) if entity is not None else None
    if holder is None or holder.owning_player_id != carrier.owning_player_id:
        return False
    return is_pokemon_of_type(holder, PokemonTypes.FAIRY)


def _on_bench(board, carrier) -> bool:
    return not is_in_active_spot(carrier)


card = PokemonCardDef(
    guid="1ab15f4a-09b3-5fb7-80e6-a9680e8c4ced",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ribombee.Name",
    display_name="Ribombee",
    searchable_by=["Ribombee", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=146,
    set_code="SM8",
    rarity=Rarities.Rare,
    hp=60,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.DARKNESS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Cutiefly.Name",
    family_id=742,
    abilities=[
        Ability(
            title="Mysterious Buzz",
            game_text="As long as this Pokémon is on your Bench, whenever your opponent plays a Supporter card from their hand, prevent all effects of that card done to your [Y] Pokémon in play.",
            passive=trainer_effect_shield_passive(
                protects=_my_fairy_pokemon, condition=_on_bench),
        ),
        Attack(title="Stampede", game_text="",
               cost={PokemonTypes.FAIRY: 1}, damage=20),
    ],
)
