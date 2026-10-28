"""Electrode (SV035 101 -- JP SV2a 101; English MEW/101, PAF/134). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.session.effects import is_pokemon_tool


async def bang_boom_chain(ctx):
    pool = [c for p in ctx.my_pokemon_in_play() for c in p.children if is_pokemon_tool(c)]
    picks = []
    if pool:
        picks = await ctx.choose_cards(pool, len(pool), minimum=0, prompt="Discard any number of Pokémon Tools from your Pokémon")
        if picks:
            await ctx.discard_cards(picks)
    await ctx.deal_damage(20 + 40 * len(picks))


card = PokemonCardDef(
    guid="166a903f-7625-578d-b6f7-c46b40226973",
    key="SV035",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Electrode.Name",
    display_name="Electrode",
    searchable_by=["Electrode", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=101,
    set_code="SV035",
    regulation_mark="G",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Voltorb.Name",
    family_id=100,
    abilities=[
        Attack(
            title="Bang Boom Chain",
            game_text="Before doing damage, you may discard any number of Pokémon Tools from your Pokémon. This attack does 40 more damage for each card you discarded in this way.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=20,
            damage_operator="+",
            effect=bang_boom_chain,
        ),
        Attack(
            title="Electro Ball",
            game_text="",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=70,
        ),
    ],
)
