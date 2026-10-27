"""Absol (SV065 30 -- JP SV6a 030; English SFA/30). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card


def _energy_in_play(ctx, t) -> int:
    return sum(1 for p in ctx.my_pokemon_in_play() for e in ctx.attached_energies(p) if is_energy_of_type(e, t))


def _three_dark(ctx) -> bool:
    return _energy_in_play(ctx, PokemonTypes.DARKNESS) >= 3


card = PokemonCardDef(
    guid="60fd49fd-ebcc-5518-af4d-d717c9d8d2cc",
    key="SV065",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Absol.Name",
    display_name="Absol",
    searchable_by=["Absol", "Basic"],
    subtypes=["Basic"],
    collector_number=30,
    set_code="SV065",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=110,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=359,
    abilities=[
        Attack(
            title="Darkfall",
            game_text="If you have at least 3 Darkness Energy in play, this attack does 50 more damage.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="+",
            effect=ac.bonus_if(_three_dark, 50),
        ),
    ],
)
