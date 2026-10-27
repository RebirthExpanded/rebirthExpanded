"""N's Klinklang (SV09 105 -- JP SV9 066; English JTG/105). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="dcc11739-7af3-553c-8d7d-1f00be072270",
    key="SV09",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.NsKlinklang.Name",
    display_name="N's Klinklang",
    searchable_by=["N's Klinklang", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=105,
    set_code="SV09",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=160,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.NsKlang.Name",
    family_id=599,
    abilities=[
        Attack(
            title="Magnetic Blast",
            game_text="",
            cost={PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
        Attack(
            title="Triple Smash",
            game_text="Flip 3 coins. This attack does 120 damage for each heads.",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            damage_operator="x",
            effect=ac.flip_damage(coins=3, per_heads=120),
        ),
    ],
)
