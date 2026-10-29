"""Rotom V (Promo_SWSH 257 -- JP SP6 001; English SP/257). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac

from spirit.game.session.effects import is_special_energy


async def _lost_hack(ctx):
    holders = [p for p in ctx.opponent_pokemon_in_play()
               if any(is_special_energy(e) for e in ctx.attached_energies(p))]
    if not holders:
        return
    target = await ctx.choose_pokemon(holders, "Choose 1 of your opponent's Pokémon")
    if target is None or ctx.effects_blocked(target):
        return
    energies = [e for e in ctx.attached_energies(target) if is_special_energy(e)]
    picks = await ctx.choose_cards(energies, 1, prompt="Choose a Special Energy to put in the Lost Zone")
    if picks:
        await ctx.move_to_lost_zone(picks)


card = PokemonCardDef(
    guid="c195b576-7182-5727-952c-bb476c6143bc",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RotomV.Name",
    display_name="Rotom V",
    searchable_by=["Rotom V", "Basic", "V"],
    subtypes=["Basic", "V"],
    collector_number=257,
    set_code="Promo_SWSH",
    regulation_mark="F",
    rarity=Rarities.RareHoloV,
    hp=190,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=479,
    abilities=[
        Attack(
            title="Lost Hack",
            game_text="Put a Special Energy attached to 1 of your opponent's Pokémon in the Lost Zone.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=_lost_hack,
        ),
        Attack(
            title="Extreme Current",
            game_text="Discard an Energy from this Pokémon.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=160,
            effect=ac.self_energy_discard_attack(1),
        ),
    ],
)
