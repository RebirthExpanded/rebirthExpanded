"""Pikachu V (Promo_SWSH 63 -- JP SD 028; English SP/63). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="57d90273-e726-5b8b-afcb-fd56eef43fa8",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.PikachuV.Name",
    display_name="Pikachu V",
    searchable_by=["Pikachu V", "Basic", "V"],
    subtypes=["Basic", "V"],
    collector_number=63,
    set_code="Promo_SWSH",
    regulation_mark="D",
    rarity=Rarities.RareHoloV,
    hp=190,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=25,
    abilities=[
        Attack(
            title="Pika Ball",
            game_text="",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=30,
        ),
        Attack(
            title="Circle Circuit",
            game_text="This attack does 30 damage for each of your Benched Pokémon.",
            cost={PokemonTypes.LIGHTNING: 2},
            damage=30,
            damage_operator="x",
            effect=ac.damage_per(ac.count_bench("mine"), 30),
        ),
    ],
)
