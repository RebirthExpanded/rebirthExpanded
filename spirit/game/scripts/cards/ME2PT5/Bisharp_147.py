"""Bisharp (ME2PT5 147 -- JP M2a 117; English ASC/147). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su


card = PokemonCardDef(
    guid="89140fd1-17af-569e-a65a-205366e42275",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bisharp.Name",
    display_name="Bisharp",
    searchable_by=["Bisharp", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=147,
    set_code="ME2PT5",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=120,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pawniard.Name",
    family_id=624,
    abilities=[
        Attack(
            title="Rapid Draw",
            game_text="Draw 2 cards.",
            cost={PokemonTypes.METAL: 1},
            damage=50,
            effect=su.draw_attack(2),
        ),
    ],
)
