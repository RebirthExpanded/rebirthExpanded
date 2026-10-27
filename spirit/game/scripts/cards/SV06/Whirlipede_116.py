"""Whirlipede (SV06 116 -- JP SV6 069; English TWM/116). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="c0350768-782b-5778-8b7c-0d2625ce1354",
    key="SV06",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Whirlipede.Name",
    display_name="Whirlipede",
    searchable_by=["Whirlipede", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=116,
    set_code="SV06",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Venipede.Name",
    family_id=543,
    abilities=[
        Attack(
            title="Poison Ring",
            game_text="Your opponent's Active Pokémon is now Poisoned. During your opponent's next turn, the Defending Pokémon can't retreat.",
            cost={PokemonTypes.DARKNESS: 1},
            effect=ac.condition_attack(SpecialConditions.POISONED, no_retreat=True),
        ),
        Attack(
            title="Spinning Attack",
            game_text="",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
        ),
    ],
)
