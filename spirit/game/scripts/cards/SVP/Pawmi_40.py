"""Pawmi (SVP 40 -- JP SVP 035; English SVP/40). Japanese art.
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
    guid="19d2c5b2-8e93-5ed6-b21c-27272defc79f",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pawmi.Name",
    display_name="Pawmi",
    searchable_by=["Pawmi", "Basic"],
    subtypes=["Basic"],
    collector_number=40,
    set_code="SVP",
    regulation_mark="G",
    rarity=Rarities.RarePromo,
    hp=50,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=921,
    abilities=[
        Attack(
            title="Static Slap",
            game_text="Flip a coin. If heads, discard an Energy from your opponent's Active Pokémon.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=_flip_discard_energy,
        ),
    ],
)
