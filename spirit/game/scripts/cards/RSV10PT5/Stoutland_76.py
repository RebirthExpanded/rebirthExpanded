"""Stoutland (RSV10PT5 76 -- JP SV11W 074; English WHT/156, WHT/76). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac

from spirit.game.session.effects import is_special_energy


async def odor_sleuth(ctx):
    heads = sum(1 for r in await ctx.flip_coins(3, "Odor Sleuth") if r)
    discard = list(ctx.discard_pile())
    if not heads or not discard:
        return
    picks = await ctx.choose_cards(discard, min(heads, len(discard)), minimum=0,
                                   prompt=f"Choose up to {heads} cards from your discard pile")
    if picks:
        await ctx.put_in_hand(picks, reveal=False)


def _has_special_energy(ctx) -> bool:
    return any(is_special_energy(e) for e in ctx.attached_energies(ctx.attacker))


card = PokemonCardDef(
    guid="787085a0-73ae-58e7-839a-5607e7291e67",
    key="RSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Stoutland.Name",
    display_name="Stoutland",
    searchable_by=["Stoutland", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=76,
    set_code="RSV10PT5",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=160,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Herdier.Name",
    family_id=506,
    abilities=[
        Attack(
            title="Odor Sleuth",
            game_text="Flip 3 coins. Put a number of cards up to the number of heads from your discard pile into your hand.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=odor_sleuth,
        ),
        Attack(
            title="Special Fang",
            game_text="If this Pokémon has any Special Energy attached, this attack does 100 more damage.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=100,
            damage_operator="+",
            effect=ac.bonus_if(_has_special_energy, 100),
        ),
    ],
)
