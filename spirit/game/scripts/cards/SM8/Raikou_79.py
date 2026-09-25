"""Raikou (SM - Lost Thunder 79/214 -- JP SM8 037/095).

Basic Lightning Pokemon. HP 120, weakness Fighting x2, resistance Metal -20,
retreat 2.

  Lost Voltage  [LC] 30+  If you have any [L] Energy cards in the Lost Zone,
                          this attack does 90 more damage.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import bonus_if
from spirit.game.session.effects import is_energy_of_type
from spirit.game.data_utils import Attack, PokemonCardDef


def _lightning_in_lost_zone(ctx) -> bool:
    return any(is_energy_of_type(c, PokemonTypes.LIGHTNING) for c in ctx.lost_zone())


card = PokemonCardDef(
    guid="eee5dfa9-954e-50bc-9c06-0fc4e4a6cb3c",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Raikou.Name",
    display_name="Raikou",
    searchable_by=['Raikou', 'Basic', 'Raikou'],
    subtypes=['Basic'],
    collector_number=79,
    set_code="SM8",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=243,
    abilities=[
        Attack(title="Lost Voltage", game_text="If you have any Lightning Energy cards in the Lost Zone, this attack does 90 more damage.",
               cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1}, damage=30, damage_operator="+",
               effect=bonus_if(_lightning_in_lost_zone, 90)),
    ],
)
