"""Duosion (SV05 71 -- JP SV5K 031; English TEF/71). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="75269926-1852-5d60-b29d-a54e1b085206",
    key="SV05",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Duosion.Name",
    display_name="Duosion",
    searchable_by=["Duosion", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=71,
    set_code="SV05",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Solosis.Name",
    family_id=577,
    abilities=[
        Attack(
            title="Double Trick",
            game_text="Flip 2 coins. This attack does 30 damage for each heads.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="x",
            effect=ac.flip_damage(coins=2, per_heads=30),
        ),
    ],
)
