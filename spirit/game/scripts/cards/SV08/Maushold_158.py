"""Maushold (SV08 158 -- JP SV8 092; English SSP/158). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su
from spirit.game.card_effects import attacks_common as ac
from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES


def _maushold(card) -> bool:
    return card.get_attribute(AttrID.EVOLUTION_LOGIC_NAME) == "Maushold"


card = PokemonCardDef(
    guid="4ffdd8bf-0715-591d-aaaa-fec9787526d9",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Maushold.Name",
    display_name="Maushold",
    searchable_by=["Maushold", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=158,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Tandemaus.Name",
    family_id=924,
    abilities=[
        Attack(
            title="Familial March",
            game_text="Search your deck for up to 2 in any combination of Maushold and Maushold ex and put them onto your Bench. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=su.search_to_bench(_maushold, count=2, prompt="Choose up to 2 Maushold or Maushold ex."),
        ),
        Attack(
            title="Incessant Incisors",
            game_text="Flip 4 coins. This attack does 30 damage for each heads.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="x",
            effect=ac.flip_damage(coins=4, per_heads=30),
        ),
    ],
)
