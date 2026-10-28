"""Ferrothorn (SV4 128 -- JP SV3a 044; English PAR/128, PAR/209). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import passives_common as pc


card = PokemonCardDef(
    guid="008d5391-503a-5e83-adf6-90e9db3b8d07",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ferrothorn.Name",
    display_name="Ferrothorn",
    searchable_by=["Ferrothorn", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=128,
    set_code="SV4",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=140,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Ferroseed.Name",
    family_id=597,
    abilities=[
        Ability(
            title="Exoskeleton",
            game_text="This Pokémon takes 30 less damage from attacks (after applying Weakness and Resistance).",
            passive=pc.takes_less_passive(30),
        ),
        Attack(
            title="Spinning Needles",
            game_text="During your next turn, this Pokémon's Spinning Needles attack does 100 more damage (before applying Weakness and Resistance).",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=pc.boost_own_next_turn(100, "Spinning Needles"),
        ),
    ],
)
