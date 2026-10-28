"""Arcanine (SV035 59 -- JP SV2a 059; English MEW/59). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su
from spirit.game.card_effects import attacks_common as ac
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card


def _basic_fire(card):
    return is_basic_energy_card(card) and is_energy_of_type(card, PokemonTypes.FIRE)

from spirit.game.attributes import PokemonTypes as _PT


async def torrid_torrent(ctx):
    await ctx.deal_damage()
    pool = [c for c in ctx.discard_pile() if _basic_fire(c)]
    if pool and ctx.attacker not in ctx.knockouts:
        picks = await ctx.choose_cards(pool, min(2, len(pool)), minimum=0, prompt="Attach up to 2 Basic Fire Energy cards")
        for card in picks:
            await ctx.attach_energy(card, ctx.attacker)


card = PokemonCardDef(
    guid="2cfda5e7-0d3f-5ea0-922d-422d5ed911b0",
    key="SV035",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Arcanine.Name",
    display_name="Arcanine",
    searchable_by=["Arcanine", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=59,
    set_code="SV035",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=150,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Growlithe.Name",
    family_id=58,
    abilities=[
        Attack(
            title="Torrid Torrent",
            game_text="Attach up to 2 Basic Fire Energy cards from your discard pile to this Pokémon.",
            cost={PokemonTypes.FIRE: 1},
            damage=30,
            effect=torrid_torrent,
        ),
        Attack(
            title="Dynamite Fang",
            game_text="Discard 2 Fire Energy from this Pokémon.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 2},
            damage=240,
            effect=ac.self_energy_discard_attack(count=2, energy_type=_PT.FIRE),
        ),
    ],
)
