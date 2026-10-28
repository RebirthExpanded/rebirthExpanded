"""Garchomp ex (SV4 38 -- JP SV3a 006; English PAR/219, PAR/245, PAR/260, PAR/38). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers
from spirit.game.card_effects.pokemon import TeraRulePassive

from spirit.game.card_effects import attacks_common as ac
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card


def _basic_fighting(card):
    return is_basic_energy_card(card) and is_energy_of_type(card, PokemonTypes.FIGHTING)


async def _discard_to_bench(ctx, pred, upto, prompt):
    bench = ctx.my_bench()
    pool = [c for c in ctx.discard_pile() if pred(c)]
    if not bench or not pool:
        return
    picks = await ctx.choose_cards(pool, min(upto, len(pool)), minimum=0, prompt=prompt)
    for card in picks:
        target = await ctx.choose_pokemon(bench, "Choose a Benched Pokémon to attach the Energy to")
        if target is not None:
            await ctx.attach_energy(card, target)


async def hydro_lander(ctx):
    await ctx.deal_damage()
    await _discard_to_bench(ctx, _basic_fighting, 3, "Attach up to 3 Basic Fighting Energy cards to your Benched Pokémon")


async def sonic_dive(ctx):
    pool = list(ctx.attached_energies(ctx.attacker))
    if len(pool) < 2:
        return
    picks = await ctx.choose_cards(pool, 2, minimum=2, prompt="Choose 2 Energy to discard from this Pokémon")
    await ctx.discard_cards(picks)
    await ac.snipe_attack(120, pool="any")(ctx)


card = PokemonCardDef(
    guid="140f1046-96d4-5a4c-af94-468c59c907db",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Garchompex.Name",
    display_name="Garchomp ex",
    searchable_by=["Garchomp ex", "Stage 2", "ex", "Tera"],
    subtypes=["Stage 2", "ex", "Tera"],
    collector_number=38,
    set_code="SV4",
    regulation_mark="G",
    rarity=Rarities.RareHoloEX,
    hp=320,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Gabite.Name",
    family_id=443,
    passive=TeraRulePassive(),
    abilities=[
        Attack(
            title="Hydro Lander",
            game_text="Attach up to 3 Basic Fighting Energy cards from your discard pile to your Benched Pokémon in any way you like.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=160,
            effect=hydro_lander,
        ),
        Attack(
            title="Sonic Dive",
            game_text="Discard 2 Energy from this Pokémon. This attack does 120 damage to 1 of your opponent's Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.COLORLESS: 2},
            effect=sonic_dive,
        ),
    ],
)
