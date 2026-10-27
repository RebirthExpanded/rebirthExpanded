"""Unfezant (SV05 135 -- JP SV5M 059; English TEF/135). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


async def _hit_then_lock(ctx):
    await ctx.deal_damage()
    ac.lock_all_attacks(ctx, ctx.attacker)


async def opposing_winds(ctx):
    await ctx.deal_damage()
    target = ctx.opponent_active()
    if target is None or target in ctx.knockouts or ctx.effects_blocked(target):
        return
    pool = list(ctx.attached_energies(target))
    if pool and await ctx.ask_yes_no("Put 2 Energy attached to your opponent's Active Pokémon into their hand?"):
        n = min(2, len(pool))
        picks = await ctx.choose_cards(pool, n, minimum=n, prompt="Choose 2 Energy")
        if picks:
            await ctx.put_in_hand(picks)


card = PokemonCardDef(
    guid="e01ec4bf-ac0e-5d73-89c2-80d097df11a2",
    key="SV05",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Unfezant.Name",
    display_name="Unfezant",
    searchable_by=["Unfezant", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=135,
    set_code="SV05",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    hp=150,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Tranquill.Name",
    family_id=519,
    abilities=[
        Attack(
            title="Opposing Winds",
            game_text="You may put 2 Energy attached to your opponent's Active Pokémon into their hand.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=70,
            effect=opposing_winds,
        ),
        Attack(
            title="Boundless Power",
            game_text="During your next turn, this Pokémon can't attack.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=180,
            effect=_hit_then_lock,
        ),
    ],
)
