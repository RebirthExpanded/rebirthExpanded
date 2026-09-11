"""Jolteon (XY - Ancient Origins 26/98 -- JP XY7-B 014/069).

Stage 1 Lightning Pokemon, evolves from Eevee. HP 90, weakness Fighting
x2, resistance Metal -20, retreat 0.

  Ability  Electric Effect  As long as this Pokemon is in play, each of
                            your Stage 1 Pokemon is [L] type in addition
                            to its existing types.
  Thunder Blast  [LCC] 80  Discard an Energy attached to this Pokemon.

Vaporeon's Aqua Effect in Lightning: the [L] rides the live type list, so
Electropower's +30 reaches a Stage 1 made Lightning this way.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import self_energy_discard_attack
from spirit.game.card_effects.pokemon import stage_one_type_grant
from spirit.game.data_utils import Ability, Attack, PokemonCardDef

card = PokemonCardDef(
    guid="887d42ac-f87f-549a-979e-ab99c65352bb",
    key="XY7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Jolteon.Name",
    display_name="Jolteon",
    searchable_by=["Jolteon", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=26,
    set_code="XY7",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    family_id=133,
    abilities=[
        Ability(
            title="Electric Effect",
            game_text="As long as this Pokémon is in play, each of your Stage 1 Pokémon is [L] type in addition to its existing types.",
            passive=stage_one_type_grant(PokemonTypes.LIGHTNING),
        ),
        Attack(
            title="Thunder Blast",
            game_text="Discard an Energy attached to this Pokémon.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            effect=self_energy_discard_attack(count=1),
        ),
    ],
)
