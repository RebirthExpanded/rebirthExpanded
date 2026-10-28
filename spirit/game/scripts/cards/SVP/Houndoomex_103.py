"""Houndoom ex (SVP 103 -- JP SVD 072; English OBF/134, SVP/103). Japanese art.
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
    guid="afe9b908-f723-5655-976f-56833f016e16",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Houndoomex.Name",
    display_name="Houndoom ex",
    searchable_by=["Houndoom ex", "Stage 1", "ex"],
    subtypes=["Stage 1", "ex"],
    collector_number=103,
    set_code="SVP",
    regulation_mark="G",
    rarity=Rarities.RarePromo,
    hp=270,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Houndour.Name",
    family_id=228,
    abilities=[
        Attack(
            title="Evil Claw",
            game_text="If the Defending Pokémon is a Basic Pokémon, it can't attack during your opponent's next turn.",
            cost={PokemonTypes.DARKNESS: 2},
            damage=90,
            effect=_hit_lock_basic,
        ),
        Attack(
            title="Hound's Fang",
            game_text="This Pokémon also does 30 damage to itself.",
            cost={PokemonTypes.DARKNESS: 3},
            damage=220,
            effect=ac.recoil_attack(30),
        ),
    ],
)
