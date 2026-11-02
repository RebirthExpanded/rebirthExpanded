"""Meowth (SMPJ 375 -- JP SMP 375; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.card_effects import support_common as su

from spirit.game.session.effects import is_item_card

_find_out = ac.flip_or_nothing(then=su.search_to_hand(is_item_card, count=1, reveal=True, prompt="Choose an Item card."))


card = PokemonCardDef(
    guid="73de6f19-e96c-5902-9664-891d759e873b",
    key="SMPJ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Meowth.Name",
    display_name="Meowth",
    searchable_by=["Meowth", "Basic"],
    subtypes=["Basic"],
    collector_number=375,
    set_code="SMPJ",
    regulation_mark="C",
    rarity=Rarities.RarePromo,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=52,
    abilities=[
        Attack(
            title="Find Out",
            game_text="Flip a coin. If heads, search your deck for an Item card, reveal it, and put it into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=_find_out,
        ),
        Attack(
            title="Whimsy Tackle",
            game_text="Flip a coin. If tails, this attack does nothing.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=ac.flip_or_nothing(),
        ),
    ],
)
