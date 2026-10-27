"""Azumarill (SV08 74 -- JP SVLN 004; English SSP/74). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.session.passives import Passive, carrier_pokemon
from spirit.game.card_effects import attacks_common as ac
from spirit.game.data_utils import def_for, subtypes_for


def _has_sub(card, sub) -> bool:
    return card is not None and sub in (subtypes_for(card.archetype_id) or [])



class GlisteningBubblesPassive(Passive):
    """Any Tera Pokemon in play: Double-Edge costs [P]."""

    def modify_attack_cost(self, cost, pokemon, carrier, board):
        if pokemon is not carrier or sum(cost.values()) != 4:
            return cost
        if any(_has_sub(p, "Tera") for p in board.pokemon_in_play(pokemon.owning_player_id)):
            return {"Psychic": 1}
        return cost


card = PokemonCardDef(
    guid="ed50fcd4-4680-523f-9a22-bb7a97ac14c7",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Azumarill.Name",
    display_name="Azumarill",
    searchable_by=["Azumarill", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=74,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Marill.Name",
    family_id=298,
    abilities=[
        Ability(
            title="Glistening Bubbles",
            game_text="If you have any Tera Pokémon in play, this Pokémon can use the Double-Edge attack for Psychic.",
            passive=GlisteningBubblesPassive(),
        ),
        Attack(
            title="Double-Edge",
            game_text="This Pokémon also does 50 damage to itself.",
            cost={PokemonTypes.PSYCHIC: 4},
            damage=230,
            effect=ac.recoil_attack(50),
        ),
    ],
)
