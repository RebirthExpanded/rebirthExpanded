"""Sandy Shocks ex (SV085 56 -- JP SV4K 042; English PAR/108, PAR/228, PAR/250, PRE/159, PRE/56). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


async def _hit_then_lock(ctx):
    await ctx.deal_damage()
    ac.lock_all_attacks(ctx, ctx.attacker)
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card


def _basic_fighting(card):
    return is_basic_energy_card(card) and is_energy_of_type(card, PokemonTypes.FIGHTING)


def _absorb_condition(board, player_id, pokemon) -> bool:
    other = next((pid for pid in board.player_ids if pid != player_id), None)
    prizes = board.find_player_area(other, "prizePile") if other else None
    discard = board.find_player_area(player_id, "discard")
    return (prizes is not None and len(prizes.children) <= 4 and bool(discard)
            and any(_basic_fighting(c) for c in discard.children))


async def magnetic_absorption(ctx):
    pool = [c for c in ctx.discard_pile() if _basic_fighting(c)]
    if pool:
        picks = await ctx.choose_cards(pool, 1, minimum=1, prompt="Choose a Basic Fighting Energy card to attach")
        if picks:
            await ctx.attach_energy(picks[0], ctx.source)


card = PokemonCardDef(
    guid="0a2b58d6-9be9-55ae-b811-9d04d447e227",
    key="SV085",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.SandyShocksex.Name",
    display_name="Sandy Shocks ex",
    searchable_by=["Sandy Shocks ex", "Basic", "ex", "Ancient"],
    subtypes=["Basic", "ex", "Ancient"],
    collector_number=56,
    set_code="SV085",
    regulation_mark="G",
    rarity=Rarities.RareHoloEX,
    hp=220,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=0,
    abilities=[
        Ability(
            title="Magnetic Absorption",
            game_text="Once during your turn, if your opponent has 4 or fewer Prize cards remaining, you may attach a Basic Fighting Energy card from your discard pile to this Pokémon.",
            activation=Activations.ONCE_PER_TURN,
            condition=_absorb_condition,
            effect=magnetic_absorption,
        ),
        Attack(
            title="Earthen Spike",
            game_text="During your next turn, this Pokémon can't attack.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=200,
            effect=_hit_then_lock,
        ),
    ],
)
