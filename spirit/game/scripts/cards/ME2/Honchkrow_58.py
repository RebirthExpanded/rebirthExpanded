"""Honchkrow (ME2 58 -- JP MBG 005; English PFL/58). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


async def sniping_feathers(ctx):
    pool = list(ctx.attached_energies(ctx.attacker))
    n = min(2, len(pool))
    if n:
        picks = await ctx.choose_cards(pool, n, minimum=n, prompt="Choose 2 Energy to discard from this Pokémon")
        await ctx.discard_cards(picks)
    await ac.snipe_attack(120, pool="any")(ctx)


card = PokemonCardDef(
    guid="413c00c3-2d33-5bd0-8325-761cd15ffa7e",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Honchkrow.Name",
    display_name="Honchkrow",
    searchable_by=["Honchkrow", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=58,
    set_code="ME2",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Murkrow.Name",
    family_id=198,
    abilities=[
        Attack(
            title="Wind of Darkness",
            game_text="",
            cost={PokemonTypes.DARKNESS: 1},
            damage=30,
        ),
        Attack(
            title="Sniping Feathers",
            game_text="Discard 2 Energy from this Pokémon, and this attack does 120 damage to 1 of your opponent's Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            effect=sniping_feathers,
        ),
    ],
)
