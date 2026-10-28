"""Doublade (SV4 132 -- JP SV3a 046; English PAR/132). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="03d2bd09-676c-55fc-8c04-a04db0828f17",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Doublade.Name",
    display_name="Doublade",
    searchable_by=["Doublade", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=132,
    set_code="SV4",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Honedge.Name",
    family_id=679,
    abilities=[
        Attack(
            title="Slash",
            game_text="",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
        Attack(
            title="Slashing Strike",
            game_text="During your next turn, this Pokémon can't use Slashing Strike.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=80,
            locks_next_turn=True,
        ),
    ],
)
