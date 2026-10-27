"""Espathra (SV08 95 -- JP SV7a 023; English SSP/95). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su

from spirit.game.session.effects import is_evolution_pokemon


async def mystical_eyes(ctx):
    pool = [p for p in ctx.opponent_pokemon_in_play() if is_evolution_pokemon(p) and not ctx.effects_blocked(p)]
    if pool:
        target = await ctx.choose_pokemon(pool, "Choose 1 of your opponent's evolved Pokémon to devolve")
        if target is not None:
            await ctx.devolve_pokemon(target, 1, "hand")


card = PokemonCardDef(
    guid="ad15c4c5-9457-5bae-9d31-2d16bbd0ddc3",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Espathra.Name",
    display_name="Espathra",
    searchable_by=["Espathra", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=95,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Flittle.Name",
    family_id=955,
    abilities=[
        Attack(
            title="Mystical Eyes",
            game_text="Devolve 1 of your opponent's evolved Pokémon by putting the highest Stage Evolution card on it into your opponent's hand.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=mystical_eyes,
        ),
        Attack(
            title="Spiral Drain",
            game_text="Heal 30 damage from this Pokémon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
            effect=su.heal_attack(30),
        ),
    ],
)
