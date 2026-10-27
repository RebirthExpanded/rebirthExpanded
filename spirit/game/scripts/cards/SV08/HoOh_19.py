"""Ho-Oh (SV08 19 -- JP SVLS 003; English SSP/19). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.data_utils import def_for, subtypes_for


def _has_sub(card, sub) -> bool:
    return card is not None and sub in (subtypes_for(card.archetype_id) or [])


def _tera_benched(ctx) -> bool:
    return any(_has_sub(p, "Tera") for p in ctx.my_bench())


card = PokemonCardDef(
    guid="05497f4f-6c0d-5e98-adb7-2764f87d91a7",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HoOh.Name",
    display_name="Ho-Oh",
    searchable_by=["Ho-Oh", "Basic"],
    subtypes=["Basic"],
    collector_number=19,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=250,
    abilities=[
        Attack(
            title="Flap",
            game_text="",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
        Attack(
            title="Shining Blaze",
            game_text="If you have any Tera Pokémon on your Bench, this attack does 100 more damage.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
            damage_operator="+",
            effect=ac.bonus_if(_tera_benched, 100),
        ),
    ],
)
