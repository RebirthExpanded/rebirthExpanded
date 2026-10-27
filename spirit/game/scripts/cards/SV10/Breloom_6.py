"""Breloom (SV10 6 -- JP MC 029; English DRI/6). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.card_effects import support_common as su


card = PokemonCardDef(
    guid="28d323f4-3b3e-5a17-8b14-2fa1cafed1c7",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Breloom.Name",
    display_name="Breloom",
    searchable_by=["Breloom", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=6,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=120,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Shroomish.Name",
    family_id=285,
    abilities=[
        Attack(
            title="Damage Rush",
            game_text="Flip a coin until you get tails. This attack does 50 more damage for each heads.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="+",
            effect=ac.flip_damage(until_tails=True, bonus_per_heads=50),
        ),
        Attack(
            title="Mega Drain",
            game_text="Heal 30 damage from this Pokémon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
            effect=su.heal_attack(30),
        ),
    ],
)
