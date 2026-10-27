"""Druddigon (RSV10PT5 71 -- JP SV11W 069; English WHT/151, WHT/71). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="042fc9ff-3d5c-57bc-8347-98ab892d4eea",
    key="RSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Druddigon.Name",
    display_name="Druddigon",
    searchable_by=["Druddigon", "Basic"],
    subtypes=["Basic"],
    collector_number=71,
    set_code="RSV10PT5",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    family_id=621,
    abilities=[
        Attack(
            title="Shred",
            game_text="This attack's damage isn't affected by any effects on your opponent's Active Pokémon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=40,
            effect=ac.ignore_effects_attack(),
        ),
        Attack(
            title="Ambush",
            game_text="Flip a coin. If heads, this attack does 60 more damage.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=90,
            damage_operator="+",
            effect=ac.flip_bonus(60),
        ),
    ],
)
