"""Team Rocket's Porygon2 (SV - Destined Rivals 154/182 -- JP SV10 082/099, the art here).

Stage 1 Colorless Pokemon, evolves from Team Rocket's Porygon. HP 90,
weakness Fighting x2, no resistance, retreat 1.

  R Command [CCC] 20x  This attack does 20 damage for each Supporter card
                       that has "Team Rocket" in its name in your discard
                       pile.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import count_discard, damage_per
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, def_for
from spirit.game.session.effects import is_supporter_card


def _team_rocket_supporter(card) -> bool:
    name = getattr(def_for(card.archetype_id), "display_name", "") or ""
    return is_supporter_card(card) and "Team Rocket" in name


card = PokemonCardDef(
    guid="89a1b0b7-a0d8-53d6-b01b-5bb5c12cb220",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsPorygon2.Name",
    display_name="Team Rocket's Porygon2",
    searchable_by=["Team Rocket's Porygon2", "Stage 1", "TeamRocketsPorygon2"],
    subtypes=["Stage 1"],
    collector_number=154,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsPorygon.Name",
    family_id=137,
    abilities=[
        Attack(title="R Command",
               game_text="This attack does 20 damage for each Supporter card that has \"Team Rocket\" in its name in your discard pile.",
               cost={PokemonTypes.COLORLESS: 3},
               damage=20, damage_operator="x",
               effect=damage_per(count_discard("mine", _team_rocket_supporter), 20)),
    ],
)
