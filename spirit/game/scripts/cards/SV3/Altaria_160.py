"""Altaria (SV3 160 -- JP SV3 086; English OBF/160). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="fd38f280-3c35-5503-b588-268188e59027",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Altaria.Name",
    display_name="Altaria",
    searchable_by=["Altaria", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=160,
    set_code="SV3",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Swablu.Name",
    family_id=333,
    abilities=[
        Attack(
            title="Glide",
            game_text="",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
        Attack(
            title="Soothing Lullaby",
            game_text="Your opponent's Active Pokémon is now Asleep. During Pokémon Checkup, your opponent flips 2 coins instead of 1. If either of them is tails, that Pokémon is still Asleep.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.METAL: 1},
            damage=110,
            effect=ac.condition_attack(SpecialConditions.ASLEEP, checkup_coins=2),
        ),
    ],
)
