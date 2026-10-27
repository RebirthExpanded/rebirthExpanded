"""Stunfisk (RSV10PT5 35 -- JP SV11W 032; English WHT/118, WHT/35). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac

from spirit.game.attributes import PokemonTypes as _PT


def _has_fighting(ctx) -> bool:
    return ac.count_energy("self", _PT.FIGHTING)(ctx) > 0


card = PokemonCardDef(
    guid="4f4e0ab7-9da3-5383-b755-9a5171ebcce3",
    key="RSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Stunfisk.Name",
    display_name="Stunfisk",
    searchable_by=["Stunfisk", "Basic"],
    subtypes=["Basic"],
    collector_number=35,
    set_code="RSV10PT5",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=618,
    abilities=[
        Attack(
            title="Muddy Bolt",
            game_text="If this Pokémon has any Fighting Energy attached, this attack does 20 more damage.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="+",
            effect=ac.bonus_if(_has_fighting, 20),
        ),
        Attack(
            title="Flop",
            game_text="",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
    ],
)
