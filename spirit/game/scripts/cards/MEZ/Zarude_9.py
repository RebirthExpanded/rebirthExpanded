"""Zarude (MEZ 9 -- JP MEZ 009; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="2fc3cfc4-c5e1-5b19-ae5c-7f045a814d10",
    key="MEZ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Zarude.Name",
    display_name="Zarude",
    searchable_by=["Zarude", "Basic"],
    subtypes=["Basic"],
    collector_number=9,
    set_code="MEZ",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=130,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=893,
    abilities=[
        Attack(
            title="Smack",
            game_text="",
            cost={PokemonTypes.DARKNESS: 1},
            damage=20,
        ),
        Attack(
            title="Finishing Whip",
            game_text="Flip 2 coins. If both of them are heads, this attack does 150 more damage.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            damage_operator="+",
            effect=ac.flip_bonus(150, coins=2),
        ),
    ],
)
