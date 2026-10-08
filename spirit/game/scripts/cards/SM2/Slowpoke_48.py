"""Slowpoke (SM - Guardians Rising 48/145 -- JP SM2K 023/050, the art here).

Basic Psychic Pokemon. HP 70, weakness Psychic x2, retreat 3.

  Headbutt       [C]   10
  Whimsy Tackle  [PCC] 60  Flip a coin. If tails, this attack does nothing.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import flip_or_nothing
from spirit.game.data_utils import Attack, PokemonCardDef

card = PokemonCardDef(
    guid="85b60f6a-c818-5a23-bbe8-93f99595348a",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Slowpoke.Name",
    display_name="Slowpoke",
    searchable_by=["Slowpoke", "Basic"],
    subtypes=["Basic"],
    collector_number=48,
    set_code="SM2",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=79,
    abilities=[
        Attack(
            title="Headbutt",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Whimsy Tackle",
            game_text="Flip a coin. If tails, this attack does nothing.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=flip_or_nothing(),
        ),
    ],
)
