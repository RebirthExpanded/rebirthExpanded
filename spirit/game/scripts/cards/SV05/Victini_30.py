"""Victini (SV05 30 -- JP SV5M 019; English TEF/30). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su
from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="1f5536e2-90e9-5dd0-9bce-fdb81c28fdeb",
    key="SV05",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Victini.Name",
    display_name="Victini",
    searchable_by=["Victini", "Basic"],
    subtypes=["Basic"],
    collector_number=30,
    set_code="SV05",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=494,
    abilities=[
        Attack(
            title="Flippity Flap",
            game_text="Shuffle your hand into your deck. Then, draw 6 cards.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=su.shuffle_hand_into_deck_draw(6),
        ),
        Attack(
            title="Singe Off",
            game_text="Discard a Special Energy from your opponent's Active Pokémon.",
            cost={PokemonTypes.FIRE: 1},
            damage=30,
            effect=ac.discard_opponent_energy_attack(1, special_only=True),
        ),
    ],
)
