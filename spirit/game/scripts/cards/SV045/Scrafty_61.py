"""Scrafty (SV045 61 -- JP SV3a 038; English PAF/61). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac

from spirit.game.session.effects import is_basic_pokemon_in_play


async def _hit_lock_basic(ctx):
    await ctx.deal_damage()
    d = ctx.opponent_active()
    if d is not None and d not in ctx.knockouts and is_basic_pokemon_in_play(d):
        ac.lock_defender_attacks(ctx)


card = PokemonCardDef(
    guid="626e7b9e-fff1-5151-8608-f96e5b0eaf47",
    key="SV045",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Scrafty.Name",
    display_name="Scrafty",
    searchable_by=["Scrafty", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=61,
    set_code="SV045",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Scraggy.Name",
    family_id=559,
    abilities=[
        Attack(
            title="Lambaste",
            game_text="If the Defending Pokémon is a Basic Pokémon, it can't attack during your opponent's next turn.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=_hit_lock_basic,
        ),
        Attack(
            title="Headbang",
            game_text="",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
        ),
    ],
)
