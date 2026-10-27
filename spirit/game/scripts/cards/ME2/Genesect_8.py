"""Genesect (ME2 8 -- JP M2 008; English PFL/8). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac

from spirit.game.attributes import PokemonTypes as _PT


async def bugs_cannon(ctx):
    n = ac.count_energy("self", _PT.GRASS)(ctx)
    if n:
        await ac.snipe_attack(20 * n, pool="any")(ctx)


card = PokemonCardDef(
    guid="5b997686-b4d2-5657-a6c4-0f0098c0b5e7",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Genesect.Name",
    display_name="Genesect",
    searchable_by=["Genesect", "Basic"],
    subtypes=["Basic"],
    collector_number=8,
    set_code="ME2",
    regulation_mark="I",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    family_id=649,
    abilities=[
        Attack(
            title="Bug's Cannon",
            game_text="This attack does 20 damage to 1 of your opponent's Pokémon for each Grass Energy attached to this Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.GRASS: 1},
            effect=bugs_cannon,
        ),
        Attack(
            title="Speed Attack",
            game_text="",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=110,
        ),
    ],
)
