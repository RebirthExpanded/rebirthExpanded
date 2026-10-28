"""Hydreigon (SV2 140 -- JP SV1a 059; English PAL/140). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.session.effects import is_energy_card


def _tri_howl_condition(board, player_id, pokemon) -> bool:
    deck = board.find_player_area(player_id, "deck")
    return bool(deck and deck.children)


async def tri_howl(ctx):
    top = list(ctx.deck_top(3))
    if not top:
        return
    await ctx.reveal_cards(top, to_player=ctx.player_id)
    pool = [c for c in top if is_energy_card(c)]
    attached = []
    if pool:
        picks = await ctx.choose_cards(pool, len(pool), minimum=0, prompt="Choose any number of Energy cards to attach")
        for card in picks:
            target = await ctx.choose_pokemon(ctx.my_pokemon_in_play(), "Choose 1 of your Pokémon to attach it to")
            if target is not None and await ctx.attach_energy(card, target):
                attached.append(card)
    rest = [c for c in top if c not in attached]
    if rest:
        await ctx.discard_cards(rest)


card = PokemonCardDef(
    guid="de1edf8f-f62e-5882-b115-909ee2a385b8",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hydreigon.Name",
    display_name="Hydreigon",
    searchable_by=["Hydreigon", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=140,
    set_code="SV2",
    regulation_mark="G",
    rarity=Rarities.Rare,
    hp=180,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Zweilous.Name",
    family_id=633,
    abilities=[
        Ability(
            title="Tri Howl",
            game_text="Once during your turn, you may look at the top 3 cards of your deck and attach any number of Energy cards you find there to your Pokémon in any way you like. Discard the other cards.",
            activation=Activations.ONCE_PER_TURN,
            condition=_tri_howl_condition,
            effect=tri_howl,
        ),
        Attack(
            title="Dark Cutter",
            game_text="",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=160,
        ),
    ],
)
