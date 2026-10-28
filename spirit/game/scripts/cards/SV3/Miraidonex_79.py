"""Miraidon ex (SV3 79 -- JP SVD 046; English OBF/79, SVP/143). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card


def _basic_lightning(card):
    return is_basic_energy_card(card) and is_energy_of_type(card, PokemonTypes.LIGHTNING)


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


async def techno_turbo(ctx):
    await ctx.deal_damage()
    await _discard_to_bench(ctx, _basic_lightning, 1, "Attach a Basic Lightning Energy card to 1 of your Benched Pokémon")


card = PokemonCardDef(
    guid="a81d9959-e5df-5426-b20b-9bb336e5d6ac",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Miraidonex.Name",
    display_name="Miraidon ex",
    searchable_by=["Miraidon ex", "Basic", "ex"],
    subtypes=["Basic", "ex"],
    collector_number=79,
    set_code="SV3",
    regulation_mark="G",
    rarity=Rarities.RareHoloEX,
    hp=220,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=1008,
    abilities=[
        Attack(
            title="Rapid Draw",
            game_text="Draw 2 cards.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=20,
            effect=su.draw_attack(2),
        ),
        Attack(
            title="Techno Turbo",
            game_text="Attach a Basic Lightning Energy card from your discard pile to 1 of your Benched Pokémon.",
            cost={PokemonTypes.LIGHTNING: 3},
            damage=150,
            effect=techno_turbo,
        ),
    ],
)
