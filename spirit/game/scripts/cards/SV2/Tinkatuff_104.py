"""Tinkatuff (SV2 104 -- JP SV2D 034; English PAF/166, PAL/104, PAL/217). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="e0affc15-24b2-5651-a317-6322f6aac467",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tinkatuff.Name",
    display_name="Tinkatuff",
    searchable_by=["Tinkatuff", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=104,
    set_code="SV2",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Tinkatink.Name",
    family_id=957,
    abilities=[
        Attack(
            title="Play Rough",
            game_text="Flip a coin. If heads, this attack does 30 more damage.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="+",
            effect=ac.flip_bonus(30),
        ),
        Attack(
            title="Pulverizing Press",
            game_text="This attack's damage isn't affected by any effects on your opponent's Active Pokémon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=ac.ignore_effects_attack(),
        ),
    ],
)
