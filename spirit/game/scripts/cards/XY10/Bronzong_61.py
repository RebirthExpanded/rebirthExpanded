"""Bronzong (XY - Fates Collide 61/124 -- JP XY9-B 048/080).

Stage 1 Metal Pokemon, evolves from Bronzor. HP 100, weakness Fire x2,
resistance Psychic -20, retreat 3.

  Ability  Metal Fortress  Prevent all effects of your opponent's attacks,
                           including damage, done to your Benched Pokemon.
  Guard Press  [MCC] 60  During your opponent's next turn, any damage done
                         to this Pokemon by attacks is reduced by 20.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.passives_common import is_in_active_spot, protect_next_turn
from spirit.game.data_utils import Ability, Attack, PokemonCardDef
from spirit.game.session.passives import Passive, carrier_pokemon


class MetalFortressPassive(Passive):
    def _protected(self, target, carrier):
        holder = carrier_pokemon(target) if target is not None else None
        return holder is not None and holder.owning_player_id == carrier.owning_player_id \
            and not is_in_active_spot(holder)

    def prevents_damage(self, calc, carrier):
        return bool(calc.is_attack and calc.is_opposing and self._protected(calc.target, carrier))

    def blocks_attack_effects(self, target, carrier, source=None):
        if source is not None and source.owning_player_id == carrier.owning_player_id:
            return False
        return self._protected(target, carrier)


card = PokemonCardDef(
    guid="f3e4ebe0-c027-5226-acec-15cff68f9a54",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bronzong.Name",
    display_name="Bronzong",
    searchable_by=["Bronzong", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=61,
    set_code="XY10",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Bronzor.Name",
    family_id=436,
    abilities=[
        Ability(title="Metal Fortress",
                game_text="Prevent all effects of your opponent's attacks, including damage, done to your Benched Pokémon.",
                passive=MetalFortressPassive()),
        Attack(title="Guard Press",
               game_text="During your opponent's next turn, any damage done to this Pokémon by attacks is reduced by 20 (after applying Weakness and Resistance).",
               cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2}, damage=60,
               effect=protect_next_turn(reduce=20)),
    ],
)
