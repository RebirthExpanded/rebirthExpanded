"""Lunatone (SV - Obsidian Flames 92/197 -- JP SV3 047/108).

Basic Psychic Pokemon. HP 90, weakness Darkness x2, resistance Fighting
-30, retreat 1.

  Ability  New Moon  If you have Solrock in play, prevent all effects of
                     any Stadium done to your Pokemon in play.
  Moon Press  [PCC] 100

New Moon rides passives.py's stadium-shield state: NewMoonPassive only
answers the printed condition (a Solrock on this side), and the engine
decides -- order-dependently, as the official Q&A rules it -- whether the
shield is up. Silent Lab played onto a working New Moon is prevented;
Lunatone put into play under Silent Lab never switches on; Garbotoxin
switches it off (a Stealthy Hood on Lunatone stops that). Player-level
Stadium effects (Sky Field's Bench, Collapsed Stadium's discard, Luminous
Maze Forest's re-flip) still apply; Temple of Sinnoh, Lost City, Beach
Court, Crystal Cave, Magma Basin, Gapejaw Bog and the like do not.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Attack, PokemonCardDef, def_for
from spirit.game.session.passives import Passive


class NewMoonPassive(Passive):
    def stadium_immunity(self, board, carrier):
        return any(
            getattr(def_for(p.archetype_id), "display_name", "") == "Solrock"
            for p in board.pokemon_in_play(carrier.owning_player_id))


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
                game_text="If you have Solrock in play, prevent all effects of any Stadium done to your Pokémon in play.",
                passive=NewMoonPassive()),
        Attack(title="Moon Press", game_text="",
               cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2}, damage=100),
    ],
)
