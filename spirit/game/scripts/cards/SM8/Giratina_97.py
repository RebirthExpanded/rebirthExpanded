"""Giratina (SM - Lost Thunder 97/214 -- JP SM7b 041/060).

Basic Psychic Pokemon. HP 130, weakness Darkness x2, resistance Fighting
-20, retreat 3.

  Ability  Distortion Door  Once during your turn (before your attack), if
                            this Pokemon is in your discard pile, you may
                            put it onto your Bench. If you do, put 1 damage
                            counter on 2 of your opponent's Benched Pokemon.
  Shadow Impact  [PPC] 130  Put 4 damage counters on 1 of your Pokemon.

Darkrai-GX's Restoration path: an Ability usable from the discard pile,
gated on Bench room, that Benches the card. The counters that follow go
on 2 of THEIR Benched Pokemon -- one each -- and with fewer than 2 there,
on what is there. Shadow Impact's counters land on one of your own
Pokemon, this one included.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.support_common import requires_bench_space
from spirit.game.data_utils import (Ability, Activations, Attack,
                                    PokemonCardDef)


async def distortion_door(ctx):
    if not await ctx.ask_yes_no("Put this Pokémon onto your Bench?"):
        return
    if not await ctx.bench_pokemon(ctx.source):
        return
    bench = list(ctx.opponent_bench())
    if not bench:
        return
    targets = bench if len(bench) <= 2 else await ctx.choose_cards(
        bench, 2, minimum=2,
        prompt="Choose 2 of your opponent's Benched Pokémon.")
    for target in targets:
        await ctx.deal_damage(10, target=target, as_counters=True,
                              apply_modifiers=False)


async def shadow_impact(ctx):
    await ctx.deal_damage()
    target = await ctx.choose_pokemon(
        ctx.my_pokemon_in_play(), "Choose 1 of your Pokémon to put 4 damage counters on")
    if target is not None:
        await ctx.deal_damage(40, target=target, as_counters=True,
                              apply_modifiers=False)


card = PokemonCardDef(
    guid="aaa14554-f297-5e65-83c3-19f40875fbf1",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Giratina.Name",
    display_name="Giratina",
    searchable_by=["Giratina", "Basic"],
    subtypes=["Basic"],
    collector_number=97,
    set_code="SM8",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=487,
    abilities=[
        Ability(
            title="Distortion Door",
            game_text="Once during your turn (before your attack), if this Pokémon is in your discard pile, you may put it onto your Bench. If you do, put 1 damage counter on 2 of your opponent's Benched Pokémon.",
            usable_from="discard",
            activation=Activations.ONCE_PER_TURN,
            condition=requires_bench_space(1),
            effect=distortion_door,
        ),
        Attack(
            title="Shadow Impact",
            game_text="Put 4 damage counters on 1 of your Pokémon.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
            effect=shadow_impact,
        ),
    ],
)
