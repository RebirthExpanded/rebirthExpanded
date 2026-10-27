"""Luxray (ME3 28 -- JP M3 027; English POR/28). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="90e915df-a94f-5da8-b650-04348cece59f",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Luxray.Name",
    display_name="Luxray",
    searchable_by=["Luxray", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=28,
    set_code="ME3",
    regulation_mark="J",
    rarity=Rarities.Rare,
    hp=150,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Luxio.Name",
    family_id=403,
    abilities=[
        Attack(
            title="Incessant Onslaught",
            game_text="This attack does 70 damage for each Prize card you have taken.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=70,
            damage_operator="x",
            effect=ac.damage_per(ac.count_prizes_taken("mine"), 70),
        ),
        Attack(
            title="Strong Volt",
            game_text="Discard 2 Energy from this Pokémon.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=200,
            effect=ac.self_energy_discard_attack(count=2),
        ),
    ],
)
