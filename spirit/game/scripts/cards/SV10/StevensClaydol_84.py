"""Steven's Claydol (SV10 84 -- JP SVOD 002; English DRI/84). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="38750c66-b150-5208-baeb-5a32e964329d",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.StevensClaydol.Name",
    display_name="Steven's Claydol",
    searchable_by=["Steven's Claydol", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=84,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.StevensBaltoy.Name",
    family_id=343,
    abilities=[
        Attack(
            title="Eerie Light",
            game_text="Your opponent's Active Pokémon is now Confused.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=20,
            effect=ac.condition_attack(SpecialConditions.CONFUSED),
        ),
        Attack(
            title="Clay Blast",
            game_text="Discard all Energy from this Pokémon.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=220,
            effect=ac.self_energy_discard_attack(all_energy=True),
        ),
    ],
)
