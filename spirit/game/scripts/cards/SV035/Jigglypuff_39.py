"""Jigglypuff (SV035 39 -- JP SV2a 039; English MEW/39, PAF/198). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su
from spirit.game.card_effects import attacks_common as ac

from spirit.game.session.effects import is_supporter_card


card = PokemonCardDef(
    guid="29e89583-5de3-522b-8fc1-935897c25785",
    key="SV035",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Jigglypuff.Name",
    display_name="Jigglypuff",
    searchable_by=["Jigglypuff", "Basic"],
    subtypes=["Basic"],
    collector_number=39,
    set_code="SV035",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=174,
    abilities=[
        Attack(
            title="Lead",
            game_text="Search your deck for a Supporter card, reveal it, and put it into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=su.search_to_hand(is_supporter_card, count=1, reveal=True, prompt="Choose a Supporter card."),
        ),
        Attack(
            title="Stompy Stomp",
            game_text="Flip 2 coins. This attack does 20 damage for each heads.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="x",
            effect=ac.flip_damage(coins=2, per_heads=20),
        ),
    ],
)
