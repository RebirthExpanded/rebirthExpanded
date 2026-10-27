"""Pupitar (SV09 81 -- JP SV9 048; English JTG/81). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="9b9d1641-055f-5513-a39d-6013960a322a",
    key="SV09",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pupitar.Name",
    display_name="Pupitar",
    searchable_by=["Pupitar", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=81,
    set_code="SV09",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Larvitar.Name",
    family_id=246,
    abilities=[
        Attack(
            title="Take Down",
            game_text="This Pokémon also does 20 damage to itself.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=ac.recoil_attack(20),
        ),
    ],
)
