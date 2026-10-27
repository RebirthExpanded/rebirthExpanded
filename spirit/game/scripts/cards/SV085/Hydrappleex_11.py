"""Hydrapple ex (SV085 11 -- JP SV7 012; English PRE/11, SCR/14, SCR/156, SCR/167). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card


def _basic_grass(card):
    return is_basic_energy_card(card) and is_energy_of_type(card, PokemonTypes.GRASS)


def _ripening_condition(board, player_id, pokemon) -> bool:
    hand = board.find_player_area(player_id, "hand")
    return bool(hand) and any(_basic_grass(c) for c in hand.children)


async def ripening_charge(ctx):
    pool = [c for c in ctx.hand() if _basic_grass(c)]
    if not pool:
        return
    picks = await ctx.choose_cards(pool, 1, minimum=1, prompt="Choose a Basic Grass Energy card to attach")
    target = await ctx.choose_pokemon(ctx.my_pokemon_in_play(), "Choose 1 of your Pokémon") if picks else None
    if target is not None and await ctx.attach_energy(picks[0], target):
        await ctx.heal(30, target)


def _grass_in_play(ctx) -> int:
    return sum(1 for p in ctx.my_pokemon_in_play() for e in ctx.attached_energies(p)
               if is_energy_of_type(e, PokemonTypes.GRASS))


card = PokemonCardDef(
    guid="0e04954e-7558-5b25-9f88-5a06afd40181",
    key="SV085",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hydrappleex.Name",
    display_name="Hydrapple ex",
    searchable_by=["Hydrapple ex", "Stage 2", "ex"],
    subtypes=["Stage 2", "ex"],
    collector_number=11,
    set_code="SV085",
    regulation_mark="H",
    rarity=Rarities.RareHoloEX,
    hp=330,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Dipplin.Name",
    family_id=840,
    abilities=[
        Ability(
            title="Ripening Charge",
            game_text="Once during your turn, you may attach a Basic Grass Energy card from your hand to 1 of your Pokémon. If you attached Energy to a Pokémon in this way, heal 30 damage from that Pokémon.",
            activation=Activations.ONCE_PER_TURN,
            condition=_ripening_condition,
            effect=ripening_charge,
        ),
        Attack(
            title="Syrup Storm",
            game_text="This attack does 30 more damage for each Grass Energy attached to all of your Pokémon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="+",
            effect=ac.damage_per(_grass_in_play, 30, base=30),
        ),
    ],
)
