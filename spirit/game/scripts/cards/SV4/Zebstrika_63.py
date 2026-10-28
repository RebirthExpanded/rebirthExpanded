"""Zebstrika (SV4 63 -- JP SV4M 024; English PAR/63). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card


def _basic_lightning(card):
    return is_basic_energy_card(card) and is_energy_of_type(card, PokemonTypes.LIGHTNING)


async def burst_of_braying(ctx):
    n = ac.count_prizes_taken("opponent")(ctx)
    pool = [c for c in ctx.discard_pile() if _basic_lightning(c)]
    if not n or not pool:
        return
    picks = await ctx.choose_cards(pool, min(n, len(pool)), minimum=0, prompt=f"Attach up to {n} Basic Lightning Energy cards")
    for card in picks:
        target = await ctx.choose_pokemon(ctx.my_pokemon_in_play(), "Choose 1 of your Pokémon")
        if target is not None:
            await ctx.attach_energy(card, target)


card = PokemonCardDef(
    guid="5326599c-ce38-5086-8f34-c740c81c6d51",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Zebstrika.Name",
    display_name="Zebstrika",
    searchable_by=["Zebstrika", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=63,
    set_code="SV4",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Blitzle.Name",
    family_id=522,
    abilities=[
        Attack(
            title="Burst of Braying",
            game_text="Choose Basic Lightning Energy cards from your discard pile up to the number of Prize cards your opponent has taken and attach them to your Pokémon in any way you like.",
            cost={PokemonTypes.LIGHTNING: 1},
            effect=burst_of_braying,
        ),
        Attack(
            title="Thunder",
            game_text="This Pokémon also does 50 damage to itself.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=150,
            effect=ac.recoil_attack(50),
        ),
    ],
)
