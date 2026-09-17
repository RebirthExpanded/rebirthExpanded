"""Alolan Raichu (SM - Unified Minds 57/236 -- JP SM10a 010/054).

Stage 1 Lightning. HP 110, weakness Fighting x2, resistance Metal -20,
retreat 1. Evolves from Pikachu.

  Electro Rain    [L]     Discard any amount of Lightning Energy from this
                          Pokemon. Then, for each Energy you discarded in
                          this way, choose 1 of your opponent's Pokemon and
                          do 30 damage to it. (You can choose the same
                          Pokemon more than once.) This damage isn't
                          affected by Weakness or Resistance.
  Electric Ball  [LCC] 90

Electro Rain is a free-aim spread: the player picks the Energy, then aims
each discarded Energy separately, and the same target may be chosen again.
The picks are tallied first and each Pokemon is dealt its total in one hit
rather than 30 at a time, so an aimed 60 kills a 60 HP Pokemon in one blow
and a shield that reads a single hit reads it once (Q&A: three picks on
one Pokemon-GX with a Choice Band is 120, not 3 x 60).

"Lightning Energy" is read live off the board, not off the card's printed
type: a Rainbow Energy on this Pokemon is a [L] Energy and may be
discarded (Q&A), a Unit Energy LPM likewise. And the aims go by the
number of [L] the discarded cards PROVIDED, not by the number of cards --
Counter Energy providing two is two picks (Q&A).

"Isn't affected by Weakness or Resistance" is the printed ignore on both,
and the damage goes wherever it is aimed -- the opponent's Active included,
which is why this is deal_damage per target rather than the Bench-only
snipe factory.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.pokemon import energy_units_of_type
from spirit.game.data_utils import Attack, PokemonCardDef

PER_ENERGY = 30


async def electro_rain(ctx):
    """Discard any amount of [L] (live reading: Rainbow counts), then aim
    30 per [L] the discarded cards provided, repeats allowed."""
    attacker = ctx.attacker
    if attacker is None:
        return
    lightning = [e for e in ctx.board.attached_energies(attacker)
                 if energy_units_of_type(ctx.board, e, PokemonTypes.LIGHTNING.value) > 0]
    if not lightning:
        return
    picks = await ctx.choose_cards(
        lightning, len(lightning), minimum=0,
        prompt="Choose any amount of Lightning Energy to discard.",
    )
    if not picks:
        return
    # Count the [L] provided while the cards are still attached: Rainbow
    # provides [L] only on a Pokemon, and a doubling reads the board.
    aims = sum(energy_units_of_type(ctx.board, e, PokemonTypes.LIGHTNING.value)
               for e in picks)
    await ctx.discard_cards(picks)
    targets = ctx.opponent_pokemon_in_play()
    if not targets or aims <= 0:
        return
    tally = {}
    for n in range(aims):
        chosen = await ctx.choose_pokemon(
            targets, f"Choose 1 of your opponent's Pokémon to damage ({n + 1}/{aims}).")
        if chosen is None:
            chosen = targets[0]
        tally[chosen.entity_id] = tally.get(chosen.entity_id, 0) + 1
    for target in targets:
        hits = tally.get(target.entity_id, 0)
        if hits:
            await ctx.deal_damage(PER_ENERGY * hits, target=target,
                                  ignore_weakness=True, ignore_resistance=True)


card = PokemonCardDef(
    guid="3139be3a-a07b-588f-8ae0-4600c48ef112",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.AlolanRaichu.Name",
    display_name="Alolan Raichu",
    searchable_by=["Alolan Raichu", "Stage 1", "AlolanRaichu"],
    subtypes=["Stage 1"],
    collector_number=57,
    set_code="SM11",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pikachu.Name",
    family_id=25,
    abilities=[
        Attack(
            title="Electro Rain",
            game_text="Discard any amount of Lightning Energy from this Pokémon. Then, for each Energy you discarded in this way, choose 1 of your opponent's Pokémon and do 30 damage to it. (You can choose the same Pokémon more than once.) This damage isn't affected by Weakness or Resistance.",
            cost={PokemonTypes.LIGHTNING: 1},
            effect=electro_rain,
        ),
        Attack(
            title="Electric Ball",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
        ),
    ],
)
