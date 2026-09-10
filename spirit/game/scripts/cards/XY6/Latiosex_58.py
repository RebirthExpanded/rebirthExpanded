"""Latios-EX (XY - Roaring Skies 58/108 -- JP XY6 048/078).

Basic Dragon Pokemon-EX. HP 170, weakness Fairy x2, retreat 2.

  Fast Raid    [P]     40  If you go first, you can use this attack on your
                           first turn.
  Light Pulse  [WPPC] 110  Prevent all effects of your opponent's attacks,
                           except damage, done to this Pokemon during your
                           opponent's next turn.

The pool's first uppercase Pokemon-EX. Nothing new is needed for the rule
box: data_utils has carried "EX" in its multi-prize table all along (2
Prizes, and a rule box for everything that reads one), it simply had no
card to read until now. It is also the first live holder of the subtype
Counter Energy's exclusion names, which was written against this era.

Light Pulse is protect_next_turn's effects-only setting: damage still
lands in full, everything else an attack would do to Latios-EX -- Special
Conditions, discards, switching -- does not. It is the attack-effect
shield, not the damage one, so reduce/prevent stay off.

Fast Raid is the same per-attack turn-1 permission Pheromosa-GX carries.
"""

from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.passives_common import protect_next_turn

card = PokemonCardDef(
    guid="d6151b57-3602-596a-9c78-2707dba09b8e",
    key="XY6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Latiosex.Name",
    display_name="Latios-EX",
    searchable_by=["Latios-EX", "Basic", "EX", "Latiosex"],
    subtypes=["Basic", "EX"],
    collector_number=58,
    set_code="XY6",
    rarity=Rarities.RareHoloEX,
    hp=170,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FAIRY,
    family_id=381,
    abilities=[
        Attack(
            title="Fast Raid",
            game_text="If you go first, you can use this attack on your first turn.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=40,
            usable_first_turn=True,
        ),
        Attack(
            title="Light Pulse",
            game_text="Prevent all effects of your opponent's attacks, except damage, done to this Pokémon during your opponent's next turn.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.PSYCHIC: 2,
                  PokemonTypes.COLORLESS: 1},
            damage=110,
            effect=protect_next_turn(effects_too=True),
        ),
    ],
)
