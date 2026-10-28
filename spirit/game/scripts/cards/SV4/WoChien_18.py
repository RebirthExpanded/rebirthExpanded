"""Wo-Chien (SV4 18 -- JP SV4M 009; English PAR/18). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import passives_common as pc
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card


def _basic_grass(card):
    return is_basic_energy_card(card) and is_energy_of_type(card, PokemonTypes.GRASS)


async def _discard_to_one(ctx, pred, upto, label):
    pool = [c for c in ctx.discard_pile() if pred(c)]
    if not pool:
        return
    target = await ctx.choose_pokemon(ctx.my_pokemon_in_play(), "Choose 1 of your Pokémon")
    if target is None:
        return
    picks = await ctx.choose_cards(pool, min(upto, len(pool)), minimum=0, prompt=f"Attach up to {upto} {label}")
    for card in picks:
        await ctx.attach_energy(card, target)


async def leaf_bringer(ctx):
    await _discard_to_one(ctx, _basic_grass, 2, "Basic Grass Energy cards")


async def binding_greed(ctx):
    await ctx.deal_damage()
    await pc.apply_defender_attack_cost_raise(ctx, 2)


card = PokemonCardDef(
    guid="c53a9490-7ae3-50d0-ab77-ddfb786d6db6",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.WoChien.Name",
    display_name="Wo-Chien",
    searchable_by=["Wo-Chien", "Basic"],
    subtypes=["Basic"],
    collector_number=18,
    set_code="SV4",
    regulation_mark="G",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    family_id=1001,
    abilities=[
        Attack(
            title="Leaf Bringer",
            game_text="Attach up to 2 Basic Grass Energy cards from your discard pile to 1 of your Pokémon.",
            cost={PokemonTypes.GRASS: 1},
            effect=leaf_bringer,
        ),
        Attack(
            title="Binding Greed",
            game_text="During your opponent's next turn, attacks used by the Defending Pokémon cost ColorlessColorless more.",
            cost={PokemonTypes.GRASS: 3, PokemonTypes.COLORLESS: 1},
            damage=140,
            effect=binding_greed,
        ),
    ],
)
