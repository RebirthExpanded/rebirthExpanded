"""Golurk (ZSV10PT5 43 -- JP SV11B 046; English BLK/123, BLK/43). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="660950ce-82b9-5ac8-aca2-3d6a638daafe",
    key="ZSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Golurk.Name",
    display_name="Golurk",
    searchable_by=["Golurk", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=43,
    set_code="ZSV10PT5",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=160,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Golett.Name",
    family_id=622,
    abilities=[
        Attack(
            title="Double Smash",
            game_text="Flip 2 coins. This attack does 80 damage for each heads.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=80,
            damage_operator="x",
            effect=ac.flip_damage(coins=2, per_heads=80),
        ),
        Attack(
            title="Golurk Hammer",
            game_text="",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 3},
            damage=200,
        ),
    ],
)
