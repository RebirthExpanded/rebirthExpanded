from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers, is_pokemon_v
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import snipe_attack


async def shocking_block(ctx):
    """Whenever any player attaches an Energy from hand to their Pokemon V, put 2 damage counters on it."""
    if _shocking_block_applies(ctx):
        await ctx.deal_damage(20, target=ctx.energy_receiver, apply_modifiers=False,
                              as_counters=True)


def _shocking_block_applies(ctx) -> bool:
    receiver = ctx.energy_receiver
    if receiver is None or receiver.owning_player_id is None:
        return False
    if receiver not in ctx.board.pokemon_in_play(receiver.owning_player_id):
        return False
    return is_pokemon_v(receiver.archetype_id)


card = PokemonCardDef(
    guid="b6f25036-ac03-5190-ba5e-f4f448c4528c",
    key="CZ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RadiantCharjabug.Name",
    display_name="Radiant Charjabug",
    searchable_by=["Radiant Charjabug", "Basic", "Radiant", "RadiantCharjabug"],
    subtypes=["Basic", "Radiant"],
    collector_number=51,
    set_code="CZ",
    rarity=Rarities.RareRadiant,
    hp=90,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=737,
    abilities=[
        Ability(
            title="Shocking Block",
            game_text="Whenever any player attaches an Energy card from their hand to 1 of their Pok\u00e9mon V, put 2 damage counters on that Pok\u00e9mon.",
            trigger=Triggers.ON_ENERGY_ATTACHED,
            effect=shocking_block,
            trigger_applies=_shocking_block_applies,
        ),
        Attack(
            title="Linear Attack",
            game_text="This attack does 30 damage to 1 of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.LIGHTNING: 1},
            effect=snipe_attack(30, pool="any", count=1, side="opponent"),
        ),
    ],
)