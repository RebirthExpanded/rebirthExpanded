"""Annihilape ex (SVP 32 -- JP SV2P 040; English PAL/242, SVP/32). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES


async def angry_grudge(ctx):
    hp = ctx.attacker.get_attribute(AttrID.HP, 0) or 0
    most = max(0, min(12, hp // 10))
    if not most:
        return
    index = await ctx.choose("How many damage counters will you put on this Pokémon?", [str(i) for i in range(most + 1)])
    n = index if isinstance(index, int) and 0 <= index <= most else 0
    if n:
        await ctx.deal_damage(10 * n, target=ctx.attacker, apply_modifiers=False, as_counters=True)
        await ctx.deal_damage(20 * n)


card = PokemonCardDef(
    guid="c74463ed-f0a0-5170-8972-590fb661cd54",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Annihilapeex.Name",
    display_name="Annihilape ex",
    searchable_by=["Annihilape ex", "Stage 2", "ex"],
    subtypes=["Stage 2", "ex"],
    collector_number=32,
    set_code="SVP",
    regulation_mark="G",
    rarity=Rarities.RarePromo,
    hp=320,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Primeape.Name",
    family_id=56,
    abilities=[
        Attack(
            title="Angry Grudge",
            game_text="Put up to 12 damage counters on this Pokémon. This attack does 20 damage for each damage counter you placed in this way.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=20,
            damage_operator="x",
            effect=angry_grudge,
        ),
        Attack(
            title="Seismic Toss",
            game_text="",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=150,
        ),
    ],
)
