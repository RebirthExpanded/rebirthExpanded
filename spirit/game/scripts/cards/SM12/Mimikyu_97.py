"""Mimikyu (SM - Cosmic Eclipse 97/236 -- JP SM12a 063/173, the art here).

Basic Psychic Pokemon. HP 70, no weakness, retreat 1.

  Ability: Shadow Box  Pokemon-GX that have any damage counters on them
                       (both yours and your opponent's) have no Abilities.
  Tail Trickery [CC] 20  Flip a coin. If heads, your opponent's Active
                         Pokemon is now Confused.

An Ability lock read live: a Pokemon-GX loses its Abilities the moment a
damage counter lands on it (Rainbow Energy's counter before Venusaur &
Snivy-GX's Shining Vine -- official Q&A) and gets them back once healed.
"""

from spirit.game.attributes import AttrID, PokemonStage, PokemonTypes, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.passives_common import ability_lock_passive
from spirit.game.data_utils import Ability, Attack, PokemonCardDef, subtypes_for
from spirit.game.models.board import board_of


def _damaged_gx(pokemon, carrier) -> bool:
    """A Pokemon-GX with damage counters on it. Asked from inside the lock
    scan, so it reads the last settled max HP (board.effective_max_seen)
    instead of re-running the passives; printed HP when none is recorded."""
    if "GX" not in subtypes_for(pokemon.archetype_id):
        return False
    hp = pokemon.get_attribute(AttrID.HP, 0)
    printed = int(pokemon.attribute_originals.get(AttrID.HP.value, hp) or hp)
    board = board_of(pokemon)
    seen = getattr(board, "effective_max_seen", None) or {}
    return hp < seen.get(pokemon.entity_id, printed)


card = PokemonCardDef(
    guid="7d8b4253-0f5f-5a9b-990d-7447bb7d2eba",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mimikyu.Name",
    display_name="Mimikyu",
    searchable_by=["Mimikyu", "Basic"],
    subtypes=["Basic"],
    collector_number=97,
    set_code="SM12",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    family_id=778,
    abilities=[
        Ability(
            title="Shadow Box",
            game_text="Pokémon-GX that have any damage counters on them (both yours and your opponent's) have no Abilities.",
            passive=ability_lock_passive(_damaged_gx),
        ),
        Attack(
            title="Tail Trickery",
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Confused.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            effect=condition_attack(SpecialConditions.CONFUSED, flip=True),
        ),
    ],
)
