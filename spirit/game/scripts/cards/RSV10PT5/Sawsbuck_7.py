"""Sawsbuck (RSV10PT5 7 -- JP SV11W 007; English WHT/7, WHT/92). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su


card = PokemonCardDef(
    guid="2b5da267-6800-505f-ad1b-5e87bd60f816",
    key="RSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sawsbuck.Name",
    display_name="Sawsbuck",
    searchable_by=["Sawsbuck", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=7,
    set_code="RSV10PT5",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Deerling.Name",
    family_id=585,
    abilities=[
        Attack(
            title="Push Down",
            game_text="Switch out your opponent's Active Pokémon to the Bench. (Your opponent chooses the new Active Pokémon.)",
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=su.gust_attack(opponent_chooses=True),
        ),
        Attack(
            title="Solar Beam",
            game_text="",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
        ),
    ],
)
