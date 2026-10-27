"""Deerling (SV05 16 -- JP SV5M 008; English TEF/16, TEF/165). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac

from spirit.game.attributes import PokemonTypes as _PT


card = PokemonCardDef(
    guid="7d23c0bf-9b97-56aa-9e59-db729798ed83",
    key="SV05",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Deerling.Name",
    display_name="Deerling",
    searchable_by=["Deerling", "Basic"],
    subtypes=["Basic"],
    collector_number=16,
    set_code="SV05",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=585,
    abilities=[
        Attack(
            title="Flop",
            game_text="",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Leaf Litter Tackle",
            game_text="Discard a Grass Energy from this Pokémon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            effect=ac.self_energy_discard_attack(count=1, energy_type=_PT.GRASS),
        ),
    ],
)
