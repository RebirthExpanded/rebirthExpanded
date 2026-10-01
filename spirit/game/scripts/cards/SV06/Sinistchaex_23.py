from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.pokemon import energy_provides_type
from spirit.game.session.effects import is_basic_energy


def _basic_grass(card) -> bool:
    return is_basic_energy(card) and energy_provides_type(card, PokemonTypes.GRASS.value)


async def re_brew(ctx):
    """2 counters on an opposing Pokemon per Basic [G] Energy in your discard
    pile, then shuffle those Energy into your deck."""
    energies = [c for c in ctx.recoverable_discard() if _basic_grass(c)]
    pool = ctx.opponent_pokemon_in_play()
    if energies and pool:
        target = await ctx.choose_pokemon(pool, "Choose 1 of your opponent's Pokémon")
        if target is not None:
            await ctx.deal_damage(20 * len(energies), target=target,
                                  apply_modifiers=False, as_counters=True)
    if energies:
        await ctx.reveal_cards(energies)
        await ctx.shuffle_into_deck(energies, ctx.player_id)


async def matcha_splash(ctx):
    """120. Heal 30 damage from each of your Pokemon."""
    await ctx.deal_damage()
    for pokemon in list(ctx.my_pokemon_in_play()):
        await ctx.heal(30, pokemon)

card = PokemonCardDef(
    guid="178f223a-0103-5b3b-a663-9f9a839576e8",
    key="SV06",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sinistchaex.Name",
    display_name="Sinistcha ex",
    searchable_by=["Sinistcha ex", "Stage 1", "ex", "Sinistchaex"],
    subtypes=["Stage 1", "ex"],
    collector_number=23,
    set_code="SV06",
    regulation_mark="H",
    rarity=Rarities.RareHoloEX,
    hp=240,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Poltchageist.Name",
    family_id=1012,
    abilities=[
        Attack(
            title="Re-Brew",
            game_text="Put 2 damage counters on 1 of your opponent's Pok\u00e9mon for each Basic [G] Energy card in your discard pile. Then, shuffle those Energy cards into your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=0,
            effect=re_brew,
        ),
        Attack(
            title="Matcha Splash",
            game_text="Heal 30 damage from each of your Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=matcha_splash,
        ),
    ],
)
