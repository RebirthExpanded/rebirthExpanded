from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.data_utils import def_for
from spirit.game.card_effects.attacks_common import lock_all_attacks
from spirit.game.card_effects.pokemon import is_lightning_energy
from spirit.game.session.effects import is_basic_energy


def _is_ionos(pokemon) -> bool:
    name = getattr(def_for(pokemon.archetype_id), "display_name", "") or ""
    return name.startswith("Iono's ")


def _basic_lightning(card) -> bool:
    return is_basic_energy(card) and is_lightning_energy(card)


def _electric_streamer_condition(board, player_id, pokemon) -> bool:
    hand = board.find_player_area(player_id, "hand")
    return any(_basic_lightning(c) for c in (hand.children if hand else [])) and any(
        _is_ionos(p) for p in board.pokemon_in_play(player_id))


async def electric_streamer(ctx):
    """Attach Basic [L] Energy from hand to your Iono's Pokemon until Done."""
    while True:
        pool = [c for c in ctx.hand() if _basic_lightning(c)]
        targets = [p for p in ctx.my_pokemon_in_play() if _is_ionos(p)]
        if not pool or not targets:
            return
        picks = await ctx.choose_cards(pool, 1, minimum=0,
                                       prompt="Choose a Basic [L] Energy card to attach (or Done)")
        if not picks:
            return
        target = await ctx.choose_pokemon(targets, "Choose 1 of your Iono's Pokémon")
        if target is None:
            return
        await ctx.attach_energy(picks[0], target)


async def thunderous_bolt(ctx):
    """230. During your next turn, this Pokemon can't attack."""
    await ctx.deal_damage()
    lock_all_attacks(ctx, ctx.attacker)

card = PokemonCardDef(
    guid="de06fdcb-4287-547b-a87b-85f779d7ef70",
    key="SV09",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.IonosBelliboltex.Name",
    display_name="Iono's Bellibolt ex",
    searchable_by=["Iono's Bellibolt ex", "Stage 1", "ex", "IonosBelliboltex"],
    subtypes=["Stage 1", "ex"],
    collector_number=53,
    set_code="SV09",
    regulation_mark="I",
    rarity=Rarities.RareHoloEX,
    hp=280,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.IonosTadbulb.Name",
    family_id=938,
    abilities=[
        Ability(
            title="Electric Streamer",
            game_text="As often as you like during your turn, you may attach a Basic [L] Energy card from your hand to 1 of your Iono\'s Pok\u00e9mon.",
            activation=Activations.UNLIMITED,
            condition=_electric_streamer_condition,
            effect=electric_streamer,
        ),
        Attack(
            title="Thunderous Bolt",
            game_text="During your next turn, this Pok\u00e9mon can't attack.",
            cost={PokemonTypes.LIGHTNING: 3, PokemonTypes.COLORLESS: 1},
            damage=230,
            effect=thunderous_bolt,
        ),
    ],
)
