"""Gloom (SV3 2 -- JP SV3 002; English OBF/198, OBF/2). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su


card = PokemonCardDef(
    guid="52526505-f7ab-5b84-9f4a-e0290858d070",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gloom.Name",
    display_name="Gloom",
    searchable_by=["Gloom", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=2,
    set_code="SV3",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Oddish.Name",
    family_id=43,
    abilities=[
        Attack(
            title="Inviting Scent",
            game_text="Switch in 1 of your opponent's Benched Pokémon to the Active Spot.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=su.gust_attack(),
        ),
        Attack(
            title="Leaf Step",
            game_text="",
            cost={PokemonTypes.GRASS: 1},
            damage=20,
        ),
    ],
)
