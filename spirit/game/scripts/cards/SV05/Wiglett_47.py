"""Wiglett (SV05 47 -- JP SV5K 021; English TEF/47). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su
from spirit.game.card_effects import attacks_common as ac

from spirit.game.session.effects import is_item_card


card = PokemonCardDef(
    guid="f7f76856-fb97-5825-8ea3-a9bba0198603",
    key="SV05",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Wiglett.Name",
    display_name="Wiglett",
    searchable_by=["Wiglett", "Basic"],
    subtypes=["Basic"],
    collector_number=47,
    set_code="SV05",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=960,
    abilities=[
        Attack(
            title="Lucky Find",
            game_text="Search your deck for an Item card, reveal it, and put it into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.WATER: 1},
            effect=su.search_to_hand(is_item_card, count=1, reveal=True, prompt="Choose an Item card."),
        ),
        Attack(
            title="Aqua Bomb",
            game_text="This Pokémon also does 20 damage to itself.",
            cost={PokemonTypes.WATER: 2},
            damage=40,
            effect=ac.recoil_attack(20),
        ),
    ],
)
