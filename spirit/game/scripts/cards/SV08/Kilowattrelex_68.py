"""Kilowattrel ex (SV08 68 -- JP SVP 155; English SSP/68). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card


def _basic_lightning(card):
    return is_basic_energy_card(card) and is_energy_of_type(card, PokemonTypes.LIGHTNING)


async def _return_charge(ctx):
    """Switch this Pokemon with 1 of your Benched Pokemon. If you do, attach
    up to 2 Basic Lightning Energy cards from your hand to this Pokemon."""
    me = ctx.attacker
    bench = ctx.my_bench()
    if not bench:
        return
    target = await ctx.choose_pokemon(bench, "Choose your new Active Pokémon")
    if target is None or not await ctx.switch_active(ctx.player_id, target):
        return
    pool = [c for c in ctx.hand() if _basic_lightning(c)]
    if not pool:
        return
    picks = await ctx.choose_cards(pool, min(2, len(pool)), minimum=0,
                                   prompt="Attach up to 2 Basic Lightning Energy cards to this Pokémon.")
    for card in picks or []:
        await ctx.attach_energy(card, me)


card = PokemonCardDef(
    guid="87675066-8a1a-58ea-b842-70b88b7d04c6",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kilowattrelex.Name",
    display_name="Kilowattrel ex",
    searchable_by=["Kilowattrel ex", "Stage 1", "ex"],
    subtypes=["Stage 1", "ex"],
    collector_number=68,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.RareHoloEX,
    hp=260,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Wattrel.Name",
    family_id=940,
    abilities=[
        Attack(
            title="Return Charge",
            game_text="Switch this Pokémon with 1 of your Benched Pokémon. If you do, attach up to 2 Basic Lightning Energy cards from your hand to this Pokémon.",
            cost={PokemonTypes.LIGHTNING: 1},
            effect=_return_charge,
        ),
        Attack(
            title="Thunder Lance",
            game_text="This attack does 40 more damage for each Lightning Energy attached to this Pokémon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=40,
            damage_operator="+",
            effect=ac.damage_per(ac.count_energy('self', energy_type=PokemonTypes.LIGHTNING), 40, base=40),
        ),
    ],
)
