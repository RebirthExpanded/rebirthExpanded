"""Armarouge ex (SVP 105 -- JP SVI 011; English SVP/105). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac

from spirit.game.attributes import PokemonTypes as _PT


card = PokemonCardDef(
    guid="d02fd676-3536-53cd-b2e3-489844699c92",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Armarougeex.Name",
    display_name="Armarouge ex",
    searchable_by=["Armarouge ex", "Stage 1", "ex"],
    subtypes=["Stage 1", "ex"],
    collector_number=105,
    set_code="SVP",
    regulation_mark="H",
    rarity=Rarities.RarePromo,
    hp=260,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Charcadet.Name",
    family_id=935,
    abilities=[
        Attack(
            title="Armor Cannon",
            game_text="Discard a Fire Energy from this Pokémon.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=200,
            effect=ac.self_energy_discard_attack(count=1, energy_type=_PT.FIRE),
        ),
    ],
)
