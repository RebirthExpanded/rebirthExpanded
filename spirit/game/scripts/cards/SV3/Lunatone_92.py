"""Lunatone (SV - Obsidian Flames 92/197 -- JP SV3 047/108).

Basic Psychic Pokemon. HP 90, weakness Darkness x2, resistance Fighting
-30, retreat 1.

  Ability  New Moon  If you have Solrock in play, prevent all effects of
                     any Stadium done to your Pokemon in play.
  Moon Press  [PCC] 100

NOT YET WIRED: New Moon. The engine has no per-Pokemon "ignore Stadium
passives" switch; the Ability is declared (text and PIE slot) but does
nothing. Moon Press works.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Attack, PokemonCardDef

card = PokemonCardDef(
    guid="a58946cf-c82b-54ec-9959-6b51f192f575",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lunatone.Name",
    display_name="Lunatone",
    searchable_by=["Lunatone", "Basic"],
    subtypes=["Basic"],
    collector_number=92,
    set_code="SV3",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=337,
    regulation_mark="G",
    abilities=[
        Ability(title="New Moon",
                game_text="If you have Solrock in play, prevent all effects of any Stadium done to your Pokémon in play."),
        Attack(title="Moon Press", game_text="",
               cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2}, damage=100),
    ],
)
