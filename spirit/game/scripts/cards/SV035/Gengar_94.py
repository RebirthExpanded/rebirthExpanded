"""Gengar (SV035 94 -- JP SV2a 094; English MEW/94). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.session.effects import is_trainer_card


async def poltergeist(ctx):
    hand = list(ctx.hand(ctx.opponent_id))
    if hand:
        await ctx.reveal_hand(of_player=ctx.opponent_id, to_player=ctx.player_id)
    n = sum(1 for c in hand if is_trainer_card(c))
    if n:
        await ctx.deal_damage(50 * n)


async def hollow_dive(ctx):
    await ctx.deal_damage()
    for _ in range(3):
        bench = ctx.opponent_bench()
        if not bench:
            return
        target = await ctx.choose_pokemon(bench, "Choose 1 of your opponent's Benched Pokémon to put a damage counter on")
        if target is None:
            return
        await ctx.deal_damage(10, target=target, apply_modifiers=False, as_counters=True)


card = PokemonCardDef(
    guid="7185a3da-dc1f-5762-acfa-d2997a3c71e3",
    key="SV035",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gengar.Name",
    display_name="Gengar",
    searchable_by=["Gengar", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=94,
    set_code="SV035",
    regulation_mark="G",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Haunter.Name",
    family_id=92,
    abilities=[
        Attack(
            title="Poltergeist",
            game_text="Your opponent reveals their hand. This attack does 50 damage for each Trainer card you find there.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=50,
            damage_operator="x",
            effect=poltergeist,
        ),
        Attack(
            title="Hollow Dive",
            game_text="Put 3 damage counters on your opponent's Benched Pokémon in any way you like.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=110,
            effect=hollow_dive,
        ),
    ],
)
