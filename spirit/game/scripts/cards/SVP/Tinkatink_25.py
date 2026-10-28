"""Tinkatink (SVP 25 -- JP SV2D 033; English SVP/25). Japanese art.
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
    guid="e5567305-61cd-5d4c-b7bc-fa60726ac025",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tinkatink.Name",
    display_name="Tinkatink",
    searchable_by=["Tinkatink", "Basic"],
    subtypes=["Basic"],
    collector_number=25,
    set_code="SVP",
    regulation_mark="G",
    rarity=Rarities.RarePromo,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    family_id=957,
    abilities=[
        Attack(
            title="Smithereen Smash",
            game_text="Flip a coin. If heads, discard an Energy from your opponent's Active Pokémon.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
            effect=_flip_discard_energy,
        ),
    ],
)
