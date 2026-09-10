"""Pheromosa-GX (SM - Ultra Prism 140/156 -- JP SM4+ 012/114).

Basic Grass Pokemon-GX, Ultra Beast. HP 170, weakness Fire x2, retreat 1.

  Fast Raid    [G]  30  If you go first, you can use this attack on your
                        first turn.
  Cruel Spike  [GG] 60  Your opponent's Active Pokemon is now Confused.
  Beauty-GX    [GG] 50x This attack does 50 damage for each Prize card your
                        opponent has taken.

Fast Raid is the per-attack first-turn permission the engine already had
before Meloetta ex generalised it: usable_first_turn on this attack alone,
so Cruel Spike and Beauty-GX stay illegal on turn 1 going first.

Beauty-GX counts Prizes your opponent has TAKEN, not the ones they have
left -- the two differ once anything has moved Prizes around (Naganadel-GX
deals three, Redeemable Ticket re-lays them), so it goes through
count_prizes_taken rather than 6 minus the pile.

Ultra Beast is the subtype Beast Energy and Beast Ring read, so this
Pokemon is a live holder for both.
"""

from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import (PokemonStage, PokemonTypes, Rarities,
                                    SpecialConditions)
from spirit.game.card_effects.attacks_common import (condition_attack,
                                                     count_prizes_taken,
                                                     damage_per)

card = PokemonCardDef(
    guid="1364e41b-2954-5ede-95ce-e08581304502",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pheromosagx.Name",
    display_name="Pheromosa-GX",
    searchable_by=["Pheromosa-GX", "Basic", "GX", "Ultra Beast", "Pheromosagx"],
    subtypes=["Basic", "GX", "Ultra Beast"],
    collector_number=140,
    set_code="SM5",
    rarity=Rarities.RareUltra,
    hp=170,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=795,
    abilities=[
        Attack(
            title="Fast Raid",
            game_text="If you go first, you can use this attack on your first turn.",
            cost={PokemonTypes.GRASS: 1},
            damage=30,
            usable_first_turn=True,
        ),
        Attack(
            title="Cruel Spike",
            game_text="Your opponent's Active Pokémon is now Confused.",
            cost={PokemonTypes.GRASS: 2},
            damage=60,
            effect=condition_attack(SpecialConditions.CONFUSED),
        ),
        Attack(
            title="Beauty-GX",
            game_text="This attack does 50 damage for each Prize card your opponent has taken. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.GRASS: 2},
            gx=True,
            effect=damage_per(count_prizes_taken("opponent"), 50),
        ),
    ],
)
