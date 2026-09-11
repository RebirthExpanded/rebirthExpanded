"""Feebas (SM - Dragon Majesty 28/70 -- JP SM6a 013/053).

Basic Water Pokemon. HP 30, weakness Grass x2, retreat 1.

  Ability  Submerge  As long as this Pokemon is on your Bench, prevent all
                     damage done to this Pokemon by attacks (both yours and
                     your opponent's).
  Rain Splash  [W] 10

A prevents_damage passive answering only while its carrier is Benched and
only for attack damage: damage counters placed by an effect are not
"damage done by attacks", and a Benched Feebas still takes those.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Attack, PokemonCardDef
from spirit.game.session.passives import Passive


class SubmergePassive(Passive):
    def prevents_damage(self, calc, carrier):
        return calc.is_attack and calc.target is carrier and not calc.to_active


card = PokemonCardDef(
    guid="3f316fa3-9816-5311-9a87-3acb1699bf8f",
    key="DM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Feebas.Name",
    display_name="Feebas",
    searchable_by=["Feebas", "Basic"],
    subtypes=["Basic"],
    collector_number=28,
    set_code="DM",
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=349,
    abilities=[
        Ability(
            title="Submerge",
            game_text="As long as this Pokémon is on your Bench, prevent all damage done to this Pokémon by attacks (both yours and your opponent's).",
            passive=SubmergePassive(),
        ),
        Attack(title="Rain Splash", game_text="",
               cost={PokemonTypes.WATER: 1}, damage=10),
    ],
)
