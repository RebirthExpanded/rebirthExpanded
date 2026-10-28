"""Tapu Koko ex (SV4 68 -- JP SV3a 019; English PAR/222, PAR/247, PAR/68). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac


def _lost_one(ctx) -> bool:
    return ctx.kos_by_attack_last_turn() > 0


async def vengeful_shock(ctx):
    lost = _lost_one(ctx)
    await ctx.deal_damage(120 if lost else 30)
    d = ctx.opponent_active()
    if lost and d is not None and d not in ctx.knockouts:
        await ctx.apply_special_condition(d, SpecialConditions.PARALYZED)


card = PokemonCardDef(
    guid="934e4d31-208e-5957-b796-0620987d1e33",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TapuKokoex.Name",
    display_name="Tapu Koko ex",
    searchable_by=["Tapu Koko ex", "Basic", "ex"],
    subtypes=["Basic", "ex"],
    collector_number=68,
    set_code="SV4",
    regulation_mark="G",
    rarity=Rarities.RareHoloEX,
    hp=210,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=785,
    abilities=[
        Attack(
            title="Vengeful Shock",
            game_text="If any of your Pokémon were Knocked Out by damage from an attack during your opponent's last turn, this attack does 90 more damage, and your opponent's Active Pokémon is now Paralyzed.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="+",
            effect=vengeful_shock,
        ),
        Attack(
            title="Extreme Current",
            game_text="Discard an Energy from this Pokémon.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=180,
            effect=ac.self_energy_discard_attack(count=1),
        ),
    ],
)
