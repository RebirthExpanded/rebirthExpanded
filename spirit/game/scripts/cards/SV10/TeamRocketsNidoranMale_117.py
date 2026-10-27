"""Team Rocket's Nidoran♂ (SV10 117 -- JP MC 435; English DRI/117). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="0d306346-9aca-508c-b306-65d0d9a94bf2",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsNidoranMale.Name",
    display_name="Team Rocket's Nidoran♂",
    searchable_by=["Team Rocket's Nidoran♂", "Basic"],
    subtypes=["Basic"],
    collector_number=117,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=32,
    abilities=[
        Attack(
            title="Pierce",
            game_text="",
            cost={PokemonTypes.DARKNESS: 1},
            damage=10,
        ),
        Attack(
            title="Hammer In",
            game_text="",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)
