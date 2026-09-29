from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.session.passives import TurnDamageModifier


async def torrential_heart(ctx):
    """5 damage counters on this Pokemon; its attacks do +120 to the opposing
    Active this turn (a TurnDamageModifier keyed to this entity)."""
    pokemon = ctx.source
    await ctx.deal_damage(50, target=pokemon, apply_modifiers=False, as_counters=True)
    ctx.add_turn_damage_modifier(TurnDamageModifier(
        amount=120, player_id=ctx.player_id, source_entity_id=pokemon.entity_id))

card = PokemonCardDef(
    guid="53bddec4-8863-5cc0-bd6e-ae8bd15bb8f7",
    key="SV05",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Feraligatr.Name",
    display_name="Feraligatr",
    searchable_by=["Feraligatr", "Stage 2", "Feraligatr"],
    subtypes=["Stage 2"],
    collector_number=41,
    set_code="SV05",
    regulation_mark="H",
    rarity=Rarities.Rare,
    hp=180,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Croconaw.Name",
    family_id=158,
    abilities=[
        Ability(
            title="Torrential Heart",
            game_text="Once during your turn, you may put 5 damage counters on this Pok\u00e9mon. If you do, during this turn, attacks used by this Pok\u00e9mon do 120 more damage to your opponent's Active Pok\u00e9mon (before applying Weakness and Resistance).",
            activation=Activations.ONCE_PER_TURN,
            effect=torrential_heart,
        ),
        Attack(
            title="Giant Wave",
            game_text="During your next turn, this Pok\u00e9mon can't use Giant Wave.",
            cost={PokemonTypes.WATER: 2},
            damage=160,
            locks_next_turn=True,
        ),
    ],
)
