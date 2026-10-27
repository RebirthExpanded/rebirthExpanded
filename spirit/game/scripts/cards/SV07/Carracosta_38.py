"""Carracosta (SV07 38 -- JP SV7 023; English SCR/38). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import passives_common as pc

from spirit.game.session.effects import is_evolution_pokemon


card = PokemonCardDef(
    guid="0a3eb6cc-d41b-5024-bb6b-72652331098b",
    key="SV07",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Carracosta.Name",
    display_name="Carracosta",
    searchable_by=["Carracosta", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=38,
    set_code="SV07",
    regulation_mark="H",
    rarity=Rarities.Rare,
    hp=160,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Tirtouga.Name",
    family_id=564,
    abilities=[
        Ability(
            title="Primal Knowledge",
            game_text="Attacks used by your Pokémon do 30 more damage to your opponent's Active Evolution Pokémon (before applying Weakness and Resistance).",
            passive=pc.team_damage_boost_passive(30, target_pred=is_evolution_pokemon),
        ),
        Attack(
            title="Tidal Wave",
            game_text="",
            cost={PokemonTypes.WATER: 2},
            damage=150,
        ),
    ],
)
