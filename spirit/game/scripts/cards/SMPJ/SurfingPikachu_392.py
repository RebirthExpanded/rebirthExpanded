"""Surfing Pikachu (SMPJ 392 -- JP SMP 392; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import passives_common as pc


card = PokemonCardDef(
    guid="8de9654d-1ebb-58ee-b65d-61c2d0e5e8b8",
    key="SMPJ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.SurfingPikachu.Name",
    display_name="Surfing Pikachu",
    searchable_by=["Surfing Pikachu", "Basic"],
    subtypes=["Basic"],
    collector_number=392,
    set_code="SMPJ",
    regulation_mark="C",
    rarity=Rarities.RarePromo,
    hp=60,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=172,
    abilities=[
        Attack(
            title="Static Shock",
            game_text="",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=10,
        ),
        Attack(
            title="Summer Waves",
            game_text="Flip a coin. If heads, prevent all effects of attacks, including damage, done to this Pokémon during your opponent's next turn.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=30,
            effect=pc.flip_protection(prevent=True, effects_too=True),
        ),
    ],
)
