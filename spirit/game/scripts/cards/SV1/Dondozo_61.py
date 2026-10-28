"""Dondozo (SV1 61 -- JP SV1S 021; English PAF/126, SVI/207, SVI/61). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES


def _tatsugiri(ctx) -> int:
    return sum(1 for c in ctx.discard_pile() if c.get_attribute(AttrID.EVOLUTION_LOGIC_NAME) == "Tatsugiri")


card = PokemonCardDef(
    guid="35d0adfc-0e10-5133-b877-c31255cec4c0",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dondozo.Name",
    display_name="Dondozo",
    searchable_by=["Dondozo", "Basic"],
    subtypes=["Basic"],
    collector_number=61,
    set_code="SV1",
    regulation_mark="G",
    rarity=Rarities.Rare,
    hp=160,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=977,
    abilities=[
        Attack(
            title="Release Rage",
            game_text="This attack does 50 damage for each Tatsugiri in your discard pile.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator="x",
            effect=ac.damage_per(_tatsugiri, 50),
        ),
        Attack(
            title="Heavy Splash",
            game_text="",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 2},
            damage=120,
        ),
    ],
)
