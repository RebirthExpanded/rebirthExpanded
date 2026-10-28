"""Vaporeon (SVPJ 63 -- JP SVP 063; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="4f17e885-fe5b-572f-a3fb-cbeeb16203a8",
    key="SVPJ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Vaporeon.Name",
    display_name="Vaporeon",
    searchable_by=["Vaporeon", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=63,
    set_code="SVPJ",
    regulation_mark="G",
    rarity=Rarities.RarePromo,
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    family_id=133,
    abilities=[
        Attack(
            title="Aqua Bullet",
            game_text="This attack also does 20 damage to 1 of your opponent's Benched Pokémon. (Don’t apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=90,
            effect=ac.snipe_attack(20, pool="bench", also_base=True),
        ),
    ],
)
