"""Veluza (SV07 45 -- JP SV7 027; English SCR/45). Japanese art.
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
from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="6930e202-76c1-56fd-9cb2-d0b61e4adb0f",
    key="SV07",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Veluza.Name",
    display_name="Veluza",
    searchable_by=["Veluza", "Basic"],
    subtypes=["Basic"],
    collector_number=45,
    set_code="SV07",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=976,
    abilities=[
        Ability(
            title="Food Prep",
            game_text="Attacks used by this Pokémon cost Colorless less for each Kofu card in your discard pile.",
            passive=FoodPrepPassive(),
        ),
        Attack(
            title="Sonic Edge",
            game_text="This attack's damage isn't affected by any effects on your opponent's Active Pokémon.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=110,
            effect=ac.ignore_effects_attack(),
        ),
    ],
)
