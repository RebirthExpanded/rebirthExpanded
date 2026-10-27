"""Ambipom (ME2 79 -- JP M2 067; English PFL/107, PFL/79). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


async def dual_tail(ctx):
    pool = list(ctx.attached_energies(ctx.attacker))
    n = min(2, len(pool))
    if n:
        picks = await ctx.choose_cards(pool, n, minimum=n, prompt="Choose 2 Energy to discard from this Pokémon")
        await ctx.discard_cards(picks)
    await ac.snipe_attack(60, pool="any", count=2)(ctx)


card = PokemonCardDef(
    guid="a634a78d-af22-5785-af92-762015f8a6c3",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ambipom.Name",
    display_name="Ambipom",
    searchable_by=["Ambipom", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=79,
    set_code="ME2",
    regulation_mark="I",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Aipom.Name",
    family_id=190,
    abilities=[
        Attack(
            title="Slap",
            game_text="",
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
        Attack(
            title="Dual Tail",
            game_text="Discard 2 Energy from this Pokémon, and this attack does 60 damage to each of 2 of your opponent's Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.COLORLESS: 3},
            effect=dual_tail,
        ),
    ],
)
