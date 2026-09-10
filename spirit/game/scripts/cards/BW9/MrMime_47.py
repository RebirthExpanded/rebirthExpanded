"""Mr. Mime (BW - Plasma Freeze 47/116).

Basic Psychic Pokemon. HP 70, weakness Psychic x2, no resistance,
retreat 1.

  Ability  Bench Barrier  Prevent all damage done to your Benched Pokemon
                          by attacks.

  Psy Bolt [PC] 20  Flip a coin. If heads, the Defending Pokemon is now
                    Paralyzed.

The Ability guards the whole Bench on its own side, this Mr. Mime included
while it sits there, and only against ATTACK damage -- damage counters
placed by an Ability or a Trainer still land, which is exactly what
prevent_damage_when's attacks_only default means.

The SWSH11 Mr. Mime already in the pool is a different card; they share
only a name.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import (PokemonTypes, PokemonStage, Rarities,
                                    SpecialConditions)
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.passives_common import prevent_damage_when


def _my_benched(calc, carrier):
    """A Benched Pokemon on the carrier's own side."""
    target = calc.target
    return (target is not None
            and not calc.to_active
            and target.owning_player_id == carrier.owning_player_id)


card = PokemonCardDef(
    guid="25a43d57-66a2-5a27-9a7b-890877d0e6a7",
    key="BW9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MrMime.Name",
    display_name="Mr. Mime",
    searchable_by=["Mr. Mime", "Basic", "MrMime"],
    subtypes=["Basic"],
    collector_number=47,
    set_code="BW9",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=122,
    abilities=[
        Ability(
            title="Bench Barrier",
            game_text="Prevent all damage done to your Benched Pokémon by attacks.",
            passive=prevent_damage_when(_my_benched),
        ),
        Attack(
            title="Psy Bolt",
            game_text=("Flip a coin. If heads, the Defending Pokémon is now "
                       "Paralyzed."),
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
    ],
)
