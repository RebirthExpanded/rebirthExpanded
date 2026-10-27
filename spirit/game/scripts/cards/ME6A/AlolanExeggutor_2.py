"""Alolan Exeggutor (ME6A 2 -- JP M6a 002; English 30C/129, 30C/2, MEP/94). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su
from spirit.game.session.passives import Passive, carrier_pokemon
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card



class ScaleUpPassive(Passive):
    """+250 HP with 6 or more Grass Energy attached (an Ability)."""

    def max_hp_bonus(self, pokemon, carrier):
        if pokemon is not carrier:
            return 0
        from spirit.game.models.board import EnergyEntity
        grass = sum(1 for e in pokemon.children if isinstance(e, EnergyEntity) and is_energy_of_type(e, PokemonTypes.GRASS))
        return 250 if grass >= 6 else 0


card = PokemonCardDef(
    guid="69b4fe02-4b6f-5878-8af9-27826cb228eb",
    key="ME6A",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.AlolanExeggutor.Name",
    display_name="Alolan Exeggutor",
    searchable_by=["Alolan Exeggutor", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=2,
    set_code="ME6A",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=150,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Exeggcute.Name",
    family_id=102,
    abilities=[
        Ability(
            title="Scale Up",
            game_text="If this Pokémon has 6 or more Grass Energy attached, it gets +250 HP.",
            passive=ScaleUpPassive(),
        ),
        Attack(
            title="Mega Drain",
            game_text="Heal 50 damage from this Pokémon",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 3},
            damage=150,
            effect=su.heal_attack(50),
        ),
    ],
)
