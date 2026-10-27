"""Delcatty (ME2PT5 166 -- JP MC 586; English ASC/166). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="299bd387-433b-5dae-a8d7-caa265d7c83f",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Delcatty.Name",
    display_name="Delcatty",
    searchable_by=["Delcatty", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=166,
    set_code="ME2PT5",
    regulation_mark="J",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Skitty.Name",
    family_id=300,
    abilities=[
        Attack(
            title="Cat Kick",
            game_text="",
            cost={PokemonTypes.COLORLESS: 1},
            damage=40,
        ),
        Attack(
            title="Energy Crush",
            game_text="This attack does 40 damage for each Energy attached to all of your opponent's Pokémon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=40,
            damage_operator="x",
            effect=ac.damage_per(ac.count_energy("opponent"), 40),
        ),
    ],
)
