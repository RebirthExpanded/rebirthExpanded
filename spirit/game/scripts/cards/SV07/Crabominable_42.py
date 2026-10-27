"""Crabominable (SV07 42 -- JP SV7 024; English SCR/149, SCR/42, SVP/134). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.session.passives import Passive, carrier_pokemon
from spirit.game.data_utils import def_for, subtypes_for



class FoodPrepPassive(Passive):
    """Attacks cost [C] less for each Kofu card in your discard pile."""

    def modify_attack_cost(self, cost, pokemon, carrier, board):
        if pokemon is not carrier or not cost.get("Colorless"):
            return cost
        discard = board.find_player_area(pokemon.owning_player_id, "discard")
        n = sum(1 for c in (discard.children if discard else [])
                if getattr(def_for(c.archetype_id), "display_name", "") == "Kofu")
        if not n:
            return cost
        cost = dict(cost)
        cost["Colorless"] = max(0, cost["Colorless"] - n)
        if not cost["Colorless"]:
            del cost["Colorless"]
        return cost


card = PokemonCardDef(
    guid="e00b7026-3e6c-5204-8299-2dabc243cc97",
    key="SV07",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Crabominable.Name",
    display_name="Crabominable",
    searchable_by=["Crabominable", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=42,
    set_code="SV07",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    hp=160,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Crabrawler.Name",
    family_id=739,
    abilities=[
        Ability(
            title="Food Prep",
            game_text="Attacks used by this Pokémon cost Colorless less for each Kofu card in your discard pile.",
            passive=FoodPrepPassive(),
        ),
        Attack(
            title="Haymaker",
            game_text="During your next turn, this Pokémon can't use Haymaker.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 4},
            damage=250,
            locks_next_turn=True,
        ),
    ],
)
