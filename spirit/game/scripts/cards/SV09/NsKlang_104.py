"""N's Klang (SV09 104 -- JP SV9 065; English JTG/104). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="cfa19a15-4c45-5db2-ac07-b6f09ff11a46",
    key="SV09",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.NsKlang.Name",
    display_name="N's Klang",
    searchable_by=["N's Klang", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=104,
    set_code="SV09",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.NsKlink.Name",
    family_id=599,
    abilities=[
        Attack(
            title="Spinning Gears",
            game_text="Your opponent's Active Pokémon is now Confused.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=ac.condition_attack(SpecialConditions.CONFUSED),
        ),
        Attack(
            title="Confront",
            game_text="",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
        ),
    ],
)
