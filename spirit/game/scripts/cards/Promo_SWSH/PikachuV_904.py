"""Pikachu V (JP 25th Anniversary Golden Box, S8a-G 005/015 -- the art
here). No English print; 904 is this pool's own number in the SWSH promos.

Basic Lightning Pokemon V. HP 190, weakness Fighting x2, no resistance,
retreat 1.

  Pika Ball       [L]   30
  Electro Circle  [LL]  30x  This attack does 30 damage for each of your
                             Benched Pokemon.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import count_bench, damage_per
from spirit.game.data_utils import Attack, PokemonCardDef

card = PokemonCardDef(
    guid="097d3a5f-90f3-5563-a616-77c678e2b873",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.PikachuV.Name",
    display_name="Pikachu V",
    searchable_by=["Pikachu V", "Basic", "V", "PikachuV"],
    subtypes=["Basic", "V"],
    collector_number=904,
    set_code="Promo_SWSH",
    regulation_mark="E",
    rarity=Rarities.RarePromo,
    hp=190,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=25,
    abilities=[
        Attack(
            title="Pika Ball",
            game_text="",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=30,
        ),
        Attack(
            title="Electro Circle",
            game_text="This attack does 30 damage for each of your Benched Pokémon.",
            cost={PokemonTypes.LIGHTNING: 2},
            damage=30,
            damage_operator="x",
            effect=damage_per(count_bench("mine"), 30),
        ),
    ],
)
