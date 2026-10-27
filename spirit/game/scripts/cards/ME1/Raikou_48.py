"""Raikou (ME1 48 -- JP M1S 030; English MEG/48). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card


def _four_lightning(ctx) -> bool:
    return sum(1 for p in ctx.my_pokemon_in_play() for e in ctx.attached_energies(p)
               if is_energy_of_type(e, PokemonTypes.LIGHTNING)) >= 4


card = PokemonCardDef(
    guid="1c3bc25c-3457-5d97-8bf6-d5439c606b8c",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Raikou.Name",
    display_name="Raikou",
    searchable_by=["Raikou", "Basic"],
    subtypes=["Basic"],
    collector_number=48,
    set_code="ME1",
    regulation_mark="I",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=243,
    abilities=[
        Attack(
            title="Electro Fall",
            game_text="If you have at least 4 Lightning Energy in play, this attack does 90 more damage.",
            cost={PokemonTypes.LIGHTNING: 2},
            damage=30,
            damage_operator="+",
            effect=ac.bonus_if(_four_lightning, 90),
        ),
    ],
)
