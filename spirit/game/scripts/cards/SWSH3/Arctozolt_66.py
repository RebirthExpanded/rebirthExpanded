from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def biting_whirlpool(ctx):
    """Whenever your opponent attaches an Energy card from their hand to 1 of
    their Pokémon, put 2 damage counters on that Pokémon."""
    if _biting_whirlpool_applies(ctx):
        await ctx.deal_damage(20, target=ctx.energy_receiver, apply_modifiers=False,
                              as_counters=True)


def _biting_whirlpool_applies(ctx) -> bool:
    if ctx.attaching_player_id == ctx.player_id:
        return False
    receiver = ctx.energy_receiver
    if receiver is None or receiver.owning_player_id is None:
        return False
    if receiver not in ctx.board.pokemon_in_play(receiver.owning_player_id):
        return False
    return True


card = PokemonCardDef(
    guid="30c81b90-865b-554b-b23e-c2c1d614da12",
    key="SWSH3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Arctozolt.Name",
    display_name="Arctozolt",
    searchable_by=["Arctozolt", "Stage 1", "Arctozolt"],
    subtypes=["Stage 1"],
    collector_number=66,
    set_code="SWSH3",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.RareFossil.Name",
    family_id=881,
    abilities=[
        Ability(
            title="Biting Whirlpool",
            game_text="Whenever your opponent attaches an Energy card from their hand to 1 of their Pok\u00e9mon, put 2 damage counters on that Pok\u00e9mon.",
            trigger=Triggers.ON_ENERGY_ATTACHED,
            effect=biting_whirlpool,
            trigger_applies=_biting_whirlpool_applies,
        ),
        Attack(
            title="Electro Ball",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=70,
        ),
    ],
)