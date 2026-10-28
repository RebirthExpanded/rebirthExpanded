"""Garbodor (SV4 117 -- JP SV4K 050; English PAR/117, PAR/204). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac

from spirit.game.session.effects import is_pokemon_tool


async def chuck(ctx):
    pool = [c for c in ctx.hand() if is_pokemon_tool(c)]
    if not pool:
        return
    picks = await ctx.discard_from_hand(len(pool), minimum=0, predicate=is_pokemon_tool, prompt="Discard any number of Pokémon Tool cards")
    if picks:
        await ctx.deal_damage(50 * len(picks))


card = PokemonCardDef(
    guid="b274ba1c-5b24-5759-a388-7c944b96498a",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Garbodor.Name",
    display_name="Garbodor",
    searchable_by=["Garbodor", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=117,
    set_code="SV4",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Trubbish.Name",
    family_id=568,
    abilities=[
        Attack(
            title="Chuck",
            game_text="Discard any number of Pokémon Tool cards from your hand. This attack does 50 damage for each card you discarded in this way.",
            cost={PokemonTypes.DARKNESS: 1},
            damage=50,
            damage_operator="x",
            effect=chuck,
        ),
        Attack(
            title="Venomous Hit",
            game_text="Your opponent's Active Pokémon is now Poisoned.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            effect=ac.condition_attack(SpecialConditions.POISONED),
        ),
    ],
)
