"""Mienfoo (SV4 96 -- JP SV4K 033; English PAR/96). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="2e57ac25-daaf-5820-b14a-f0d67b1d4272",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mienfoo.Name",
    display_name="Mienfoo",
    searchable_by=["Mienfoo", "Basic"],
    subtypes=["Basic"],
    collector_number=96,
    set_code="SV4",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=619,
    abilities=[
        Attack(
            title="Low Kick",
            game_text="",
            cost={PokemonTypes.FIGHTING: 1},
            damage=10,
        ),
        Attack(
            title="Beatdown",
            game_text="",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
