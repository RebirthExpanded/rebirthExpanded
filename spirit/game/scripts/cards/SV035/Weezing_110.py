"""Weezing (SV035 110 -- JP SV2a 110; English MEW/110). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.card_effects import passives_common as pc


def _blast_applies(ctx) -> bool:
    attacker = getattr(ctx, "ko_attacker", None)
    return (bool(getattr(ctx, "ko_from_attack", False)) and attacker is not None
            and attacker.owning_player_id != ctx.source.owning_player_id
            and pc.is_in_active_spot(ctx.source))


async def lets_have_a_blast(ctx):
    attacker = getattr(ctx, "ko_attacker", None)
    results = await ctx.flip_coins(1, "Let's Have a Blast")
    if results and results[0] and attacker is not None:
        await ctx.knock_out(attacker)


card = PokemonCardDef(
    guid="8bea5837-68ce-536a-93c7-02123f9dea68",
    key="SV035",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Weezing.Name",
    display_name="Weezing",
    searchable_by=["Weezing", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=110,
    set_code="SV035",
    regulation_mark="G",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Koffing.Name",
    family_id=109,
    abilities=[
        Ability(
            title="Let's Have a Blast",
            game_text="If this Pokémon is in the Active Spot and is Knocked Out by damage from an attack from your opponent's Pokémon, flip a coin. If heads, the Attacking Pokémon is Knocked Out.",
            trigger=Triggers.ON_KNOCKED_OUT,
            trigger_applies=_blast_applies,
            effect=lets_have_a_blast,
        ),
        Attack(
            title="Spinning Fumes",
            game_text="This attack also does 10 damage to each of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=ac.spread_damage(10, also_base=True),
        ),
    ],
)
