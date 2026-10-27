"""Cinccino (ZSV10PT5 76 -- JP SV11B 078; English BLK/153, BLK/76). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="5b57206e-6d44-5651-aaa5-c501278ae502",
    key="ZSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cinccino.Name",
    display_name="Cinccino",
    searchable_by=["Cinccino", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=76,
    set_code="ZSV10PT5",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Minccino.Name",
    family_id=572,
    abilities=[
        Attack(
            title="Do the Wave",
            game_text="This attack does 20 more damage for each of your Benched Pokémon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="+",
            effect=ac.damage_per(ac.count_bench("mine"), 20, base=20),
        ),
    ],
)
