from spirit.game.data_utils import PokemonCardDef, Ability, Attack, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


FEZANDIPITI_EX_GUID = "6bcb2b55-3a89-4488-a5bb-22970907013f"


def _flip_the_script_condition(board, player_id, pokemon) -> bool:
    # "any of your Pokémon were Knocked Out during your opponent's last
    # turn" is tracked only for KO-by-attack in the engine's turn ledger.
    ts = getattr(board, "turn_state", None)
    if ts is None:
        return False
    return bool(getattr(ts, "kos_by_attack_last_turn", {}).get(player_id))


async def flip_the_script(ctx):
    await ctx.draw_cards(3)


async def cruel_arrow(ctx):
    target = await ctx.choose_pokemon(
        ctx.opponent_pokemon_in_play(),
        "Choose 1 of your opponent's Pokémon",
    )
    if target is None:
        return
    await ctx.deal_damage(100, target=target)


card = PokemonCardDef(
    guid=FEZANDIPITI_EX_GUID,
    key="SV065",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Fezandipitiex.Name",
    display_name="Fezandipiti ex",
    searchable_by=["Fezandipiti ex", "Basic", "ex", "Fezandipitiex"],
    subtypes=["Basic", "ex"],
    collector_number=38,
    set_code="SV065",
    regulation_mark="H",
    rarity=Rarities.RareHoloEX,
    hp=210,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=1016,
    abilities=[
        Ability(
            title="Flip the Script",
            game_text=(
                "Once during your turn, if any of your Pokémon were "
                "Knocked Out during your opponent's last turn, you may "
                "draw 3 cards.\n\nYou can't use more than 1 Flip the Script "
                "Ability each turn."
            ),
            activation=Activations.ONCE_PER_TURN,
            shared_once_per_turn="Flip the Script",
            condition=_flip_the_script_condition,
            effect=flip_the_script,
        ),
        Attack(
            title="Cruel Arrow",
            game_text="",
            cost={PokemonTypes.COLORLESS: 3},
            damage=100,
            effect=cruel_arrow,
        ),
    ],
)

