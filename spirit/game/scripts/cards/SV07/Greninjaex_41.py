"""Greninja ex (SV07 41 -- JP SVI 017; English SCR/41). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="a62419a1-e151-5a00-be19-82d72a48181d",
    key="SV07",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Greninjaex.Name",
    display_name="Greninja ex",
    searchable_by=["Greninja ex", "Stage 2", "ex"],
    subtypes=["Stage 2", "ex"],
    collector_number=41,
    set_code="SV07",
    regulation_mark="H",
    rarity=Rarities.RareHoloEX,
    hp=300,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Frogadier.Name",
    family_id=656,
    abilities=[
        Attack(
            title="Shifting Shuriken",
            game_text="Flip a coin. If heads, this attack does 100 more damage.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=100,
            damage_operator="+",
            effect=ac.flip_bonus(100),
        ),
    ],
)
