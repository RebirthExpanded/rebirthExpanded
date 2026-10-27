"""Mawile (ME3 32 -- JP M3 031; English POR/32). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac

from spirit.game.session.effects import is_energy_card


card = PokemonCardDef(
    guid="39216229-47af-5bc7-afc2-521fb9a2b6ae",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mawile.Name",
    display_name="Mawile",
    searchable_by=["Mawile", "Basic"],
    subtypes=["Basic"],
    collector_number=32,
    set_code="ME3",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=110,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    family_id=303,
    abilities=[
        Attack(
            title="Double Eater",
            game_text="Discard up to 2 Energy cards from your hand, and this attack does 60 damage for each card you discarded in this way.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
            damage_operator="x",
            effect=ac.discard_for_bonus("hand", predicate=is_energy_card, max_count=2, per=60, base=0, prompt="Discard up to 2 Energy cards from your hand."),
        ),
    ],
)
