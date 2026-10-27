"""Mewtwo ex (ME6A 55 -- JP M6a 055; English 30C/151, 30C/157, 30C/64). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


async def _hit_then_lock(ctx):
    await ctx.deal_damage()
    ac.lock_all_attacks(ctx, ctx.attacker)
from spirit.game.data_utils import def_for, subtypes_for


async def photon_bullets(ctx):
    for p in list(ctx.opponent_pokemon_in_play()):
        if "ex" in (subtypes_for(p.archetype_id) or []):
            await ctx.deal_damage(50, target=p)


card = PokemonCardDef(
    guid="57f5820b-20fb-50c8-8e44-41f5a90bff47",
    key="ME6A",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mewtwoex.Name",
    display_name="Mewtwo ex",
    searchable_by=["Mewtwo ex", "Basic", "ex"],
    subtypes=["Basic", "ex"],
    collector_number=55,
    set_code="ME6A",
    regulation_mark="J",
    rarity=Rarities.RareHoloEX,
    hp=230,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=150,
    abilities=[
        Attack(
            title="Photon Bullets",
            game_text="This attack does 50 damage to each of your opponent's Pokémon ex. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.PSYCHIC: 2},
            effect=photon_bullets,
        ),
        Attack(
            title="Psychic Powers",
            game_text="During your next turn, this Pokémon can't use attacks.",
            cost={PokemonTypes.PSYCHIC: 3},
            damage=230,
            effect=_hit_then_lock,
        ),
    ],
)
