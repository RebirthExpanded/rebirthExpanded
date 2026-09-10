"""Sobble (Mega Evolution 39/132 -- JP M1S 021/063).

Basic Water. HP 70, weakness Lightning x2, retreat 1, regulation mark I.

  Surprise Attack  [W] 30  Flip a coin. If tails, this attack does nothing.

The plain coin-flip attack, so it is the shared flip_or_nothing factory.
The rest of the Sobble line was already in the pool -- this printing is the
only one of the six that was not.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import flip_or_nothing
from spirit.game.data_utils import Attack, PokemonCardDef

card = PokemonCardDef(
    guid="1e48df18-b2ec-5d69-98f4-543a34792a03",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sobble.Name",
    display_name="Sobble",
    searchable_by=["Sobble", "Basic", "Sobble"],
    subtypes=["Basic"],
    collector_number=39,
    set_code="ME1",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=816,
    abilities=[
        Attack(
            title="Surprise Attack",
            game_text="Flip a coin. If tails, this attack does nothing.",
            cost={PokemonTypes.WATER: 1},
            damage=30,
            effect=flip_or_nothing(),
        ),
    ],
)
