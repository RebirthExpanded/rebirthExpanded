"""Marnie's Scrafty (SV10 133 -- JP SVOM 004; English DRI/133). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="dc80a3cf-2ddb-5572-b3e3-a7a775531fe2",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MarniesScrafty.Name",
    display_name="Marnie's Scrafty",
    searchable_by=["Marnie's Scrafty", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=133,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.MarniesScraggy.Name",
    family_id=559,
    abilities=[
        Attack(
            title="Rear Kick",
            game_text="",
            cost={PokemonTypes.DARKNESS: 1},
            damage=40,
        ),
        Attack(
            title="Wild Tackle",
            game_text="This Pokémon also does 30 damage to itself.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=160,
            effect=ac.recoil_attack(30),
        ),
    ],
)
