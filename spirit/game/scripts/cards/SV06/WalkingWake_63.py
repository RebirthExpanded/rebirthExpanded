"""Walking Wake (SV06 63 -- JP SV5a 026; English TWM/63). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su
from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES


async def undulating_slice(ctx):
    hp = ctx.attacker.get_attribute(AttrID.HP, 0) or 0
    most = max(0, min(9, hp // 10))
    if not most:
        return
    index = await ctx.choose("How many damage counters will you put on this Pokémon?", [str(i) for i in range(most + 1)])
    n = index if isinstance(index, int) and 0 <= index <= most else 0
    if n:
        await ctx.deal_damage(10 * n, target=ctx.attacker, apply_modifiers=False, as_counters=True)
        await ctx.deal_damage(20 * n)


card = PokemonCardDef(
    guid="b1b4e041-969a-558a-bd92-a27a714440e8",
    key="SV06",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.WalkingWake.Name",
    display_name="Walking Wake",
    searchable_by=["Walking Wake", "Basic", "Ancient"],
    subtypes=["Basic", "Ancient"],
    collector_number=63,
    set_code="SV06",
    regulation_mark="H",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=1009,
    abilities=[
        Attack(
            title="Aurora Gain",
            game_text="Heal 20 damage from this Pokémon.",
            cost={PokemonTypes.WATER: 1},
            damage=20,
            effect=su.heal_attack(20),
        ),
        Attack(
            title="Undulating Slice",
            game_text="Put up to 9 damage counters on this Pokémon. This attack does 20 damage for each damage counter you placed in this way.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="x",
            effect=undulating_slice,
        ),
    ],
)
