"""Silvally (SM - Unified Minds 184/236 -- JP SM10b 043/054).

Stage 1 Colorless Pokemon, evolves from Type: Null. HP 130, weakness
Fighting x2, retreat 2.

  Avenging Heart  [CC] 30+  This attack does 50 more damage for each Prize
                            card your opponent took on their last turn.
  Air Slash       [CCC] 120 Discard an Energy from this Pokemon.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import damage_per, self_energy_discard_attack
from spirit.game.data_utils import Attack, PokemonCardDef


def _opponent_prizes_taken_last_turn(ctx):
    return ctx.session.turn_state.prizes_taken_last_turn.get(ctx.opponent_id, 0)


card = PokemonCardDef(
    guid="99996318-6b82-54e4-92bb-d10df9438a1e",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Silvally.Name",
    display_name="Silvally",
    searchable_by=['Silvally', 'Stage 1', 'Silvally'],
    subtypes=['Stage 1'],
    collector_number=184,
    set_code="SM11",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.TypeNull.Name",
    family_id=772,
    abilities=[
        Attack(title="Avenging Heart", game_text="This attack does 50 more damage for each Prize card your opponent took on their last turn.",
               cost={PokemonTypes.COLORLESS: 2}, damage=30, damage_operator="+",
               effect=damage_per(_opponent_prizes_taken_last_turn, 50, base=30)),
        Attack(title="Air Slash", game_text="Discard an Energy from this Pokémon.",
               cost={PokemonTypes.COLORLESS: 3}, damage=120,
               effect=self_energy_discard_attack(count=1)),
    ],
)
