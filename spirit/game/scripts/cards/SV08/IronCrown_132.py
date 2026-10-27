"""Iron Crown (SV08 132 -- JP SV7a 039; English SSP/132). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


def _three_benched(ctx) -> bool:
    return len(ctx.opponent_bench()) >= 3


card = PokemonCardDef(
    guid="39791b16-1317-5e5c-915d-5c5e76c1af76",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.IronCrown.Name",
    display_name="Iron Crown",
    searchable_by=["Iron Crown", "Basic", "Future"],
    subtypes=["Basic", "Future"],
    collector_number=132,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    family_id=1023,
    abilities=[
        Attack(
            title="Deleting Slash",
            game_text="If your opponent has 3 or more Benched Pokémon, this attack does 80 more damage.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            damage_operator="+",
            effect=ac.bonus_if(_three_benched, 80),
        ),
        Attack(
            title="Slicing Blade",
            game_text="",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
        ),
    ],
)
