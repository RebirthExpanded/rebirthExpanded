"""Relicanth (ME - PBL 17 -- JP M5 016, the art here).

Basic Water Pokemon. HP 100, weakness Lightning x2, no resistance,
retreat 1.

  Fossil Beat [C] 10+  This attack does 30 more damage for each of your
                       Benched Pokemon that has "Antique" in its name.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import count_bench, damage_per
from spirit.game.data_utils import Attack, PokemonCardDef, def_for


def _antique(pokemon) -> bool:
    name = getattr(def_for(pokemon.archetype_id), "display_name", "") or ""
    return "Antique" in name


card = PokemonCardDef(
    guid="c449ce21-40bd-523e-be4c-0b7f40b0802b",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Relicanth.Name",
    display_name="Relicanth",
    searchable_by=["Relicanth", "Basic"],
    subtypes=["Basic"],
    collector_number=17,
    set_code="ME5",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=369,
    abilities=[
        Attack(title="Fossil Beat",
               game_text="This attack does 30 more damage for each of your Benched Pokémon that has \"Antique\" in its name.",
               cost={PokemonTypes.COLORLESS: 1},
               damage=10, damage_operator="+",
               effect=damage_per(count_bench("mine", _antique), 30, base=10)),
    ],
)
