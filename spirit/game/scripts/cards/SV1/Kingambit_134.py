"""Kingambit (SV1 134 -- JP SV1S 058; English PAF/187, SVI/134, SVI/220). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import passives_common as pc

from spirit.game.session.effects import is_basic_pokemon_in_play


card = PokemonCardDef(
    guid="86000e18-83da-5918-87f8-03299c4fcbe0",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kingambit.Name",
    display_name="Kingambit",
    searchable_by=["Kingambit", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=134,
    set_code="SV1",
    regulation_mark="G",
    rarity=Rarities.Rare,
    hp=170,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Bisharp.Name",
    family_id=624,
    abilities=[
        Ability(
            title="Leadership",
            game_text="Your Basic Pokémon's attacks do 30 more damage to your opponent's Active Pokémon (before applying Weakness and Resistance).",
            passive=pc.team_damage_boost_passive(30, attacker_pred=is_basic_pokemon_in_play),
        ),
        Attack(
            title="Hack At",
            game_text="",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=160,
        ),
    ],
)
