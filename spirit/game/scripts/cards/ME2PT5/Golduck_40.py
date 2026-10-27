"""Golduck (ME2PT5 40 -- JP M2a 033; English ASC/40, MEP/8). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.session.passives import Passive, carrier_pokemon
from spirit.game.card_effects import attacks_common as ac

from spirit.game.attributes import PokemonTypes as _PT


class DampPassive(Passive):
    """Both sides lose every self-Knock-Out Ability."""

    def blocks_ability(self, pokemon, ability, carrier) -> bool:
        return bool(getattr(ability, "self_knockout", False))


card = PokemonCardDef(
    guid="41ae250b-acbb-52fa-9d11-0f4914e30fb4",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Golduck.Name",
    display_name="Golduck",
    searchable_by=["Golduck", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=40,
    set_code="ME2PT5",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Psyduck.Name",
    family_id=54,
    abilities=[
        Ability(
            title="Damp",
            game_text="Pokémon in play (both yours and your opponent's) lose any Ability that requires the Pokémon using it to Knock Out itself.",
            passive=DampPassive(),
        ),
        Attack(
            title="Hydro Pump",
            game_text="This attack does 20 more damage for each Water Energy attached to this Pokémon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
            damage_operator="+",
            effect=ac.damage_per(ac.count_energy("self", _PT.WATER), 20, base=60),
        ),
    ],
)
