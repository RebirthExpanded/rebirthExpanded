"""Archen (RSV10PT5 50 -- JP SV11W 047; English WHT/131, WHT/50). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="337d643f-cc5c-512f-9e1d-e0c5d98bb899",
    key="RSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Archen.Name",
    display_name="Archen",
    searchable_by=["Archen", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=50,
    set_code="RSV10PT5",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.trainer.AntiquePlumeFossil.Name",
    family_id=566,
    abilities=[
        Attack(
            title="Acrobatics",
            game_text="Flip 2 coins. This attack does 30 more damage for each heads.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="+",
            effect=ac.flip_damage(coins=2, bonus_per_heads=30),
        ),
    ],
)
