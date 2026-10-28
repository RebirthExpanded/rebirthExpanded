"""Tinkaton ex (SVP 31 -- JP SV2D 035; English PAL/240, PAL/262, SVP/31). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="44b6c20b-085d-517a-bfed-8bac35e04e99",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tinkatonex.Name",
    display_name="Tinkaton ex",
    searchable_by=["Tinkaton ex", "Stage 2", "ex"],
    subtypes=["Stage 2", "ex"],
    collector_number=31,
    set_code="SVP",
    regulation_mark="G",
    rarity=Rarities.RarePromo,
    hp=300,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Tinkatuff.Name",
    family_id=957,
    abilities=[
        Attack(
            title="Big Hammer",
            game_text="This attack does 30 damage for each card in your hand.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="x",
            effect=ac.damage_per(ac.count_hand("mine"), 30),
        ),
        Attack(
            title="Pulverizing Press",
            game_text="This attack's damage isn't affected by any effects on your opponent's Active Pokémon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=140,
            effect=ac.ignore_effects_attack(),
        ),
    ],
)
