from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.pokemon import TeraRulePassive


async def orichalcum_fang(ctx):
    """50, +120 if any of your Pokemon were KO'd by attack damage last turn."""
    lost = ctx.session.turn_state.kos_by_attack_last_turn.get(ctx.player_id, [])
    await ctx.deal_damage(50 + (120 if lost else 0))

card = PokemonCardDef(
    guid="512f5461-0f58-5359-8891-eea5cbc5020e",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Koraidonex.Name",
    display_name="Koraidon ex",
    searchable_by=["Koraidon ex", "Basic", "ex", "Tera", "Koraidonex"],
    subtypes=["Basic", "ex", "Tera"],
    collector_number=121,
    set_code="ME2PT5",
    regulation_mark="J",
    rarity=Rarities.RareHoloEX,
    hp=230,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=1007,
    passive=TeraRulePassive(),
    abilities=[
        Attack(
            title="Orichalcum Fang",
            game_text="If any of your Pok\u00e9mon were Knocked Out by damage from an attack during your opponent's last turn, this attack does 120 more damage.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            damage_operator="+",
            effect=orichalcum_fang,
        ),
        Attack(
            title="Impact Blow",
            game_text="During your next turn, this Pok\u00e9mon can't use Impact Blow.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=200,
            locks_next_turn=True,
        ),
    ],
)
