"""Zoroark-GX (SM - Shining Legends 53/73 -- JP SM3+ 054/072).

Stage 1 Darkness Pokemon-GX. HP 210, weakness Fighting x2, resistance
Psychic -20, retreat 2. Evolves from Zorua.

  Ability  Trade  Once during your turn (before your attack), you may
                  discard a card from your hand. If you do, draw 2 cards.

  Riotous Beating  [CC] 20x  This attack does 20 damage for each of your
                             Pokemon in play.
  Trickster-GX     [DD]      Choose 1 of your opponent's Pokemon's attacks
                             and use it as this attack.

Trade is a cost first and a draw second, which is the whole of the
"if you do": with an empty hand there is nothing to discard, so the
Ability is not offered at all. It counts as a discard from hand, so
anything watching for that (Amoonguss's Surprise Spores) sees it.

Trickster-GX reaches EVERY Pokemon the opponent has in play, not just the
Active, and uses the chosen attack as this attack -- the copy path Team
Rocket's Mimikyu and Regidrago VSTAR already use, which carries the
re-entry guard (a copied Trickster-GX fizzles rather than looping) and the
GX-once-per-game check that the copied attack would otherwise dodge. Its
own Energy cost is what was paid; the copied attack's is not required.

The pool's first Shining Legends card, so SM35 is registered here.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import count_in_play, damage_per
from spirit.game.card_effects.support_common import requires_hand
from spirit.game.data_utils import (Ability, Activations, Attack,
                                    PokemonCardDef, def_for)

PER_POKEMON = 20


async def trade(ctx):
    """Discard a card from hand; if you do, draw 2."""
    discarded = await ctx.discard_from_hand(
        1, prompt="Choose a card to discard for Trade")
    if not discarded:
        return
    await ctx.draw_cards(2)


async def trickster_gx(ctx):
    """Use one of their Pokemon's attacks as this attack."""
    candidates = [
        (pokemon, ability)
        for pokemon in ctx.opponent_pokemon_in_play()
        for ability in (getattr(def_for(pokemon.archetype_id), "abilities", None) or [])
        if isinstance(ability, Attack)
    ]
    if not candidates:
        return
    picked = await ctx.choose_attack_to_copy(
        candidates, "Choose an attack to copy")
    if picked is None:
        return
    _, chosen = picked
    await ctx.use_attack(chosen)


card = PokemonCardDef(
    guid="48c9db7c-898d-5d4e-aad5-2aa81a0fb4fc",
    key="SM35",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ZoroarkGX.Name",
    display_name="Zoroark-GX",
    searchable_by=["Zoroark-GX", "Stage 1", "GX", "ZoroarkGX"],
    subtypes=["Stage 1", "GX"],
    collector_number=53,
    set_code="SM35",
    rarity=Rarities.RareHoloGX,
    hp=210,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Zorua.Name",
    family_id=570,
    abilities=[
        Ability(
            title="Trade",
            game_text="Once during your turn (before your attack), you may discard a card from your hand. If you do, draw 2 cards.",
            activation=Activations.ONCE_PER_TURN,
            condition=requires_hand(n=1),
            effect=trade,
        ),
        Attack(
            title="Riotous Beating",
            game_text="This attack does 20 damage for each of your Pokémon in play.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=damage_per(count_in_play("mine"), PER_POKEMON),
        ),
        Attack(
            title="Trickster-GX",
            game_text="Choose 1 of your opponent's Pokémon's attacks and use it as this attack. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.DARKNESS: 2},
            gx=True,
            effect=trickster_gx,
        ),
    ],
)
