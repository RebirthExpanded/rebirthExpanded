"""N's Klink (SV09 103 -- JP SV9 064; English JTG/103). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="17f9e6df-a465-51a2-88cc-2fbada3847a8",
    key="SV09",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.NsKlink.Name",
    display_name="N's Klink",
    searchable_by=["N's Klink", "Basic"],
    subtypes=["Basic"],
    collector_number=103,
    set_code="SV09",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    family_id=599,
    abilities=[
        Attack(
            title="Double Spin",
            game_text="Flip 2 coins. This attack does 10 damage for each heads.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="x",
            effect=ac.flip_damage(coins=2, per_heads=10),
        ),
    ],
)
