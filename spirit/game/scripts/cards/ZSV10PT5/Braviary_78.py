"""Braviary (ZSV10PT5 78 -- JP SV11W 077; English BLK/155, BLK/78). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="b7eff5da-909e-5ee3-a81d-389e80cc1492",
    key="ZSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Braviary.Name",
    display_name="Braviary",
    searchable_by=["Braviary", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=78,
    set_code="ZSV10PT5",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=140,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Rufflet.Name",
    family_id=627,
    abilities=[
        Attack(
            title="Aerial Ace",
            game_text="Flip a coin. If heads, this attack does 40 more damage.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=40,
            damage_operator="+",
            effect=ac.flip_bonus(40),
        ),
        Attack(
            title="Speed Wing",
            game_text="",
            cost={PokemonTypes.COLORLESS: 4},
            damage=130,
        ),
    ],
)
