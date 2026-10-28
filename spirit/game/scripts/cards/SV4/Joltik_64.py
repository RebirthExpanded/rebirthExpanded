"""Joltik (SV4 64 -- JP SV3a 016; English PAR/196, PAR/64). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="f4887f35-e3b5-519a-b55c-e11a32f87a21",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Joltik.Name",
    display_name="Joltik",
    searchable_by=["Joltik", "Basic"],
    subtypes=["Basic"],
    collector_number=64,
    set_code="SV4",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=595,
    abilities=[
        Attack(
            title="Flail Around",
            game_text="Flip 3 coins. This attack does 10 damage for each heads.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=10,
            damage_operator="x",
            effect=ac.flip_damage(coins=3, per_heads=10),
        ),
    ],
)
