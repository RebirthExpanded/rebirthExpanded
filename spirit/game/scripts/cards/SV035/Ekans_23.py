"""Ekans (SV035 23 -- JP SV2a 023; English MEW/23). Japanese art.
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
    guid="2d94437a-cb63-5e0e-94af-aec58825cfdf",
    key="SV035",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ekans.Name",
    display_name="Ekans",
    searchable_by=["Ekans", "Basic"],
    subtypes=["Basic"],
    collector_number=23,
    set_code="SV035",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=23,
    abilities=[
        Attack(
            title="Acid Spray",
            game_text="Flip a coin. If heads, discard an Energy from your opponent's Active Pokémon.",
            cost={PokemonTypes.DARKNESS: 2},
            damage=30,
            effect=_flip_discard_energy,
        ),
    ],
)
