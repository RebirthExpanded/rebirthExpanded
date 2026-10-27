"""Parasect (SV09 5 -- JP SV9 005; English JTG/5). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="07a743d9-fe9c-52fb-981c-aba3fb88f856",
    key="SV09",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Parasect.Name",
    display_name="Parasect",
    searchable_by=["Parasect", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=5,
    set_code="SV09",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=120,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Paras.Name",
    family_id=46,
    abilities=[
        Attack(
            title="Spore",
            game_text="Your opponent's Active Pokémon is now Asleep.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=ac.condition_attack(SpecialConditions.ASLEEP),
        ),
        Attack(
            title="Scissor Swing",
            game_text="Flip 2 coins. This attack does 30 more damage for each heads.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
            damage_operator="+",
            effect=ac.flip_damage(coins=2, bonus_per_heads=30),
        ),
    ],
)
