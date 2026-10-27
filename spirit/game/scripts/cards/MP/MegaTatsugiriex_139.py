"""Mega Tatsugiri ex (MP 139 -- JP MP 139; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="192cb4b0-b502-5add-8542-5df081a0a8ae",
    key="MP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MegaTatsugiriex.Name",
    display_name="Mega Tatsugiri ex",
    searchable_by=["Mega Tatsugiri ex", "Basic", "ex", "SV_Mega"],
    subtypes=["Basic", "ex", "SV_Mega"],
    collector_number=139,
    set_code="MP",
    regulation_mark="J",
    rarity=Rarities.RarePromo,
    hp=260,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=978,
    abilities=[
        Attack(
            title="Triple Crown Head",
            game_text="Flip 3 coins. This attack does 150 damage for each heads.",
            cost={PokemonTypes.WATER: 3},
            damage=150,
            damage_operator="x",
            effect=ac.flip_damage(coins=3, per_heads=150),
        ),
    ],
)
