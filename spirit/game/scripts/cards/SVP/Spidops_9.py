"""Spidops (SVP 9 -- JP SVP 002; English SVP/9). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="3c2cf7c6-31e3-5db3-af53-9f85c1651b12",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Spidops.Name",
    display_name="Spidops",
    searchable_by=["Spidops", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=9,
    set_code="SVP",
    regulation_mark="G",
    rarity=Rarities.RarePromo,
    hp=120,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Tarountula.Name",
    family_id=917,
    abilities=[
        Attack(
            title="String Truss",
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Paralyzed.",
            cost={PokemonTypes.GRASS: 1},
            damage=30,
            effect=ac.condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
        Attack(
            title="Jet Headbutt",
            game_text="",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
        ),
    ],
)
