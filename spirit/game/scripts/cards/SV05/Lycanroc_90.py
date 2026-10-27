"""Lycanroc (SV05 90 -- JP SVHK 009; English TEF/90). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

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


async def turbo_edge(ctx):
    await ctx.deal_damage()
    await _discard_to_bench(ctx, _basic_fighting, 2, "Attach up to 2 Basic Fighting Energy cards to your Benched Pokémon")


card = PokemonCardDef(
    guid="d5e1211b-74ff-5c02-81e5-02b0164585e9",
    key="SV05",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lycanroc.Name",
    display_name="Lycanroc",
    searchable_by=["Lycanroc", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=90,
    set_code="SV05",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Rockruff.Name",
    family_id=744,
    abilities=[
        Attack(
            title="Turbo Edge",
            game_text="Attach up to 2 Basic Fighting Energy cards from your discard pile to your Benched Pokémon in any way you like.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=turbo_edge,
        ),
    ],
)
