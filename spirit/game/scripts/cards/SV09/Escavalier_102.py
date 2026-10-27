"""Escavalier (SV09 102 -- JP SV9 063; English JTG/102). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


async def _hit_then_lock(ctx):
    await ctx.deal_damage()
    ac.lock_all_attacks(ctx, ctx.attacker)


card = PokemonCardDef(
    guid="beadddcc-e310-58a7-b998-cd1861966b64",
    key="SV09",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Escavalier.Name",
    display_name="Escavalier",
    searchable_by=["Escavalier", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=102,
    set_code="SV09",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Karrablast.Name",
    family_id=588,
    abilities=[
        Attack(
            title="Pierce",
            game_text="",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
        Attack(
            title="Iron Buster",
            game_text="During your next turn, this Pokémon can't attack.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=_hit_then_lock,
        ),
    ],
)
