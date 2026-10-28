"""Magnemite (SV2 65 -- JP SVC 002; English PAL/65). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card


def _basic_lightning(card):
    return is_basic_energy_card(card) and is_energy_of_type(card, PokemonTypes.LIGHTNING)


async def magnetic_charge(ctx):
    bench = ctx.my_bench()
    pool = [c for c in ctx.discard_pile() if _basic_lightning(c)]
    if not bench or not pool:
        return
    target = await ctx.choose_pokemon(bench, "Choose 1 of your Benched Pokémon")
    if target is None:
        return
    picks = await ctx.choose_cards(pool, min(2, len(pool)), minimum=0, prompt="Attach up to 2 Basic Lightning Energy cards")
    for card in picks:
        await ctx.attach_energy(card, target)


card = PokemonCardDef(
    guid="b32cbeb0-1109-50c8-aa1e-95c504a45671",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Magnemite.Name",
    display_name="Magnemite",
    searchable_by=["Magnemite", "Basic"],
    subtypes=["Basic"],
    collector_number=65,
    set_code="SV2",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=81,
    abilities=[
        Attack(
            title="Magnetic Charge",
            game_text="Attach up to 2 Basic Lightning Energy cards from your discard pile to 1 of your Benched Pokémon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=magnetic_charge,
        ),
        Attack(
            title="Speed Ball",
            game_text="",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)
