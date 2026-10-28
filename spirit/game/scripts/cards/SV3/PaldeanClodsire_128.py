"""Paldean Clodsire (SV3 128 -- JP SVD 070; English OBF/128). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="105b7804-4082-5913-af17-4e45ee1684c4",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.PaldeanClodsire.Name",
    display_name="Paldean Clodsire",
    searchable_by=["Paldean Clodsire", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=128,
    set_code="SV3",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=140,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.PaldeanWooper.Name",
    family_id=194,
    abilities=[
        Attack(
            title="Poison Ring",
            game_text="Your opponent's Active Pokémon is now Poisoned. During your opponent's next turn, that Pokémon can't retreat.",
            cost={PokemonTypes.DARKNESS: 1},
            damage=20,
            effect=ac.condition_attack(SpecialConditions.POISONED, no_retreat=True),
        ),
        Attack(
            title="Muddy Hammer",
            game_text="Discard the top card of your opponent's deck.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
            effect=ac.mill_attack(1),
        ),
    ],
)
