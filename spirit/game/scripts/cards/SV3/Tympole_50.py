"""Tympole (SV3 50 -- JP SV3 023; English OBF/50). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

async def _flip_discard_energy(ctx):
    await ctx.deal_damage()
    results = await ctx.flip_coins(1, ctx.ability.title if ctx.ability else "")
    target = ctx.opponent_active()
    if results and results[0] and target is not None and not ctx.effects_blocked(target) \
            and ctx.attached_energies(target):
        await ctx.discard_energy_from(target, 1, minimum=1,
                                      prompt="Choose an Energy to discard from your opponent's Active Pokémon")


card = PokemonCardDef(
    guid="706582ba-4548-5baf-a8bd-1bd8820f81ac",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tympole.Name",
    display_name="Tympole",
    searchable_by=["Tympole", "Basic"],
    subtypes=["Basic"],
    collector_number=50,
    set_code="SV3",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=535,
    abilities=[
        Attack(
            title="Screw Tail",
            game_text="Flip a coin. If heads, discard an Energy from your opponent's Active Pokémon.",
            cost={PokemonTypes.WATER: 1},
            damage=10,
            effect=_flip_discard_energy,
        ),
    ],
)
