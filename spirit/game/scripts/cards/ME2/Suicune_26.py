"""Suicune (ME2 26 -- JP M2 026; English PFL/26). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card


def _energy_in_play(ctx, t) -> int:
    return sum(1 for p in ctx.my_pokemon_in_play() for e in ctx.attached_energies(p) if is_energy_of_type(e, t))


def _four_water(ctx) -> bool:
    return _energy_in_play(ctx, PokemonTypes.WATER) >= 4


card = PokemonCardDef(
    guid="6411909d-709b-5d19-a859-ad69d6eb4b03",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Suicune.Name",
    display_name="Suicune",
    searchable_by=["Suicune", "Basic"],
    subtypes=["Basic"],
    collector_number=26,
    set_code="ME2",
    regulation_mark="I",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=245,
    abilities=[
        Attack(
            title="Crystal Fall",
            game_text="If you have at least 4 Water Energy in play, this attack does 90 more damage.",
            cost={PokemonTypes.WATER: 2},
            damage=30,
            damage_operator="+",
            effect=ac.bonus_if(_four_water, 90),
        ),
    ],
)
