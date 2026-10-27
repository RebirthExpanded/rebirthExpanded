"""Lombre (ME2 6 -- JP M2 006; English PFL/6). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su


card = PokemonCardDef(
    guid="a7c69408-1c39-5df1-8fb3-b2f65996bb2c",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lombre.Name",
    display_name="Lombre",
    searchable_by=["Lombre", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=6,
    set_code="ME2",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Lotad.Name",
    family_id=270,
    abilities=[
        Attack(
            title="Mega Drain",
            game_text="Heal 30 damage from this Pokémon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=su.heal_attack(30),
        ),
    ],
)
