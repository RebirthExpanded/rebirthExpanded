"""Umbreon ex (MF 17 -- JP MF 017; English 30C/92). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="c018e473-80fd-51ae-9ae5-d3056b81a0f5",
    key="MF",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Umbreonex.Name",
    display_name="Umbreon ex",
    searchable_by=["Umbreon ex", "Stage 1", "ex"],
    subtypes=["Stage 1", "ex"],
    collector_number=17,
    set_code="MF",
    regulation_mark="J",
    rarity=Rarities.RareHoloEX,
    hp=270,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    family_id=133,
    abilities=[
        Attack(
            title="Lunatic Claw",
            game_text="If your opponent's Active Pokémon already has any damage counters on it, this attack does 140 more damage.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=100,
            damage_operator="+",
            effect=ac.bonus_if(ac.has_damage("defender"), 140),
        ),
    ],
)
