"""Golduck (SV035 55 -- JP SV2a 055; English MEW/55). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.session.effects import is_pokemon_card


async def aquatic_rescue(ctx):
    pool = [c for c in ctx.discard_pile() if is_pokemon_card(c)]
    if pool:
        picks = await ctx.choose_cards(pool, min(4, len(pool)), minimum=0, prompt="Choose up to 4 Pokémon")
        if picks:
            await ctx.put_in_hand(picks)


card = PokemonCardDef(
    guid="0a466619-d802-5443-8312-264a239bdf7a",
    key="SV035",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Golduck.Name",
    display_name="Golduck",
    searchable_by=["Golduck", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=55,
    set_code="SV035",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Psyduck.Name",
    family_id=54,
    abilities=[
        Attack(
            title="Aquatic Rescue",
            game_text="Put up to 4 Pokémon from your discard pile into your hand.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=aquatic_rescue,
        ),
        Attack(
            title="Super Splash",
            game_text="",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
        ),
    ],
)
