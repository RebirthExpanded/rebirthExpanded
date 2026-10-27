"""Sableye (SV05 107 -- JP SV5K 050; English TEF/107). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

async def damage_collection(ctx):
    active = ctx.opponent_active()
    bench = ctx.opponent_bench()
    if active is None or not bench:
        return
    await ctx.move_damage_counters_freely(bench, [active])


card = PokemonCardDef(
    guid="bae88dd7-6bf7-50b5-a7fb-e20961249599",
    key="SV05",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sableye.Name",
    display_name="Sableye",
    searchable_by=["Sableye", "Basic"],
    subtypes=["Basic"],
    collector_number=107,
    set_code="SV05",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=302,
    abilities=[
        Attack(
            title="Claw Slash",
            game_text="",
            cost={PokemonTypes.DARKNESS: 1},
            damage=20,
        ),
        Attack(
            title="Damage Collection",
            game_text="You may move any number of damage counters from your opponent's Benched Pokémon to their Active Pokémon.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=damage_collection,
        ),
    ],
)
