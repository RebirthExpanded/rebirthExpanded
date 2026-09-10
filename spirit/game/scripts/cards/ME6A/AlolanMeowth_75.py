"""Alolan Meowth (JP M6a 075/103 -- 30th Celebrations).

Basic Darkness. HP 60, weakness Grass x2, retreat 1, regulation mark J.

  Pay Day  [D] 10  Draw a card.

Alolan Persian-GX's partner in the anniversary set, and the plainest half
of the pair. The English 30th Celebrations release is not out, so the
Japanese collector number stands.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.support_common import draw_attack
from spirit.game.data_utils import Attack, PokemonCardDef

card = PokemonCardDef(
    guid="ca12f1ba-dbc6-5147-b300-343d6440d4d9",
    key="ME6A",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.AlolanMeowth.Name",
    display_name="Alolan Meowth",
    searchable_by=["Alolan Meowth", "Basic", "AlolanMeowth"],
    subtypes=["Basic"],
    collector_number=75,
    set_code="ME6A",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=52,
    abilities=[
        Attack(
            title="Pay Day",
            game_text="Draw a card.",
            cost={PokemonTypes.DARKNESS: 1},
            damage=10,
            effect=draw_attack(1),
        ),
    ],
)
