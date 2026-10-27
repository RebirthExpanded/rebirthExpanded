"""Thundurus (ME6 25 -- JP M6 025; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.session.passives import Passive, carrier_pokemon
from spirit.game.data_utils import def_for, subtypes_for


_FORCES = {"Tornadus", "Thundurus", "Landorus", "Enamorus"}


class IncarnateUnityPassive(Passive):
    """With Tornadus, Thundurus, Landorus and Enamorus all in play, this
    Pokemon's attacks need no Colorless Energy (an Ability)."""

    def modify_attack_cost(self, cost, pokemon, carrier, board):
        if pokemon is not carrier:
            return cost
        names = {getattr(def_for(p.archetype_id), "display_name", None) for p in board.pokemon_in_play(carrier.owning_player_id)}
        if _FORCES <= names:
            cost = {k: v for k, v in cost.items() if k != "Colorless"}
        return cost


card = PokemonCardDef(
    guid="f1c342a6-1da3-570d-a7cc-34ea1a93dc1e",
    key="ME6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Thundurus.Name",
    display_name="Thundurus",
    searchable_by=["Thundurus", "Basic"],
    subtypes=["Basic"],
    collector_number=25,
    set_code="ME6",
    regulation_mark="J",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=642,
    abilities=[
        Ability(
            title="Incarnate Unity",
            game_text="If you have Tornadus, Thundurus, Landorus, and Enamorus in play, this Pokémon's attacks cost no Colorless Energy.",
            passive=IncarnateUnityPassive(),
        ),
        Attack(
            title="Thunder Edge",
            game_text="This attack's damage isn't affected by any effects on your opponent's Active Pokémon.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
            effect=ac.ignore_effects_attack(),
        ),
    ],
)
