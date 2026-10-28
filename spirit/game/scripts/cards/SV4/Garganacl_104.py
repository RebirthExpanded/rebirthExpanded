"""Garganacl (SV4 104 -- JP SV4K 040; English PAR/104, PAR/202). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card


def _basic_fighting(card):
    return is_basic_energy_card(card) and is_energy_of_type(card, PokemonTypes.FIGHTING)


def _salt_condition(board, player_id, pokemon) -> bool:
    discard = board.find_player_area(player_id, "discard")
    return bool(discard) and any(_basic_fighting(c) for c in discard.children)


async def energizing_rock_salt(ctx):
    pool = [c for c in ctx.discard_pile() if _basic_fighting(c)]
    if not pool:
        return
    picks = await ctx.choose_cards(pool, 1, minimum=1, prompt="Choose a Basic Fighting Energy card to attach")
    target = await ctx.choose_pokemon(ctx.my_pokemon_in_play(), "Choose 1 of your Pokémon") if picks else None
    if target is not None and await ctx.attach_energy(picks[0], target):
        await ctx.heal(30, target)


card = PokemonCardDef(
    guid="d4046ea2-4472-5b2d-8e3d-c5ec81b9e59f",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Garganacl.Name",
    display_name="Garganacl",
    searchable_by=["Garganacl", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=104,
    set_code="SV4",
    regulation_mark="G",
    rarity=Rarities.Rare,
    hp=160,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Naclstack.Name",
    family_id=932,
    abilities=[
        Ability(
            title="Energizing Rock Salt",
            game_text="Once during your turn, you may attach a Basic Fighting Energy card from your discard pile to 1 of your Pokémon. If you attached Energy to a Pokémon in this way, heal 30 damage from that Pokémon.",
            activation=Activations.ONCE_PER_TURN,
            condition=_salt_condition,
            effect=energizing_rock_salt,
        ),
        Attack(
            title="Land Crush",
            game_text="",
            cost={PokemonTypes.FIGHTING: 3},
            damage=140,
        ),
    ],
)
