"""Oinkologne (SV1 157 -- JP SVG 028; English SVI/157). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


async def leg_stomp(ctx):
    await ctx.deal_damage()
    results = await ctx.flip_coins(1, "Leg Stomp")
    if results and not results[0]:
        ac.lock_all_attacks(ctx, ctx.attacker)


card = PokemonCardDef(
    guid="71b373a5-8de5-5d7c-b5e5-140859379792",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Oinkologne.Name",
    display_name="Oinkologne",
    searchable_by=["Oinkologne", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=157,
    set_code="SV1",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Lechonk.Name",
    family_id=915,
    abilities=[
        Attack(
            title="Ram",
            game_text="",
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
        Attack(
            title="Leg Stomp",
            game_text="Flip a coin. If tails, during your next turn, this Pokémon can't attack.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=130,
            effect=leg_stomp,
        ),
    ],
)
