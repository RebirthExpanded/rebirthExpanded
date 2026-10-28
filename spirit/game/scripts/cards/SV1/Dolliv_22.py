"""Dolliv (SV1 22 -- JP SV1S 007; English PAF/103, SVI/200, SVI/22). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="d1e7824d-d918-5c89-9ee4-92ab548ebe17",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dolliv.Name",
    display_name="Dolliv",
    searchable_by=["Dolliv", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=22,
    set_code="SV1",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Smoliv.Name",
    family_id=928,
    abilities=[
        Attack(
            title="Slap",
            game_text="",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
        Attack(
            title="Apply Oil",
            game_text="During your opponent's next turn, if the Defending Pokémon tries to attack, your opponent flips a coin. If tails, that attack doesn't happen.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            effect=ac.smokescreen_attack(),
        ),
    ],
)
