"""Pawmot (MEE 5 -- JP MEE 005; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card


def _basic_lightning(card):
    return is_basic_energy_card(card) and is_energy_of_type(card, PokemonTypes.LIGHTNING)


card = PokemonCardDef(
    guid="f5c4b9f9-1873-5c5c-9aef-8ba169c34ad8",
    key="MEE",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pawmot.Name",
    display_name="Pawmot",
    searchable_by=["Pawmot", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=5,
    set_code="MEE",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=150,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pawmo.Name",
    family_id=921,
    abilities=[
        Ability(
            title="Generating Touch",
            game_text="Once during your turn, you may use this Ability. Attach a Basic Lightning Energy card from your discard pile to 1 of your Pokémon.",
            activation=Activations.ONCE_PER_TURN,
            condition=su.requires_discard(_basic_lightning),
            effect=su.attach_from_discard(_basic_lightning, count=1, target="choice", prompt="Choose a Basic Lightning Energy card to attach."),
        ),
        Attack(
            title="Zap Punch",
            game_text="",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=100,
        ),
    ],
)
