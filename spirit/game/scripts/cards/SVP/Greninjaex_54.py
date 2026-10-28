"""Greninja ex (SVP 54 -- JP SVD 029; English SVP/132, SVP/54). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="944f717e-3c16-51b5-a507-7cab6325fe2a",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Greninjaex.Name",
    display_name="Greninja ex",
    searchable_by=["Greninja ex", "Stage 2", "ex"],
    subtypes=["Stage 2", "ex"],
    collector_number=54,
    set_code="SVP",
    regulation_mark="G",
    rarity=Rarities.RarePromo,
    hp=300,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Frogadier.Name",
    family_id=656,
    abilities=[
        Attack(
            title="Stealthy Shuriken",
            game_text="This attack does 40 damage to 1 of your opponent's Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.COLORLESS: 1},
            effect=ac.snipe_attack(40, pool="any"),
        ),
        Attack(
            title="Torrential Slash",
            game_text="If your opponent's Active Pokémon already has any damage counters on it, this attack does 120 more damage.",
            cost={PokemonTypes.WATER: 2},
            damage=120,
            damage_operator="+",
            effect=ac.bonus_if(ac.has_damage("defender"), 120),
        ),
    ],
)
