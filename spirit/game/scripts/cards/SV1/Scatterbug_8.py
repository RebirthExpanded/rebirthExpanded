"""Scatterbug (SV - Scarlet & Violet 8/198 -- JP SV1V 004/078).

Basic Grass Pokemon. HP 30, weakness Fire x2, retreat 1, regulation mark G.

  Ability  Adaptive Evolution  This Pokemon can evolve during your first
                               turn or the turn you play it.
  Tackle  [GC] 20

Caterpie's Ability by another name -- may_evolve_early, which lifts both
evolution turn gates for the holder alone.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Attack, PokemonCardDef
from spirit.game.session.passives import Passive, carrier_pokemon


class AdaptiveEvolutionPassive(Passive):
    def may_evolve_early(self, pokemon, carrier):
        return carrier_pokemon(carrier) is pokemon


card = PokemonCardDef(
    guid="b774fbdf-2f2a-583a-8e2f-235bb95014b3",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Scatterbug.Name",
    display_name="Scatterbug",
    searchable_by=["Scatterbug", "Basic"],
    subtypes=["Basic"],
    collector_number=8,
    set_code="SV1",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=664,
    abilities=[
        Ability(
            title="Adaptive Evolution",
            game_text="This Pokémon can evolve during your first turn or the turn you play it.",
            passive=AdaptiveEvolutionPassive(),
        ),
        Attack(
            title="Tackle",
            game_text="",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)
