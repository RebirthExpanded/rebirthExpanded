"""Toedscruel (SV - Paradox Rift 17/182 -- JP SV4M 008/066).

Stage 1 Grass Pokemon, evolves from Toedscool. HP 120, weakness Fire x2,
retreat 2.

  Ability  Slime Mold Colony  Cards in your opponent's discard pile can't
                              be put into their hand by an effect of your
                              opponent's Abilities or Trainer cards.
  Mushroom Drain  [GCC] 80  Heal 30 damage from this Pokemon.

The block rides blocks_discard_recovery, consulted by put_in_hand for a
card leaving a discard pile under an Ability or Trainer of that pile's
owner; attacks (Odor Sleuth) are not named and still work.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.support_common import heal_attack
from spirit.game.data_utils import Ability, Attack, PokemonCardDef
from spirit.game.session.passives import Passive


class SlimeMoldColonyPassive(Passive):
    def blocks_discard_recovery(self, player_id, carrier):
        return player_id != carrier.owning_player_id


card = PokemonCardDef(
    guid="e5d1e354-2477-5e9f-b44c-2853d356e46a",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Toedscruel.Name",
    display_name="Toedscruel",
    searchable_by=["Toedscruel", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=17,
    set_code="SV4",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Toedscool.Name",
    family_id=948,
    regulation_mark="G",
    abilities=[
        Ability(title="Slime Mold Colony",
                game_text="Cards in your opponent's discard pile can't be put into their hand by an effect of your opponent's Abilities or Trainer cards.",
                passive=SlimeMoldColonyPassive()),
        Attack(title="Mushroom Drain", game_text="Heal 30 damage from this Pokémon.",
               cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2}, damage=80,
               effect=heal_attack(30)),
    ],
)
