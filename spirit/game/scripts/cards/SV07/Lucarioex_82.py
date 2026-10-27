"""Lucario ex (SV07 82 -- JP SVI 032; English SCR/82). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="0dbcb541-71eb-5209-bc3b-1adff8f447c9",
    key="SV07",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lucarioex.Name",
    display_name="Lucario ex",
    searchable_by=["Lucario ex", "Stage 1", "ex"],
    subtypes=["Stage 1", "ex"],
    collector_number=82,
    set_code="SV07",
    regulation_mark="H",
    rarity=Rarities.RareHoloEX,
    hp=250,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Riolu.Name",
    family_id=447,
    abilities=[
        Attack(
            title="Low Kick",
            game_text="",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
        Attack(
            title="Aura Knuckle",
            game_text="",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
        ),
    ],
)
