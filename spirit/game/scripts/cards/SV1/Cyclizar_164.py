"""Cyclizar (SV1 164 -- JP SV1V 068; English SVI/164). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su


card = PokemonCardDef(
    guid="8df00ca9-e43a-58b9-9751-fc5f1128953d",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cyclizar.Name",
    display_name="Cyclizar",
    searchable_by=["Cyclizar", "Basic"],
    subtypes=["Basic"],
    collector_number=164,
    set_code="SV1",
    regulation_mark="G",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=967,
    abilities=[
        Attack(
            title="Touring",
            game_text="Draw 2 cards.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=su.draw_attack(2),
        ),
        Attack(
            title="Speed Attack",
            game_text="",
            cost={PokemonTypes.COLORLESS: 3},
            damage=100,
        ),
    ],
)
