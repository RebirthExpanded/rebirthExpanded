"""Sigilyph (RSV10PT5 38 -- JP SV11W 035; English WHT/121, WHT/38). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.card_effects import passives_common as pc


card = PokemonCardDef(
    guid="ae42f605-2ae3-5c82-a67e-cdb7974b404f",
    key="RSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sigilyph.Name",
    display_name="Sigilyph",
    searchable_by=["Sigilyph", "Basic"],
    subtypes=["Basic"],
    collector_number=38,
    set_code="RSV10PT5",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=561,
    abilities=[
        Attack(
            title="Reflect",
            game_text="During your opponent's next turn, this Pokémon takes 40 less damage from attacks (after applying Weakness and Resistance).",
            cost={PokemonTypes.COLORLESS: 1},
            effect=pc.protect_next_turn(reduce=40),
        ),
        Attack(
            title="Telekinesis",
            game_text="This attack does 70 damage to 1 of your opponent's Pokémon. This attack's damage isn't affected by Weakness or Resistance.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            effect=ac.snipe_attack(70, pool="any", apply_modifiers=False),
        ),
    ],
)
