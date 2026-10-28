"""Ninetales (SV3 29 -- JP SV3 015; English OBF/199, OBF/29). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


async def nine_tailed_dance(ctx):
    pool = ctx.opponent_pokemon_in_play()
    target = await ctx.choose_pokemon(pool, "Choose 1 of your opponent's Pokémon to put 9 damage counters on") if pool else None
    if target is not None:
        await ctx.deal_damage(90, target=target, apply_modifiers=False, as_counters=True)
    ac.lock_all_attacks(ctx, ctx.attacker)


card = PokemonCardDef(
    guid="6460b74a-7502-5e46-b3cc-4d44f1811f4f",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ninetales.Name",
    display_name="Ninetales",
    searchable_by=["Ninetales", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=29,
    set_code="SV3",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Vulpix.Name",
    family_id=37,
    abilities=[
        Attack(
            title="Will-O-Wisp",
            game_text="",
            cost={PokemonTypes.FIRE: 1},
            damage=20,
        ),
        Attack(
            title="Nine-Tailed Dance",
            game_text="Put 9 damage counters on 1 of your opponent's Pokémon. During your next turn, this Pokémon can't attack.",
            cost={PokemonTypes.FIRE: 2},
            effect=nine_tailed_dance,
        ),
    ],
)
