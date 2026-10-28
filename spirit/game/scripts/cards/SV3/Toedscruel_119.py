"""Toedscruel (SV3 119 -- JP SVD 066; English OBF/119). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="f0191e21-06be-50db-b20b-1b12ed487559",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Toedscruel.Name",
    display_name="Toedscruel",
    searchable_by=["Toedscruel", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=119,
    set_code="SV3",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Toedscool.Name",
    family_id=948,
    abilities=[
        Attack(
            title="Beat",
            game_text="",
            cost={PokemonTypes.COLORLESS: 2},
            damage=40,
        ),
        Attack(
            title="Double Whip",
            game_text="Flip 2 coins. This attack does 100 damage for each heads.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
            damage_operator="x",
            effect=ac.flip_damage(coins=2, per_heads=100),
        ),
    ],
)
