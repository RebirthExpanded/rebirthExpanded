"""Flygon (ME2 53 -- JP M2 047; English MEP/16, PFL/101, PFL/53). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import passives_common as pc


async def sandy_flapping(ctx):
    if getattr(ctx, "evolved_pokemon", None) is not None:
        if not getattr(ctx, "evolved_from_hand", True):
            return
    else:
        attacker = getattr(ctx, "ko_attacker", None)
        if not (getattr(ctx, "ko_from_attack", False) and attacker is not None
                and attacker.owning_player_id != ctx.source.owning_player_id
                and pc.is_in_active_spot(ctx.source)):
            return
    top = list(ctx.deck_top(2, player_id=ctx.opponent_id))
    if not top or not await ctx.ask_yes_no("Use Sandy Flapping?"):
        return
    await ctx.discard_cards(top)


card = PokemonCardDef(
    guid="7bcb3153-c40c-57fe-b96f-3b2b96eefcce",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Flygon.Name",
    display_name="Flygon",
    searchable_by=["Flygon", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=53,
    set_code="ME2",
    regulation_mark="I",
    rarity=Rarities.Rare,
    hp=150,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Vibrava.Name",
    family_id=328,
    abilities=[
        Ability(
            title="Sandy Flapping",
            game_text="Once during your turn, when you play this Pokémon from your hand to evolve 1 of your Pokémon, you may use this Ability. You may also use this Ability if this Pokémon is in the Active Spot and is Knocked Out by damage from an attack from your opponent's Pokémon. Discard the top 2 cards of your opponent's deck.",
            trigger=(Triggers.ON_EVOLVE, Triggers.ON_KNOCKED_OUT),
            effect=sandy_flapping,
        ),
        Attack(
            title="Cutting Wind",
            game_text="",
            cost={PokemonTypes.FIGHTING: 2},
            damage=130,
        ),
    ],
)
