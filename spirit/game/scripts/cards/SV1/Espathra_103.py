"""Espathra (SV1 103 -- JP SV1S 037; English SVI/103). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="2689b971-eae9-5ab6-8659-63d3516a4a20",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Espathra.Name",
    display_name="Espathra",
    searchable_by=["Espathra", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=103,
    set_code="SV1",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Flittle.Name",
    family_id=955,
    abilities=[
        Attack(
            title="Eye Strength",
            game_text="During your opponent's next turn, the Defending Pokémon can't retreat.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=20,
            effect=ac.condition_attack(no_retreat=True),
        ),
        Attack(
            title="Psychic",
            game_text="This attack does 50 more damage for each Energy attached to your opponent's Active Pokémon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="+",
            effect=ac.damage_per(ac.count_energy("defender"), 50, base=30),
        ),
    ],
)
