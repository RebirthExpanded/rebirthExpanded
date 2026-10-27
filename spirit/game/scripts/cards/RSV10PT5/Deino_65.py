"""Deino (RSV10PT5 65 -- JP SV11W 060; English WHT/146, WHT/65). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="cf86d022-ec89-5806-b109-2000059f6f3f",
    key="RSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Deino.Name",
    display_name="Deino",
    searchable_by=["Deino", "Basic"],
    subtypes=["Basic"],
    collector_number=65,
    set_code="RSV10PT5",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=633,
    abilities=[
        Attack(
            title="Body Slam",
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Paralyzed.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            effect=ac.condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
        Attack(
            title="Darkness Fang",
            game_text="",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
    ],
)
