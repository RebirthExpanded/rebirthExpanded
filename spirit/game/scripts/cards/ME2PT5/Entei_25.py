"""Entei (ME2PT5 25 -- JP M2a 020; English ASC/25). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card


def _energy_in_play(ctx, t) -> int:
    return sum(1 for p in ctx.my_pokemon_in_play() for e in ctx.attached_energies(p) if is_energy_of_type(e, t))


def _four_fire(ctx) -> bool:
    return _energy_in_play(ctx, PokemonTypes.FIRE) >= 4


card = PokemonCardDef(
    guid="77573378-cff8-5554-bb66-64cee00dacd6",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Entei.Name",
    display_name="Entei",
    searchable_by=["Entei", "Basic"],
    subtypes=["Basic"],
    collector_number=25,
    set_code="ME2PT5",
    regulation_mark="I",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    family_id=244,
    abilities=[
        Attack(
            title="Flare Fall",
            game_text="If you have at least 4 Fire Energy in play, this attack does 90 more damage.",
            cost={PokemonTypes.FIRE: 2},
            damage=30,
            damage_operator="+",
            effect=ac.bonus_if(_four_fire, 90),
        ),
    ],
)
