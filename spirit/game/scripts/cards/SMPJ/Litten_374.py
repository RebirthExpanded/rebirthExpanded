"""Litten (SMPJ 374 -- JP SMP 374; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.card_effects import support_common as su

from spirit.game.session.effects import is_item_card

_find_out = ac.flip_or_nothing(then=su.search_to_hand(is_item_card, count=1, reveal=True, prompt="Choose an Item card."))


card = PokemonCardDef(
    guid="48e555bd-3766-5d05-be96-68581cfe609a",
    key="SMPJ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Litten.Name",
    display_name="Litten",
    searchable_by=["Litten", "Basic"],
    subtypes=["Basic"],
    collector_number=374,
    set_code="SMPJ",
    regulation_mark="C",
    rarity=Rarities.RarePromo,
    hp=60,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=725,
    abilities=[
        Attack(
            title="Find Out",
            game_text="Flip a coin. If heads, search your deck for an Item card, reveal it, and put it into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=_find_out,
        ),
        Attack(
            title="Flare",
            game_text="",
            cost={PokemonTypes.FIRE: 1},
            damage=10,
        ),
    ],
)
