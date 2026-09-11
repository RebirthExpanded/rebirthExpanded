"""Rowlet & Alolan Exeggutor-GX (SM - Unified Minds 1/236 -- JP SM10b
001/054).

Basic Grass TAG TEAM Pokemon-GX. HP 270, weakness Fire x2, retreat 3.

  Super Growth       [ ]        Search your deck for a card that evolves
                                from 1 of your [G] Pokemon and put it onto
                                that Pokemon to evolve it. If that Pokemon
                                is now a Stage 1 Pokemon, search your deck
                                for a Stage 2 Pokemon that evolves from that
                                Pokemon and put it onto that Pokemon to
                                evolve it. Then, shuffle your deck.
  Calming Hurricane  [GGC] 150  Heal 30 damage from this Pokemon.
  Tropical Hour-GX   [GGG+] 200 With at least 3 extra Energy attached, your
                                opponent shuffles all Energy from all of
                                their Pokemon into their deck.

Super Growth's first step is "a card that evolves from" the chosen Grass
Pokemon -- any such card, read by name the way every evolution path here
is: a Stage 1, but equally a VMAX or VSTAR onto a V, or a BREAK. Only the
second step is stage-bound: it fires when the Pokemon "is now a Stage 1",
and asks for a Stage 2. Both steps skip the evolution turn gates, as an
effect-driven evolution does. Nothing to evolve, and the attack does
nothing but shuffle.

The extra-Energy check is the TAG TEAM one: the [GGG] cost plus three of
anything, asked as a single question of what is attached.
"""

from spirit.game.attributes import (AttrID, PokemonStage, PokemonTypes,
                                    Rarities)
from spirit.game.card_effects.support_common import pokemon_can_still_evolve
from spirit.game.data_utils import Attack, PokemonCardDef
from spirit.game.session.effects import is_pokemon_of_type
from spirit.game.session.legal_actions import attack_cost_satisfied

# The [GGG] cost plus the three extra, asked as a single question.
_COST_PLUS_EXTRAS = {"Grass": 3, "Colorless": 3}


def _evolvable_grass(board, player_id):
    return [p for p in board.pokemon_in_play(player_id)
            if is_pokemon_of_type(p, PokemonTypes.GRASS)
            and pokemon_can_still_evolve(board, player_id, p)]


def _super_growth_condition(board, player_id, pokemon) -> bool:
    """Usable only with a Grass Pokemon that can still be evolved: one whose
    evolution cards are not all in the discard pile."""
    return bool(_evolvable_grass(board, player_id))


async def super_growth(ctx):
    """Evolve one of your Grass Pokemon, and a Stage 1 on to its Stage 2."""
    candidates = _evolvable_grass(ctx.board, ctx.player_id)
    target = None
    if candidates:
        target = await ctx.choose_pokemon(candidates, "Choose a Grass Pokémon to evolve")
    if target is None:
        await ctx.shuffle_deck()
        return
    logic_name = target.get_attribute(AttrID.EVOLUTION_LOGIC_NAME)
    picks = await ctx.search_deck(
        lambda c, name=logic_name: c.get_attribute(AttrID.EVOLUTION_LOGIC_FROM) == name,
        count=1, minimum=0,
        prompt="Choose a card that evolves from that Pokémon.")
    if not picks or not await ctx.evolve_pokemon(target, picks[0]):
        await ctx.shuffle_deck()
        return
    evolved = picks[0]
    if evolved.get_attribute(AttrID.STAGE) == PokemonStage.STAGE1.value:
        stage1_name = evolved.get_attribute(AttrID.EVOLUTION_LOGIC_NAME)
        more = await ctx.search_deck(
            lambda c, name=stage1_name: (
                c.get_attribute(AttrID.EVOLUTION_LOGIC_FROM) == name
                and c.get_attribute(AttrID.STAGE) == PokemonStage.STAGE2.value),
            count=1, minimum=0,
            prompt="Choose a Stage 2 Pokémon that evolves from that Pokémon.")
        if more:
            await ctx.evolve_pokemon(evolved, more[0])
    await ctx.shuffle_deck()


async def calming_hurricane(ctx):
    """150, then heal 30 from this Pokemon."""
    await ctx.deal_damage()
    await ctx.heal(30, ctx.attacker)


async def tropical_hour_gx(ctx):
    """200; with 3 extra Energy, every Energy they have in play goes back
    into their deck."""
    await ctx.deal_damage()
    energies = ctx.attached_energies(ctx.attacker)
    if not attack_cost_satisfied(_COST_PLUS_EXTRAS, energies, ctx.board):
        return
    cards = [e for p in ctx.opponent_pokemon_in_play()
             if not ctx.effects_blocked(p)
             for e in ctx.attached_energies(p)]
    if cards:
        await ctx.shuffle_into_deck(cards, ctx.opponent_id)


card = PokemonCardDef(
    guid="15bf5c5f-df94-5953-9b89-c3aaabfbe5bf",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RowletAlolanExeggutorGX.Name",
    display_name="Rowlet & Alolan Exeggutor-GX",
    searchable_by=["Rowlet & Alolan Exeggutor-GX", "Basic", "TAG TEAM", "GX",
                   "RowletAlolanExeggutorGX"],
    subtypes=["Basic", "TAG TEAM", "GX"],
    collector_number=1,
    set_code="SM11",
    rarity=Rarities.RareHoloGX,
    hp=270,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    family_id=722,
    abilities=[
        Attack(
            title="Super Growth",
            game_text="Search your deck for a card that evolves from 1 of your Grass Pokémon and put it onto that Pokémon to evolve it. If that Pokémon is now a Stage 1 Pokémon, search your deck for a Stage 2 Pokémon that evolves from that Pokémon and put it onto that Pokémon to evolve it. Then, shuffle your deck.",
            cost={},
            condition=_super_growth_condition,
            effect=super_growth,
        ),
        Attack(
            title="Calming Hurricane",
            game_text="Heal 30 damage from this Pokémon.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=150,
            effect=calming_hurricane,
        ),
        Attack(
            title="Tropical Hour-GX",
            game_text="If this Pokémon has at least 3 extra Energy attached to it (in addition to this attack's cost), your opponent shuffles all Energy from all of their Pokémon into their deck. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.GRASS: 3},
            damage=200,
            gx=True,
            effect=tropical_hour_gx,
        ),
    ],
)
