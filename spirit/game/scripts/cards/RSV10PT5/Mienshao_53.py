"""Mienshao (RSV10PT5 53 -- JP SV11W 050; English WHT/134, WHT/53). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

async def smash_uppercut(ctx):
    await ctx.deal_damage(ignore_resistance=True)


card = PokemonCardDef(
    guid="08737b85-ee4f-5eb2-812e-871868835027",
    key="RSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mienshao.Name",
    display_name="Mienshao",
    searchable_by=["Mienshao", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=53,
    set_code="RSV10PT5",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Mienfoo.Name",
    family_id=619,
    abilities=[
        Attack(
            title="Low Sweep",
            game_text="",
            cost={PokemonTypes.FIGHTING: 1},
            damage=40,
        ),
        Attack(
            title="Smash Uppercut",
            game_text="This attack's damage isn't affected by Resistance.",
            cost={PokemonTypes.FIGHTING: 2},
            damage=80,
            effect=smash_uppercut,
        ),
    ],
)
