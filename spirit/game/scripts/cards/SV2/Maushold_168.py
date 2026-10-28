"""Maushold (SV2 168 -- JP SV2D 064; English PAL/168, PAL/226). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES


async def gnaw_relentlessly(ctx):
    n = sum(1 for p in ctx.my_pokemon_in_play() if p.get_attribute(AttrID.EVOLUTION_LOGIC_NAME) == "Maushold")
    if not n:
        return
    for p in list(ctx.opponent_pokemon_in_play()):
        await ctx.deal_damage(10 * n, target=p, apply_modifiers=False, as_counters=True)


card = PokemonCardDef(
    guid="8fcec24c-1d74-59da-b69d-3b4eff323fa6",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Maushold.Name",
    display_name="Maushold",
    searchable_by=["Maushold", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=168,
    set_code="SV2",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Tandemaus.Name",
    family_id=924,
    abilities=[
        Attack(
            title="Gentle Slap",
            game_text="",
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
        Attack(
            title="Gnaw Relentlessly",
            game_text="Put 1 damage counter on each of your opponent's Pokémon for each of your Maushold in play.",
            cost={PokemonTypes.COLORLESS: 3},
            effect=gnaw_relentlessly,
        ),
    ],
)
