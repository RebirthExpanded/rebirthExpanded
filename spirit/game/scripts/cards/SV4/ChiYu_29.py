"""Chi-Yu (SV4 29 -- JP SV4K 016; English PAR/29, SVP/57). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card


def _basic_fire(card):
    return is_basic_energy_card(card) and is_energy_of_type(card, PokemonTypes.FIRE)


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


def _lost_one(ctx) -> bool:
    return ctx.kos_by_attack_last_turn() > 0


async def flare_bringer(ctx):
    await _discard_to_one(ctx, _basic_fire, 2, "Basic Fire Energy cards")


card = PokemonCardDef(
    guid="ba03fa24-ab10-5425-b11b-844636919f8f",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ChiYu.Name",
    display_name="Chi-Yu",
    searchable_by=["Chi-Yu", "Basic"],
    subtypes=["Basic"],
    collector_number=29,
    set_code="SV4",
    regulation_mark="G",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=1004,
    abilities=[
        Attack(
            title="Flare Bringer",
            game_text="Attach up to 2 Basic Fire Energy cards from your discard pile to 1 of your Pokémon.",
            cost={PokemonTypes.FIRE: 1},
            effect=flare_bringer,
        ),
        Attack(
            title="Megafire of Envy",
            game_text="If any of your Pokémon were Knocked Out by damage from an attack during your opponent's last turn, this attack does 90 more damage.",
            cost={PokemonTypes.FIRE: 2},
            damage=50,
            damage_operator="+",
            effect=ac.bonus_if(_lost_one, 90),
        ),
    ],
)
