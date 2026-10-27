"""Zweilous (RSV10PT5 66 -- JP SV11W 061; English WHT/147, WHT/66). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="778cdad8-0674-5795-bc55-ebc5c0532ded",
    key="RSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Zweilous.Name",
    display_name="Zweilous",
    searchable_by=["Zweilous", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=66,
    set_code="RSV10PT5",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=110,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Deino.Name",
    family_id=633,
    abilities=[
        Attack(
            title="Double Hit",
            game_text="Flip 2 coins. This attack does 40 damage for each heads.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=40,
            damage_operator="x",
            effect=ac.flip_damage(coins=2, per_heads=40),
        ),
        Attack(
            title="Pitch-Black Fangs",
            game_text="",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 2},
            damage=100,
        ),
    ],
)
