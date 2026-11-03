"""Rayquaza (XYPJ 232 -- JP XYP 232; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.card_effects import passives_common as pc

_fly = ac.flip_or_nothing(then=pc.protect_next_turn(prevent=True, effects_too=True))


card = PokemonCardDef(
    guid="3f9ffb87-6bb5-5fa3-be2c-f3ebe226511a",
    key="XYPJ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Rayquaza.Name",
    display_name="Rayquaza",
    searchable_by=["Rayquaza", "Basic"],
    subtypes=["Basic"],
    collector_number=232,
    set_code="XYPJ",
    rarity=Rarities.RarePromo,
    hp=120,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FAIRY,
    family_id=384,
    abilities=[
        Attack(
            title="Fly",
            game_text="Flip a coin. If tails, this attack does nothing. If heads, during your opponent's next turn, prevent all damage from and effects of attacks done to this Pokémon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=_fly,
        ),
        Attack(
            title="Spiral Rush",
            game_text="Flip a coin until you get tails. This attack does 20 more damage for each heads.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=90,
            damage_operator="+",
            effect=ac.flip_damage(until_tails=True, bonus_per_heads=20),
        ),
    ],
)
