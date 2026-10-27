"""Forretress (SV05 110 -- JP SV5M 043; English TEF/110). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="9676efec-c4fb-5fb0-8eaf-600c40348526",
    key="SV05",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Forretress.Name",
    display_name="Forretress",
    searchable_by=["Forretress", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=110,
    set_code="SV05",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pineco.Name",
    family_id=204,
    abilities=[
        Attack(
            title="Spike Cannon",
            game_text="Flip 3 coins. This attack does 30 damage for each heads.",
            cost={PokemonTypes.METAL: 1},
            damage=30,
            damage_operator="x",
            effect=ac.flip_damage(coins=3, per_heads=30),
        ),
        Attack(
            title="Steel Tackle",
            game_text="This Pokémon also does 40 damage to itself.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=130,
            effect=ac.recoil_attack(40),
        ),
    ],
)
