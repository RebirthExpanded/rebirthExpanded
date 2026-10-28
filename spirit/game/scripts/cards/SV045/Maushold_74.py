"""Maushold (SV045 74 -- JP SV1V 066; English PAF/210, PAF/74, SVI/161). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES


def _mausholds(ctx) -> int:
    return sum(1 for p in ctx.my_pokemon_in_play() if p.get_attribute(AttrID.EVOLUTION_LOGIC_NAME) == "Maushold")


card = PokemonCardDef(
    guid="8cb91d56-46d4-5584-a668-8c86cbe2c102",
    key="SV045",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Maushold.Name",
    display_name="Maushold",
    searchable_by=["Maushold", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=74,
    set_code="SV045",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Tandemaus.Name",
    family_id=924,
    abilities=[
        Attack(
            title="Slap",
            game_text="",
            cost={PokemonTypes.COLORLESS: 1},
            damage=40,
        ),
        Attack(
            title="Family Attack",
            game_text="This attack does 70 damage for each of your Maushold in play.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=70,
            damage_operator="x",
            effect=ac.damage_per(_mausholds, 70),
        ),
    ],
)
