"""Spewpa (SV - Scarlet & Violet 9/198 -- JP SV1V 005/078).

Stage 1 Grass Pokemon, evolves from Scatterbug. HP 70, weakness Fire x2,
retreat 3, regulation mark G.

  Ability  Adaptive Evolution  This Pokemon can evolve during your first
                               turn or the turn you play it.
  Bug Bite  [GC] 30

The Ability matters more here than on the Basic: with both halves of the
line carrying it, a Scatterbug played this turn can reach Vivillon on the
same turn.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Attack, PokemonCardDef
from spirit.game.session.passives import Passive, carrier_pokemon


class AdaptiveEvolutionPassive(Passive):
    def may_evolve_early(self, pokemon, carrier):
        return carrier_pokemon(carrier) is pokemon


card = PokemonCardDef(
    guid="227399e3-4f37-5e19-8e17-91d1cb6d95f7",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Spewpa.Name",
    display_name="Spewpa",
    searchable_by=["Spewpa", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=9,
    set_code="SV1",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Scatterbug.Name",
    family_id=664,
    abilities=[
        Ability(
            title="Adaptive Evolution",
            game_text="This Pokémon can evolve during your first turn or the turn you play it.",
            passive=AdaptiveEvolutionPassive(),
        ),
        Attack(
            title="Bug Bite",
            game_text="",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)
