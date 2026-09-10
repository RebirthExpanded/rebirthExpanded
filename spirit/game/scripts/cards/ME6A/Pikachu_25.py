"""Pikachu (JP M6a 025/103 -- 30th Celebrations 09/30).

Basic Lightning. HP 50, weakness Fighting x2, no resistance, no retreat
cost, regulation mark J.

  Gnaw  [C] 10

The plainest card in the pool and the only thing worth saying about it is
the set: the English 30th Celebrations release is not out yet, so there is
no English numbering to follow. It is registered as ME6A and keeps the
Japanese collector number; if the English print numbers it differently,
the number here is the one to change.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Attack, PokemonCardDef

card = PokemonCardDef(
    guid="9893ec0b-63ad-5547-8a63-da9ed438bcd5",
    key="ME6A",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pikachu.Name",
    display_name="Pikachu",
    searchable_by=["Pikachu", "Basic", "Pikachu"],
    subtypes=["Basic"],
    collector_number=25,
    set_code="ME6A",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=25,
    abilities=[
        Attack(
            title="Gnaw",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)
