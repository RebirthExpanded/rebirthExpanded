"""Oinkologne (SV09 140 -- JP SVM 122; English JTG/140). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


async def aromatic_stomps(ctx):
    await ctx.deal_damage()
    results = await ctx.flip_coins(1, "Aromatic Stomps")
    if results and results[0]:
        ac.lock_defender_attacks(ctx)


card = PokemonCardDef(
    guid="46e2b1a0-7602-51f8-886f-084ece70f06a",
    key="SV09",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Oinkologne.Name",
    display_name="Oinkologne",
    searchable_by=["Oinkologne", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=140,
    set_code="SV09",
    regulation_mark="H",
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
            title="Aromatic Stomps",
            game_text="Flip a coin. If heads, during your opponent's next turn, the Defending Pokémon can't attack.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=aromatic_stomps,
        ),
        Attack(
            title="Headbutt Bounce",
            game_text="",
            cost={PokemonTypes.COLORLESS: 3},
            damage=120,
        ),
    ],
)
