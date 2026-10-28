"""Azumarill (SV2 45 -- JP SV2P 017; English PAL/45). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su
from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="e1e68335-441a-5763-b4fe-4c544068b400",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Azumarill.Name",
    display_name="Azumarill",
    searchable_by=["Azumarill", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=45,
    set_code="SV2",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Marill.Name",
    family_id=298,
    abilities=[
        Attack(
            title="Bubble Drain",
            game_text="Heal 30 damage from this Pokémon.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=su.heal_attack(30),
        ),
        Attack(
            title="Slam",
            game_text="Flip 2 coins. This attack does 100 damage for each heads.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
            damage_operator="x",
            effect=ac.flip_damage(coins=2, per_heads=100),
        ),
    ],
)
