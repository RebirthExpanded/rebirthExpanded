"""Tropius (MF 1 -- JP MF 001; English 30C/5). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


def _lost_one(ctx) -> bool:
    return ctx.kos_by_attack_last_turn() > 0


card = PokemonCardDef(
    guid="9ebb80fa-229b-5edb-8043-bd70c5e1cdc3",
    key="MF",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tropius.Name",
    display_name="Tropius",
    searchable_by=["Tropius", "Basic"],
    subtypes=["Basic"],
    collector_number=1,
    set_code="MF",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=120,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    family_id=357,
    abilities=[
        Attack(
            title="Rally Back",
            game_text="If any of your Pokémon were Knocked Out by damage from an attack during your opponent's last turn, this attack does 90 more damage.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="+",
            effect=ac.bonus_if(_lost_one, 90),
        ),
        Attack(
            title="Cutting Wind",
            game_text="",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
        ),
    ],
)
