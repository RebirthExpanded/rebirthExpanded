"""Mandibuzz ex (ME2PT5 139 -- JP MC 475; English ASC/139). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


async def vulture_claw(ctx):
    await ctx.deal_damage()
    await ac.discard_random_from_hand(ctx, ctx.opponent_id)


card = PokemonCardDef(
    guid="0a7f397e-bf4e-5567-a410-efba1cb1325b",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mandibuzzex.Name",
    display_name="Mandibuzz ex",
    searchable_by=["Mandibuzz ex", "Stage 1", "ex"],
    subtypes=["Stage 1", "ex"],
    collector_number=139,
    set_code="ME2PT5",
    regulation_mark="J",
    rarity=Rarities.RareHoloEX,
    hp=260,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Vullaby.Name",
    family_id=629,
    abilities=[
        Attack(
            title="Bone Shot",
            game_text="This attack does 50 damage to 1 of your opponent's Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.COLORLESS: 2},
            effect=ac.snipe_attack(50, pool="any"),
        ),
        Attack(
            title="Vulture Claw",
            game_text="Discard a random card from your opponent's hand.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=160,
            effect=vulture_claw,
        ),
    ],
)
