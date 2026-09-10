"""Liepard (BW - Noble Victories 91/101 -- JP BW6 042/059).

Stage 1 Darkness. HP 80, weakness Fighting x2, resistance Psychic -20,
retreat 1. Evolves from Purrloin.

  Tail Trickery  [D]    The Defending Pokemon is now Confused.
  Assist         [DCC]  Flip a coin. If heads, choose 1 of your Benched
                        Pokemon's attacks and use it as this attack.

Assist is N's Zoroark ex's Night Joker with a coin in front of it and no
"N's" filter: any of your own Benched Pokemon lends its attacks. It goes
through the shared copy path, so the copied attack keeps its own effects,
the re-entry guard stops a loop (a Benched Liepard's Assist cannot be
copied into another Assist), and a copied GX or VSTAR attack still answers
to the once-per-game checks.

Tails costs the attack and nothing else -- the flip happens before the
panel opens, so the player is not asked to choose an attack they will not
get to use.

Duplicate attacks across two Benched Pokemon are collapsed by title and
text, which is what keeps the panel readable when the Bench is full of the
same Pokemon.
"""

from spirit.game.attributes import (PokemonStage, PokemonTypes, Rarities,
                                    SpecialConditions)
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.data_utils import Attack, PokemonCardDef, def_for
from spirit.game.models.board import PokemonEntity

ASSIST = "Assist"


def _bench_attacks(ctx):
    pairs = []
    seen = set()
    for pokemon in ctx.my_bench():
        if not isinstance(pokemon, PokemonEntity):
            continue
        definition = def_for(pokemon.archetype_id)
        for ability in getattr(definition, "abilities", None) or []:
            if not isinstance(ability, Attack):
                continue
            key = (ability.title, ability.game_text)
            if key in seen:
                continue
            seen.add(key)
            pairs.append((pokemon, ability))
    return pairs


async def assist(ctx):
    """Heads: use one of your Benched Pokemon's attacks as this attack."""
    heads = await ctx.flip_coins(1, ASSIST)
    if not heads or not heads[0]:
        return
    candidates = _bench_attacks(ctx)
    if not candidates:
        return
    picked = await ctx.choose_attack_to_copy(candidates, "Choose an attack to copy")
    if picked is None:
        return
    _, chosen = picked
    await ctx.use_attack(chosen)


card = PokemonCardDef(
    guid="0b38dc86-54c9-54ca-ac7c-69fe32fc6411",
    key="BW7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Liepard.Name",
    display_name="Liepard",
    searchable_by=["Liepard", "Stage 1", "Liepard"],
    subtypes=["Stage 1"],
    collector_number=91,
    set_code="BW7",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Purrloin.Name",
    family_id=509,
    abilities=[
        Attack(
            title="Tail Trickery",
            game_text="The Defending Pokémon is now Confused.",
            cost={PokemonTypes.DARKNESS: 1},
            effect=condition_attack(SpecialConditions.CONFUSED),
        ),
        Attack(
            title=ASSIST,
            game_text="Flip a coin. If heads, choose 1 of your Benched Pokémon's attacks and use it as this attack.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            effect=assist,
        ),
    ],
)
