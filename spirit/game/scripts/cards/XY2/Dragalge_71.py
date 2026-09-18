"""Dragalge (XY - Flashfire 71/106 -- JP XY2 057/080, the art here).

Stage 1 Dragon Pokemon (evolves from Skrelp). HP 100, weakness Fairy x2,
no resistance, retreat 1.

  Poison Barrier  (Ability)  Your opponent's Poisoned Pokemon can't retreat.
  Poison Breath   [WPC] 60   Flip a coin. If heads, your opponent's Active
                             Pokemon is now Poisoned.
"""

from spirit.game.attributes import (
    AttrID, CLIENT_SPECIAL_CONDITION_NAMES, PokemonStage, PokemonTypes, Rarities,
    SpecialConditions,
)
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.passives_common import no_retreat_passive
from spirit.game.data_utils import Ability, Attack, PokemonCardDef

_POISONED = CLIENT_SPECIAL_CONDITION_NAMES[SpecialConditions.POISONED]


def _opposing_poisoned(pokemon, carrier) -> bool:
    return (pokemon.owning_player_id != carrier.owning_player_id
            and _POISONED in (pokemon.get_attribute(AttrID.SPECIAL_CONDITIONS) or []))


card = PokemonCardDef(
    guid="f1f815b8-c7a9-58d2-938a-7da49a63f3b5",
    key="XY2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dragalge.Name",
    display_name="Dragalge",
    searchable_by=["Dragalge", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=71,
    set_code="XY2",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FAIRY,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Skrelp.Name",
    family_id=691,
    abilities=[
        Ability(
            title="Poison Barrier",
            game_text="Your opponent's Poisoned Pokémon can't retreat.",
            passive=no_retreat_passive(_opposing_poisoned),
        ),
        Attack(
            title="Poison Breath",
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Poisoned.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
            effect=condition_attack(SpecialConditions.POISONED, flip=True),
        ),
    ],
)
