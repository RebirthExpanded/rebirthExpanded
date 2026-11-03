"""Thundurus (BWPJ 320 -- JP WAK 020; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="895b45a5-3ac0-5180-844e-5aad51319120",
    key="BWPJ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Thundurus.Name",
    display_name="Thundurus",
    searchable_by=["Thundurus", "Basic"],
    subtypes=["Basic"],
    collector_number=320,
    set_code="BWPJ",
    rarity=Rarities.RarePromo,
    hp=100,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=642,
    abilities=[
        Attack(
            title="Mach Flight",
            game_text="Flip a coin. If tails, this attack does nothing.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=ac.flip_or_nothing(),
        ),
        Attack(
            title="Flash Bolt",
            game_text="During your next turn, this Pokémon can't use Flash Bolt.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
            locks_next_turn=True,
        ),
    ],
)
