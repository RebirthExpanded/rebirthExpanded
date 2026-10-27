"""Cynthia's Milotic (SV10 53 -- JP SV9a 029; English DRI/53). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="4252b6d6-41e4-5b01-b6a8-96c5a6b2e4fb",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.CynthiasMilotic.Name",
    display_name="Cynthia's Milotic",
    searchable_by=["Cynthia's Milotic", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=53,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.CynthiasFeebas.Name",
    family_id=349,
    abilities=[
        Attack(
            title="Aqua Split",
            game_text="This attack also does 30 damage to 2 of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
            effect=ac.snipe_attack(30, pool="bench", count=2, also_base=True),
        ),
    ],
)
