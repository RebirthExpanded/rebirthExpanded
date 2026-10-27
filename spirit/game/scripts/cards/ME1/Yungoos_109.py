"""Yungoos (ME1 109 -- JP M1L 055; English MEG/109). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su


card = PokemonCardDef(
    guid="f332e3f8-5bc9-5374-b547-51b890993f0e",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Yungoos.Name",
    display_name="Yungoos",
    searchable_by=["Yungoos", "Basic"],
    subtypes=["Basic"],
    collector_number=109,
    set_code="ME1",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=734,
    abilities=[
        Attack(
            title="Collect",
            game_text="Draw a card.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=su.draw_attack(1),
        ),
        Attack(
            title="Gnaw",
            game_text="",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
