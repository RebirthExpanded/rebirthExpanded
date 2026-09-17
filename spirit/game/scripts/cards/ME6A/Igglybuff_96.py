"""Igglybuff (JP M6a 096/103 -- 30th Celebrations).

Basic Colorless Pokemon. HP 30, weakness Fighting x2, no resistance, no
retreat cost.

  Squishy Circle  [C] 30x  30 damage for each of your Benched Pokemon
                           with a maximum HP of 30.

"Maximum HP of 30" is the live figure (effective_max_hp): a 30-HP Pokemon
wearing a Bravery Charm is a 80-HP Pokemon and is not counted, and an HP
30 Pokemon on the Bench counts whether or not it carries damage. The
attacker itself is Active, so it never counts.

The English 30th Celebrations release is not out, so the names here are
this pool's rendering of ぷにぷにサークル and the Japanese collector number
stands.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import damage_per
from spirit.game.data_utils import Attack, PokemonCardDef


def _benched_with_max_hp_30(ctx) -> int:
    return sum(1 for p in ctx.my_bench() if ctx.max_hp(p) == 30)


card = PokemonCardDef(
    guid="9b1b042f-8c87-59bd-81e1-d16ee6dd4b33",
    key="ME6A",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Igglybuff.Name",
    display_name="Igglybuff",
    searchable_by=["Igglybuff", "Basic"],
    subtypes=["Basic"],
    collector_number=96,
    set_code="ME6A",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=174,
    abilities=[
        Attack(
            title="Squishy Circle",
            game_text="This attack does 30 damage for each of your Benched Pokémon that has a maximum HP of 30.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="x",
            effect=damage_per(_benched_with_max_hp_30, 30),
        ),
    ],
)
