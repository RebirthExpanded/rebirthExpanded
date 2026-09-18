"""Psyduck (ME2PT5 39 / 226).

Basic Water Pokemon. HP 70, weakness Lightning x2, retreat 1.

  Damp  (Ability)  Pokemon in play (both yours and your opponent's) lose any
                   Ability that requires the Pokemon using it to Knock Out
                   itself.
  Ram   [CC]  20

Damp is a passive that takes ONE Ability away from a Pokemon -- the one
whose text ends "this Pokemon is Knocked Out" / "Knock Out this Pokemon"
(Buzzap, Call Signal, Extra Energy Bomb, Overvolt Discharge, Milotic's
Energy Grace) -- and leaves the rest of that card alone. Those Abilities
carry Ability(self_knockout=True); the offer path asks ability_disabled()
for each Ability separately. Damp is an Ability itself, so an Ability lock
on Psyduck switches it off.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.session.passives import Passive


class DampPassive(Passive):
    """Both sides lose every self-Knock-Out Ability."""

    def blocks_ability(self, pokemon, ability, carrier) -> bool:
        return bool(getattr(ability, "self_knockout", False))


card = PokemonCardDef(
    guid="0a7e2e02-8747-5255-bbe7-d3ae0e27379f",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Psyduck.Name",
    display_name="Psyduck",
    searchable_by=["Psyduck","Basic","Psyduck"],
    subtypes=["Basic"],
    collector_number=39,
    set_code="ME2PT5",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=54,
    abilities=[
        Ability(
            title="Damp",
            game_text="Pokémon in play (both yours and your opponent's) lose any Ability that requires the Pokémon using it to Knock Out itself.",
            passive=DampPassive(),
        ),
        Attack(
            title="Ram",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
