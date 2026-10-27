"""Toedscruel (SV09 89 -- JP SVM 071; English JTG/89). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.session.passives import Passive, carrier_pokemon



class SecretForestPathPassive(Passive):
    """On your Bench: your Active Pokemon's Retreat Cost is [C][C] less."""

    def modify_retreat_cost(self, cost, pokemon, carrier, board):
        if (carrier.owning_player_id == pokemon.owning_player_id and carrier._containing_area_name() == "bench"
                and board.active_pokemon(pokemon.owning_player_id) is pokemon):
            return max(0, cost - 2)
        return cost


card = PokemonCardDef(
    guid="7b1cc29d-37b1-5529-9fe2-0ad0511c5070",
    key="SV09",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Toedscruel.Name",
    display_name="Toedscruel",
    searchable_by=["Toedscruel", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=89,
    set_code="SV09",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Toedscool.Name",
    family_id=948,
    abilities=[
        Ability(
            title="Secret Forest Path",
            game_text="As long as this Pokémon is on your Bench, your Active Pokémon's Retreat Cost is ColorlessColorless less.",
            passive=SecretForestPathPassive(),
        ),
        Attack(
            title="Mud Shot",
            game_text="",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
        ),
    ],
)
