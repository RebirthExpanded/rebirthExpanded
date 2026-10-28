"""Aerodactyl (SV035 142 -- JP SV2a 142; English MEW/142). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.session.effects import is_evolution_pokemon


async def devolution_ray(ctx):
    await ctx.deal_damage()
    d = ctx.opponent_active()
    if d is not None and d not in ctx.knockouts and not ctx.effects_blocked(d) and is_evolution_pokemon(d):
        await ctx.devolve_pokemon(d, 1, "hand")


card = PokemonCardDef(
    guid="e10b96df-a11d-5067-afcd-dd8e67a88232",
    key="SV035",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Aerodactyl.Name",
    display_name="Aerodactyl",
    searchable_by=["Aerodactyl", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=142,
    set_code="SV035",
    regulation_mark="G",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.trainer.AntiqueOldAmber.Name",
    family_id=142,
    abilities=[
        Attack(
            title="Glide",
            game_text="",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
        Attack(
            title="Devolution Ray",
            game_text="If your opponent's Active Pokémon is an evolved Pokémon, devolve it by putting the highest Stage Evolution card on it into your opponent's hand.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=100,
            effect=devolution_ray,
        ),
    ],
)
