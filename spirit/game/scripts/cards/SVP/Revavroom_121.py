"""Revavroom (SVP 121 -- JP SVP 094; English SVP/121). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

async def _flip_discard_energy(ctx):
    await ctx.deal_damage()
    results = await ctx.flip_coins(1, ctx.ability.title if ctx.ability else "")
    target = ctx.opponent_active()
    if results and results[0] and target is not None and not ctx.effects_blocked(target) \
            and ctx.attached_energies(target):
        await ctx.discard_energy_from(target, 1, minimum=1,
                                      prompt="Choose an Energy to discard from your opponent's Active Pokémon")
from spirit.game.card_effects import attacks_common as ac


def _bigger_hand(ctx) -> bool:
    return len(ctx.hand()) > len(ctx.hand(ctx.opponent_id))


card = PokemonCardDef(
    guid="447e55e1-9fae-5195-898d-b37f8897b01a",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Revavroom.Name",
    display_name="Revavroom",
    searchable_by=["Revavroom", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=121,
    set_code="SVP",
    regulation_mark="G",
    rarity=Rarities.RarePromo,
    hp=140,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Varoom.Name",
    family_id=965,
    abilities=[
        Attack(
            title="Swagger",
            game_text="Flip a coin. If heads, discard an Energy from your opponent's Active Pokémon.",
            cost={PokemonTypes.METAL: 1},
            effect=_flip_discard_energy,
        ),
        Attack(
            title="Huge Tackle",
            game_text="If you have more cards in your hand than your opponent, this attack does 80 more damage.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=70,
            damage_operator="+",
            effect=ac.bonus_if(_bigger_hand, 80),
        ),
    ],
)
