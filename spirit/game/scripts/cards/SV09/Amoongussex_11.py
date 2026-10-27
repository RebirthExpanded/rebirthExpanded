"""Amoonguss ex (SV09 11 -- JP SVM 010; English JTG/11). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="7759bb62-f156-50c5-a9ed-f814d5cd3dbd",
    key="SV09",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Amoongussex.Name",
    display_name="Amoonguss ex",
    searchable_by=["Amoonguss ex", "Stage 1", "ex"],
    subtypes=["Stage 1", "ex"],
    collector_number=11,
    set_code="SV09",
    regulation_mark="H",
    rarity=Rarities.RareHoloEX,
    hp=260,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Foongus.Name",
    family_id=590,
    abilities=[
        Attack(
            title="Spore Ball",
            game_text="Your opponent's Active Pokémon is now Asleep.",
            cost={PokemonTypes.GRASS: 1},
            damage=30,
            effect=ac.condition_attack(SpecialConditions.ASLEEP),
        ),
        Attack(
            title="Champignon's Swing",
            game_text="Flip a coin. If heads, this attack does 80 more damage.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=100,
            damage_operator="+",
            effect=ac.flip_bonus(80),
        ),
    ],
)
