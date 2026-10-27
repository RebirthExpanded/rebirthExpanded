"""Enamorus (ME6 34 -- JP M6 034; English Japan only). Japanese art.
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


def _defender_ex(ctx) -> bool:
    return ctx.defender is not None and "ex" in (subtypes_for(ctx.defender.archetype_id) or [])


card = PokemonCardDef(
    guid="fa91e5f1-4d3c-534c-bb05-f22be745f956",
    key="ME6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Enamorus.Name",
    display_name="Enamorus",
    searchable_by=["Enamorus", "Basic"],
    subtypes=["Basic"],
    collector_number=34,
    set_code="ME6",
    regulation_mark="J",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=905,
    abilities=[
        Ability(
            title="Incarnate Unity",
            game_text="If you have Tornadus, Thundurus, Landorus, and Enamorus in play, this Pokémon's attacks cost no Colorless Energy.",
            passive=IncarnateUnityPassive(),
        ),
        Attack(
            title="Rising Heart",
            game_text="If your opponent's Active Pokémon is a Pokémon ex, this attack does 100 more damage.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 2},
            damage=100,
            damage_operator="+",
            effect=ac.bonus_if(_defender_ex, 100),
        ),
    ],
)
