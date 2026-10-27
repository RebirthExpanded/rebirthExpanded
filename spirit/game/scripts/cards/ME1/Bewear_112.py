"""Bewear (ME1 112 -- JP M1S 056; English MEG/112). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="95cad2c5-59bb-5a9b-98e8-b889ab976715",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bewear.Name",
    display_name="Bewear",
    searchable_by=["Bewear", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=112,
    set_code="ME1",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=130,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Stufful.Name",
    family_id=759,
    abilities=[
        Attack(
            title="Knuckle Punch",
            game_text="",
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
        Attack(
            title="Hyper Lariat",
            game_text="Flip 2 coins. If both of them are heads, this attack does 100 more damage.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=100,
            damage_operator="+",
            effect=ac.flip_damage(coins=2, bonus=100, require_all=True),
        ),
    ],
)
