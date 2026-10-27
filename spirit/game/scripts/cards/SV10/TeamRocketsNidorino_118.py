"""Team Rocket's Nidorino (SV10 118 -- JP SV10 062; English DRI/118). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="968afc45-2087-543e-9750-bba7ed0a47f7",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsNidorino.Name",
    display_name="Team Rocket's Nidorino",
    searchable_by=["Team Rocket's Nidorino", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=118,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsNidoranMale.Name",
    family_id=32,
    abilities=[
        Attack(
            title="Hammer In",
            game_text="",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
        Attack(
            title="Horn Rend",
            game_text="If your opponent's Active Pokémon already has any damage counters on it, this attack does 60 more damage.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=60,
            damage_operator="+",
            effect=ac.bonus_if(ac.has_damage("defender"), 60),
        ),
    ],
)
