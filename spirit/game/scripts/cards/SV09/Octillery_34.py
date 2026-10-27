"""Octillery (SV09 34 -- JP SV9 020; English JTG/34). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


async def aqua_wash(ctx):
    await ctx.deal_damage()
    target = ctx.opponent_active()
    if target is None or target in ctx.knockouts or ctx.effects_blocked(target) or not ctx.attached_energies(target):
        return
    if await ctx.ask_yes_no("Put an Energy attached to your opponent's Active Pokémon into their hand?"):
        picks = await ctx.choose_cards(ctx.attached_energies(target), 1, minimum=1, prompt="Choose an Energy")
        if picks:
            await ctx.put_in_hand(picks)


card = PokemonCardDef(
    guid="2e8f549f-ec2b-5022-8e3c-0eeab08341f8",
    key="SV09",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Octillery.Name",
    display_name="Octillery",
    searchable_by=["Octillery", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=34,
    set_code="SV09",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Remoraid.Name",
    family_id=223,
    abilities=[
        Attack(
            title="Aqua Wash",
            game_text="You may put an Energy attached to your opponent's Active Pokémon into their hand.",
            cost={PokemonTypes.WATER: 1},
            damage=20,
            effect=aqua_wash,
        ),
        Attack(
            title="Octo Beatdown",
            game_text="Flip a coin until you get tails. This attack does 90 damage for each heads.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
            damage_operator="x",
            effect=ac.flip_damage(until_tails=True, per_heads=90),
        ),
    ],
)
