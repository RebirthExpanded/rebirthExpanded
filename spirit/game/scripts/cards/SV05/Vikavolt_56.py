"""Vikavolt (SV05 56 -- JP SV5M 028; English TEF/56). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES


def _charjabugs(ctx) -> int:
    return sum(1 for p in ctx.my_bench() if p.get_attribute(AttrID.EVOLUTION_LOGIC_NAME) == "Charjabug")


card = PokemonCardDef(
    guid="21e00972-98df-53d4-a64f-28a4c104ccd9",
    key="SV05",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Vikavolt.Name",
    display_name="Vikavolt",
    searchable_by=["Vikavolt", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=56,
    set_code="SV05",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    hp=160,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Charjabug.Name",
    family_id=736,
    abilities=[
        Attack(
            title="Mach Bolt",
            game_text="",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=50,
        ),
        Attack(
            title="Circuit Cannon",
            game_text="This attack does 80 more damage for each of your Benched Charjabug.",
            cost={PokemonTypes.LIGHTNING: 2},
            damage=120,
            damage_operator="+",
            effect=ac.damage_per(_charjabugs, 80, base=120),
        ),
    ],
)
