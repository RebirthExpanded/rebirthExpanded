"""Monferno (SV06 32 -- JP SV5a 016; English TWM/32). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="ce08e481-18d9-5fed-82c6-10790be60949",
    key="SV06",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Monferno.Name",
    display_name="Monferno",
    searchable_by=["Monferno", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=32,
    set_code="SV06",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Chimchar.Name",
    family_id=390,
    abilities=[
        Attack(
            title="Chop",
            game_text="",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
        ),
        Attack(
            title="Heat Blow",
            game_text="Discard an Energy from this Pokémon.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
            effect=ac.self_energy_discard_attack(count=1),
        ),
    ],
)
