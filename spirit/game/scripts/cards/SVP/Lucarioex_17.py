"""Lucario ex (SVP 17 -- JP SVAM 009; English SVP/17). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="82fa3e72-37c1-5e07-b9d4-a0bcb1d34522",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lucarioex.Name",
    display_name="Lucario ex",
    searchable_by=["Lucario ex", "Stage 1", "ex"],
    subtypes=["Stage 1", "ex"],
    collector_number=17,
    set_code="SVP",
    regulation_mark="G",
    rarity=Rarities.RarePromo,
    hp=260,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Riolu.Name",
    family_id=447,
    abilities=[
        Attack(
            title="Low Sweep",
            game_text="",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
        ),
        Attack(
            title="Aura Sphere",
            game_text="This attack also does 50 damage to 1 of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=160,
            effect=ac.snipe_attack(50, pool="bench", also_base=True),
        ),
    ],
)
