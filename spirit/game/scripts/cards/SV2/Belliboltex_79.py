"""Bellibolt ex (SV2 79 -- JP SV2D 025; English PAL/237, PAL/79). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.attributes import SpecialConditions
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card


async def paralyzing_ball(ctx):
    await ctx.deal_damage()
    pool = [e for e in ctx.attached_energies(ctx.attacker) if is_energy_of_type(e, PokemonTypes.LIGHTNING)]
    d = ctx.opponent_active()
    if len(pool) < 2 or d is None or d in ctx.knockouts or ctx.attacker in ctx.knockouts:
        return
    if await ctx.ask_yes_no("Discard 2 Lightning Energy from this Pokémon to make your opponent's Active Pokémon Paralyzed?"):
        picks = await ctx.choose_cards(pool, 2, minimum=2, prompt="Choose 2 Lightning Energy to discard")
        await ctx.discard_cards(picks)
        await ctx.apply_special_condition(d, SpecialConditions.PARALYZED)


card = PokemonCardDef(
    guid="40350512-1304-558f-8b16-2f31ac57968c",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Belliboltex.Name",
    display_name="Bellibolt ex",
    searchable_by=["Bellibolt ex", "Stage 1", "ex"],
    subtypes=["Stage 1", "ex"],
    collector_number=79,
    set_code="SV2",
    regulation_mark="G",
    rarity=Rarities.RareHoloEX,
    hp=280,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Tadbulb.Name",
    family_id=938,
    abilities=[
        Attack(
            title="Jumping Press",
            game_text="This attack does 50 damage to 1 of your opponent's Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.COLORLESS: 2},
            effect=ac.snipe_attack(50, pool="any"),
        ),
        Attack(
            title="Paralyzing Ball",
            game_text="You may discard 2 Lightning Energy from this Pokémon to make your opponent's Active Pokémon Paralyzed.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=160,
            effect=paralyzing_ball,
        ),
    ],
)
