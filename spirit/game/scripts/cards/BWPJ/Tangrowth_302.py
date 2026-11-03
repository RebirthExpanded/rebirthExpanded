"""Tangrowth (BWPJ 302 -- JP WAK 002; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su


card = PokemonCardDef(
    guid="38642ee4-6dce-53fb-981d-d72eac64a878",
    key="BWPJ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tangrowth.Name",
    display_name="Tangrowth",
    searchable_by=["Tangrowth", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=302,
    set_code="BWPJ",
    rarity=Rarities.RarePromo,
    hp=100,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Tangela.Name",
    family_id=114,
    abilities=[
        Attack(
            title="Mega Drain",
            game_text="Heal 20 damage from this Pokémon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=su.heal_attack(20),
        ),
        Attack(
            title="Vine Whip",
            game_text="",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 3},
            damage=60,
        ),
    ],
)
