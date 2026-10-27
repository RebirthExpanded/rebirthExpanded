"""Cranidos (ME5 44 -- JP M5 042; English PBL/44). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su


card = PokemonCardDef(
    guid="83fc7b65-9a7e-5ea9-9bbd-451e77d93795",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cranidos.Name",
    display_name="Cranidos",
    searchable_by=["Cranidos", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=44,
    set_code="ME5",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.trainer.AntiqueSkullFossil.Name",
    family_id=408,
    abilities=[
        Attack(
            title="Push Down",
            game_text="Switch out your opponent's Active Pokémon to the Bench. (Your opponent chooses the new Active Pokémon.)",
            cost={PokemonTypes.FIGHTING: 2},
            damage=70,
            effect=su.gust_attack(opponent_chooses=True),
        ),
    ],
)
