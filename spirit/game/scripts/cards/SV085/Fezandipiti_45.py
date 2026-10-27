"""Fezandipiti (SV085 45 -- JP SV6 056; English PRE/45, SFA/73, TWM/96). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.session.passives import Passive, carrier_pokemon
from spirit.game.card_effects import attacks_common as ac
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card

import random


class AdrenaPheromonePassive(Passive):
    """Darkness Energy attached: an attack's damage is prevented on heads."""

    async def damage_interceptor(self, ctx, calc, target, carrier):
        me = carrier_pokemon(carrier)
        if not (calc.is_attack and target is me and calc.amount > 0):
            return None
        if not any(is_energy_of_type(e, PokemonTypes.DARKNESS) for e in me.children):
            return None
        results = await ctx.flip_coins(1, "Adrena-Pheromone", source=me, flipper_id=me.owning_player_id)
        return 0 if results and results[0] else None


card = PokemonCardDef(
    guid="8467cc1c-c291-5bf1-bf8b-cd14b529cdf2",
    key="SV085",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Fezandipiti.Name",
    display_name="Fezandipiti",
    searchable_by=["Fezandipiti", "Basic"],
    subtypes=["Basic"],
    collector_number=45,
    set_code="SV085",
    regulation_mark="H",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=1016,
    abilities=[
        Ability(
            title="Adrena-Pheromone",
            game_text="If this Pokémon has any Darkness Energy attached and is damaged by an attack, flip a coin. If heads, prevent that damage.",
            passive=AdrenaPheromonePassive(),
        ),
        Attack(
            title="Energy Feather",
            game_text="This attack does 30 damage for each Energy attached to this Pokémon.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=30,
            damage_operator="x",
            effect=ac.damage_per(ac.count_energy("self"), 30),
        ),
    ],
)
