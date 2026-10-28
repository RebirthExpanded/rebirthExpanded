"""Pawmot ex (SV3 73 -- JP SVP1 005; English OBF/73). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card


async def levin_strike(ctx):
    pool = [e for e in ctx.attached_energies(ctx.attacker) if is_energy_of_type(e, PokemonTypes.LIGHTNING)]
    if len(pool) < 2:
        return
    picks = await ctx.choose_cards(pool, 2, minimum=2, prompt="Choose 2 Lightning Energy to discard")
    await ctx.discard_cards(picks)
    await ac.snipe_attack(220, pool="any")(ctx)


card = PokemonCardDef(
    guid="759179f4-422b-55c9-8d71-e28df36a6668",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pawmotex.Name",
    display_name="Pawmot ex",
    searchable_by=["Pawmot ex", "Stage 2", "ex"],
    subtypes=["Stage 2", "ex"],
    collector_number=73,
    set_code="SV3",
    regulation_mark="G",
    rarity=Rarities.RareHoloEX,
    hp=300,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pawmo.Name",
    family_id=921,
    abilities=[
        Attack(
            title="Zap Kick",
            game_text="",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=60,
        ),
        Attack(
            title="Levin Strike",
            game_text="Discard 2 Lightning Energy from this Pokémon. This attack does 220 damage to 1 of your opponent's Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.LIGHTNING: 2},
            effect=levin_strike,
        ),
    ],
)
