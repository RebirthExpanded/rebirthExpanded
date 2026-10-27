"""Incineroar ex (SV05 34 -- JP SV5M 022; English TEF/187, TEF/34). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac
from spirit.game.session.passives import Passive, carrier_pokemon



class HustlePlayPassive(Passive):
    """Attacks cost [C] less for each of the opponent's Benched Pokemon."""

    def modify_attack_cost(self, cost, pokemon, carrier, board):
        if pokemon is not carrier:
            return cost
        other = next((pid for pid in board.player_ids if pid != pokemon.owning_player_id), None)
        bench = board.find_player_area(other, "bench") if other else None
        n = len(bench.children) if bench else 0
        if n and cost.get("Colorless"):
            cost = dict(cost)
            cost["Colorless"] = max(0, cost["Colorless"] - n)
            if not cost["Colorless"]:
                del cost["Colorless"]
        return cost


card = PokemonCardDef(
    guid="33d11382-b526-568f-9e09-23fcfaaecac3",
    key="SV05",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Incineroarex.Name",
    display_name="Incineroar ex",
    searchable_by=["Incineroar ex", "Stage 2", "ex"],
    subtypes=["Stage 2", "ex"],
    collector_number=34,
    set_code="SV05",
    regulation_mark="H",
    rarity=Rarities.RareHoloEX,
    hp=320,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Torracat.Name",
    family_id=725,
    abilities=[
        Ability(
            title="Hustle Play",
            game_text="Attacks used by this Pokémon cost Colorless less for each of your opponent's Benched Pokémon.",
            passive=HustlePlayPassive(),
        ),
        Attack(
            title="Blaze Blast",
            game_text="Your opponent's Active Pokémon is now Burned.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 4},
            damage=240,
            effect=ac.condition_attack(SpecialConditions.BURNED),
        ),
    ],
)
