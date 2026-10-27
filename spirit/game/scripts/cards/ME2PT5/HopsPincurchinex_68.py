"""Hop's Pincurchin ex (ME2PT5 68 -- JP SVP 233; English ASC/68). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import passives_common as pc


def _revenge(n):
    async def effect(ctx):
        attacker = ctx.damaged_by
        if attacker is not None:
            await ctx.deal_damage(10 * n, target=attacker, apply_modifiers=False, as_counters=True, is_attack=False)
    return effect


async def spiky_thunder(ctx):
    await ctx.deal_damage()
    await ctx.draw_cards(2)


card = PokemonCardDef(
    guid="52221bcf-5bb3-5e63-b95f-5e5069604303",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HopsPincurchinex.Name",
    display_name="Hop's Pincurchin ex",
    searchable_by=["Hop's Pincurchin ex", "Basic", "ex"],
    subtypes=["Basic", "ex"],
    collector_number=68,
    set_code="ME2PT5",
    regulation_mark="I",
    rarity=Rarities.RareHoloEX,
    hp=200,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=871,
    abilities=[
        Ability(
            title="Counterattack Quills",
            game_text="If this Pokémon is in the Active Spot and is damaged by an attack from your opponent's Pokémon (even if this Pokémon is Knocked Out), place 3 damage counters on the Attacking Pokémon.",
            trigger=Triggers.ON_DAMAGED_BY_ATTACK,
            trigger_applies=pc.hit_in_active_by_opponent,
            effect=_revenge(3),
        ),
        Attack(
            title="Spiky Thunder",
            game_text="Draw 2 cards.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=spiky_thunder,
        ),
    ],
)
