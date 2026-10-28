"""Nidorino (SV035 33 -- JP SV2a 033; English MEW/33). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="0bd6b090-63c8-5b8e-92ae-475094885977",
    key="SV035",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Nidorino.Name",
    display_name="Nidorino",
    searchable_by=["Nidorino", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=33,
    set_code="SV035",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.NidoranMale.Name",
    family_id=32,
    abilities=[
        Attack(
            title="Sharp Fang",
            game_text="",
            cost={PokemonTypes.DARKNESS: 1},
            damage=30,
        ),
        Attack(
            title="Superpowered Horns",
            game_text="",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
        ),
    ],
)
