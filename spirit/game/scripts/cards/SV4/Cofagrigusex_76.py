"""Cofagrigus ex (SV4 76 -- JP SV4K 031; English PAR/224, PAR/76). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

def _ko_by_opponent(ctx) -> bool:
    attacker = getattr(ctx, "ko_attacker", None)
    return (bool(getattr(ctx, "ko_from_attack", False)) and attacker is not None
            and attacker.owning_player_id != ctx.source.owning_player_id)


async def gold_coffin(ctx):
    picks = await ctx.search_deck(count=1, minimum=0, prompt="Choose a card to put into your hand.")
    if picks:
        await ctx.put_in_hand(picks, reveal=False)
    await ctx.shuffle_deck()


async def hollow_hands(ctx):
    await ctx.deal_damage()
    for _ in range(5):
        bench = ctx.opponent_bench()
        if not bench:
            return
        target = await ctx.choose_pokemon(bench, "Choose 1 of your opponent's Benched Pokémon to put a damage counter on")
        if target is None:
            return
        await ctx.deal_damage(10, target=target, apply_modifiers=False, as_counters=True)


card = PokemonCardDef(
    guid="787eb1b0-9cb5-5fcf-83c2-93acf14bc6d9",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cofagrigusex.Name",
    display_name="Cofagrigus ex",
    searchable_by=["Cofagrigus ex", "Stage 1", "ex"],
    subtypes=["Stage 1", "ex"],
    collector_number=76,
    set_code="SV4",
    regulation_mark="G",
    rarity=Rarities.RareHoloEX,
    hp=260,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Yamask.Name",
    family_id=562,
    abilities=[
        Ability(
            title="Gold Coffin",
            game_text="If this Pokémon is Knocked Out by damage from an attack from your opponent's Pokémon, search your deck for a card and put it into your hand. Then, shuffle your deck.",
            trigger=Triggers.ON_KNOCKED_OUT,
            trigger_applies=_ko_by_opponent,
            effect=gold_coffin,
        ),
        Attack(
            title="Hollow Hands",
            game_text="Put 5 damage counters on your opponent's Benched Pokémon in any way you like.",
            cost={PokemonTypes.PSYCHIC: 2},
            damage=110,
            effect=hollow_hands,
        ),
    ],
)
