"""Corviknight (SV2 148 -- JP SV2P 052; English PAL/148). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.card_effects import passives_common as pc


async def accelerate(ctx):
    target = ctx.opponent_active()
    await ctx.deal_damage()
    if target is not None and target in ctx.knockouts:
        await pc.apply_protection(ctx, prevent=True, effects_too=True)


card = PokemonCardDef(
    guid="036c18fb-34ba-5196-9ac4-f88247480620",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Corviknight.Name",
    display_name="Corviknight",
    searchable_by=["Corviknight", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=148,
    set_code="SV2",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=170,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Corvisquire.Name",
    family_id=821,
    abilities=[
        Attack(
            title="Accelerate",
            game_text="If your opponent's Pokémon is Knocked Out by damage from this attack, during your opponent's next turn, prevent all damage from and effects of attacks done to this Pokémon.",
            cost={PokemonTypes.METAL: 1},
            damage=50,
            effect=accelerate,
        ),
        Attack(
            title="Spinning Bird",
            game_text="Discard 2 Energy from this Pokémon.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=200,
            effect=ac.self_energy_discard_attack(count=2),
        ),
    ],
)
