from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.data_utils import Triggers


async def final_hour(ctx):
    """KO'd in the Active Spot by an opposing attack: 3 damage counters on 1
    of the opponent's Pokemon."""
    if not (getattr(ctx, "ko_from_attack", False) and getattr(ctx, "was_active_at_ko", False)):
        return
    pool = [p for p in ctx.opponent_pokemon_in_play()]
    if not pool:
        return
    target = await ctx.choose_pokemon(pool, "Choose 1 of your opponent's Pokémon for 3 damage counters")
    if target is not None:
        await ctx.deal_damage(30, target=target, apply_modifiers=False, as_counters=True)

card = PokemonCardDef(
    guid="a77f50c1-fd32-51cc-860a-6522bd9e8989",
    key="SM6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Honedge.Name",
    display_name="Honedge",
    searchable_by=["Honedge", "Basic", "Honedge"],
    subtypes=["Basic"],
    collector_number=46,
    set_code="SM6",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=679,
    abilities=[
        Ability(
            title="Final Hour",
            game_text="If this Pok\u00e9mon is your Active Pok\u00e9mon and is Knocked Out by damage from an opponent's attack, put 3 damage counters on 1 of your opponent's Pok\u00e9mon.",
            trigger=Triggers.ON_KNOCKED_OUT_IN_PLAY,
            effect=final_hour,
            trigger_applies=lambda c: bool(c.ko_from_attack and getattr(c, 'was_active_at_ko', False)),
        ),
        Attack(
            title="Slash",
            cost={PokemonTypes.PSYCHIC: 3},
            damage=50,
        ),
    ],
)
