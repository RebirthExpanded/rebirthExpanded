"""Simipour (SV4 42 -- JP SV4M 016; English PAR/42). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.session.passives import Passive, carrier_pokemon
from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES



class MonkeyTrioPassive(Passive):
    """Simisage, Simisear and Simipour in play: no [C] in attack costs."""

    def modify_attack_cost(self, cost, pokemon, carrier, board):
        if pokemon is not carrier or not cost.get("Colorless"):
            return cost
        names = {p.get_attribute(AttrID.EVOLUTION_LOGIC_NAME) for p in board.pokemon_in_play(pokemon.owning_player_id)}
        if {"Simisage", "Simisear", "Simipour"} <= names:
            cost = dict(cost)
            del cost["Colorless"]
        return cost
from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="4f60fc9c-63bc-5a19-ada0-ca77a0b9066a",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Simipour.Name",
    display_name="Simipour",
    searchable_by=["Simipour", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=42,
    set_code="SV4",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Panpour.Name",
    family_id=515,
    abilities=[
        Ability(
            title="Monkey Trio",
            game_text="If you have Simisage, Simisear, and Simipour in play, ignore all Colorless Energy in the costs of attacks used by this Pokémon.",
            passive=MonkeyTrioPassive(),
        ),
        Attack(
            title="Liquid Lashing",
            game_text="This attack also does 30 damage to each of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=ac.spread_damage(30, also_base=True),
        ),
    ],
)
