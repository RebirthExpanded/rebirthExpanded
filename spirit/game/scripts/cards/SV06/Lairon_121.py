"""Lairon (SV06 121 -- JP SV6 074; English TWM/121, TWM/184). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="fbf5b25f-85fa-58af-abc1-632eb6d11532",
    key="SV06",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lairon.Name",
    display_name="Lairon",
    searchable_by=["Lairon", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=121,
    set_code="SV06",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=110,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Aron.Name",
    family_id=304,
    abilities=[
        Attack(
            title="Steel Tackle",
            game_text="This Pokémon also does 20 damage to itself.",
            cost={PokemonTypes.METAL: 1},
            damage=40,
            effect=ac.recoil_attack(20),
        ),
        Attack(
            title="Metal Claw",
            game_text="",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
        ),
    ],
)
