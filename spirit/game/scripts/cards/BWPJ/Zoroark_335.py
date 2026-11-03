"""Zoroark (BWPJ 335 -- JP WAK 035; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="9239632a-380c-552c-8170-ffdbad103404",
    key="BWPJ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Zoroark.Name",
    display_name="Zoroark",
    searchable_by=["Zoroark", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=335,
    set_code="BWPJ",
    rarity=Rarities.RarePromo,
    hp=100,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Zorua.Name",
    family_id=570,
    abilities=[
        Attack(
            title="Scratch",
            game_text="",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
        Attack(
            title="Cross Blow",
            game_text="Flip 4 coins. This attack does 30 damage for each heads.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="x",
            effect=ac.flip_damage(coins=4, per_heads=30),
        ),
    ],
)
