"""Victini (ZSV10PT5 12 -- JP SV11B 012; English BLK/12, BLK/171, SVP/208, WHT/172). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


def _five_benched(ctx) -> bool:
    return len(ctx.my_bench()) >= 5


card = PokemonCardDef(
    guid="47b49ea1-150b-580c-8b63-766e54f54205",
    key="ZSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Victini.Name",
    display_name="Victini",
    searchable_by=["Victini", "Basic"],
    subtypes=["Basic"],
    collector_number=12,
    set_code="ZSV10PT5",
    regulation_mark="I",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=494,
    abilities=[
        Attack(
            title="V-Force",
            game_text="If you have 4 or fewer Benched Pokémon, this attack does nothing.",
            cost={PokemonTypes.FIRE: 2},
            damage=120,
            effect=ac.bonus_if(_five_benched, 0, else_nothing=True),
        ),
    ],
)
