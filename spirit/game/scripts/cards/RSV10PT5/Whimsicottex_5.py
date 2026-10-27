"""Whimsicott ex (RSV10PT5 5 -- JP SV11W 005; English WHT/157, WHT/165, WHT/5). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su
from spirit.game.card_effects.trainers import is_basic_energy_card

from spirit.game.session.effects import is_trainer_card


async def wondrous_cotton(ctx):
    hand = list(ctx.hand(ctx.opponent_id))
    if hand:
        await ctx.reveal_hand(of_player=ctx.opponent_id, to_player=ctx.player_id)
    n = sum(1 for c in hand if is_trainer_card(c))
    if n:
        await ctx.deal_damage(50 * n)


card = PokemonCardDef(
    guid="c4061341-409c-5409-a694-2f45b11bdc77",
    key="RSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Whimsicottex.Name",
    display_name="Whimsicott ex",
    searchable_by=["Whimsicott ex", "Stage 1", "ex"],
    subtypes=["Stage 1", "ex"],
    collector_number=5,
    set_code="RSV10PT5",
    regulation_mark="I",
    rarity=Rarities.RareHoloEX,
    hp=230,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Cottonee.Name",
    family_id=546,
    abilities=[
        Attack(
            title="Energy Gift",
            game_text="Search your deck for up to 3 Basic Energy cards and attach them to your Pokémon in any way you like. Then, shuffle your deck.",
            cost={PokemonTypes.GRASS: 1},
            effect=su.search_attach_energy(is_basic_energy_card, count=3, prompt="Choose up to 3 Basic Energy cards to attach to your Pokémon."),
        ),
        Attack(
            title="Wondrous Cotton",
            game_text="Your opponent reveals their hand. This attack does 50 damage for each Trainer card you find there.",
            cost={PokemonTypes.GRASS: 1},
            damage=50,
            damage_operator="x",
            effect=wondrous_cotton,
        ),
    ],
)
