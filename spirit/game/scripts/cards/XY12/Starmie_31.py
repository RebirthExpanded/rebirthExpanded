"""Starmie (XY - Evolutions 31/108 -- JP CP6 029/087).

Stage 1 Water Pokemon, evolves from Staryu. HP 90, weakness Grass x2,
retreat 1.

  Ability  Space Beacon  Once during your turn (before your attack), you
                         may discard a card from your hand. If you do, put
                         2 basic Energy cards from your discard pile into
                         your hand. (You can't choose a card you discarded
                         with the effect of this Ability.)
  Star Freeze  [WC] 30  Flip a coin. If heads, your opponent's Active
                        Pokemon is now Paralyzed.
"""

from spirit.game.attributes import (PokemonStage, PokemonTypes, Rarities,
                                    SpecialConditions)
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.support_common import requires_hand
from spirit.game.data_utils import (Ability, Activations, Attack,
                                    PokemonCardDef)
from spirit.game.session.effects import is_basic_energy


async def space_beacon(ctx):
    paid = await ctx.discard_from_hand(1, prompt="Discard a card for Space Beacon")
    if not paid:
        return
    energies = [c for c in ctx.discard_pile()
                if is_basic_energy(c) and c not in paid]
    if not energies:
        return
    picks = await ctx.choose_cards(
        energies, 2, minimum=min(2, len(energies)),
        prompt="Choose 2 basic Energy cards to put into your hand")
    if picks:
        await ctx.put_in_hand(picks, reveal=True)


card = PokemonCardDef(
    guid="b222ecc5-9e69-5801-b62b-51d385474ec4",
    key="XY12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Starmie.Name",
    display_name="Starmie",
    searchable_by=["Starmie", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=31,
    set_code="XY12",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Staryu.Name",
    family_id=120,
    abilities=[
        Ability(
            title="Space Beacon",
            game_text="Once during your turn (before your attack), you may discard a card from your hand. If you do, put 2 basic Energy cards from your discard pile into your hand. (You can't choose a card you discarded with the effect of this Ability.)",
            activation=Activations.ONCE_PER_TURN,
            condition=requires_hand(None, 1),
            effect=space_beacon,
        ),
        Attack(
            title="Star Freeze",
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Paralyzed.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
    ],
)
