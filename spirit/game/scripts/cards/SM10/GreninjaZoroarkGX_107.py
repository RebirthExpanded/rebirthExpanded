"""Greninja & Zoroark-GX (SM - Unbroken Bonds 107/214 -- JP SM9a 025/055,
the art here).

Basic Darkness TAG TEAM Pokemon-GX. HP 250, weakness Fighting x2,
resistance Psychic -20, retreat 2. When Knocked Out, the opponent takes 3
Prize cards.

  Dark Pulse       [DC] 30+  This attack does 30 more damage for each [D]
                             Energy attached to all of your Pokemon.
  Night Unison-GX  [DC]+     Put 2 [D] Pokemon-GX or Pokemon-EX from your
                             discard pile onto your Bench. If this Pokemon
                             has at least 1 extra Energy attached to it (in
                             addition to this attack's cost), attach 2
                             Energy cards from your discard pile to each of
                             those Pokemon. (You can't use more than 1 GX
                             attack in a game.)

Dark Pulse counts [D] Energy as provided (a Double Turbo pays none); the
Energy cards Night Unison-GX attaches are any Energy cards in the discard
pile, up to 2 per Pokemon put down. "Pokemon-EX" is the XY-era uppercase
EX, not the SV "ex".
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import count_energy, damage_per
from spirit.game.card_effects.pokemon import is_energy_card
from spirit.game.data_utils import Attack, PokemonCardDef, def_for, subtypes_for
from spirit.game.session.effects import is_pokemon_card, is_pokemon_of_type
from spirit.game.session.legal_actions import attack_cost_satisfied

_COST_PLUS_EXTRA = {"Darkness": 1, "Colorless": 2}


def _dark_gx_or_ex(card) -> bool:
    return (is_pokemon_card(card) and is_pokemon_of_type(card, PokemonTypes.DARKNESS)
            and any(s in ("GX", "EX") for s in subtypes_for(card.archetype_id)))


async def night_unison_gx(ctx):
    candidates = [c for c in ctx.discard_pile() if _dark_gx_or_ex(c)]
    if not candidates:
        return
    room = ctx.bench_space()
    picks = await ctx.choose_cards(
        candidates, min(2, room), minimum=0,
        prompt="Choose up to 2 [D] Pokémon-GX or Pokémon-EX to put onto your Bench.")
    benched = []
    for card in picks:
        if await ctx.bench_pokemon(card):
            benched.append(card)
    if not benched:
        return
    energies = ctx.attached_energies(ctx.attacker)
    if not attack_cost_satisfied(_COST_PLUS_EXTRA, energies, ctx.board):
        return
    for pokemon in benched:
        pool = [c for c in ctx.discard_pile() if is_energy_card(c)]
        if not pool:
            return
        chosen = await ctx.choose_cards(
            pool, 2, minimum=0,
            prompt=f"Choose up to 2 Energy cards to attach to {def_for(pokemon.archetype_id).display_name}.")
        for energy in chosen:
            await ctx.attach_energy(energy, pokemon)


card = PokemonCardDef(
    guid="a3adc521-c93a-533c-944f-7968c033b887",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GreninjaZoroarkGX.Name",
    display_name="Greninja & Zoroark-GX",
    searchable_by=["Greninja & Zoroark-GX", "Basic", "TAG TEAM", "GX", "GreninjaZoroarkGX"],
    subtypes=["Basic", "TAG TEAM", "GX"],
    collector_number=107,
    set_code="SM10",
    rarity=Rarities.RareUltra,
    hp=250,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=658,
    abilities=[
        Attack(
            title="Dark Pulse",
            game_text="This attack does 30 more damage for each [D] Energy attached to all of your Pokémon.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="+",
            effect=damage_per(count_energy("mine", PokemonTypes.DARKNESS), 30, base=30),
        ),
        Attack(
            title="Night Unison-GX",
            game_text="Put 2 [D] Pokémon-GX or Pokémon-EX from your discard pile onto your Bench. If this Pokémon has at least 1 extra Energy attached to it (in addition to this attack's cost), attach 2 Energy cards from your discard pile to each of those Pokémon. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            gx=True,
            effect=night_unison_gx,
        ),
    ],
)
