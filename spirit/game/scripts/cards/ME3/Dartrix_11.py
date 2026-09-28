from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def feather_shot(ctx):
    """Discard all Energy from this Pokemon; 90 to 1 of the opponent's Pokemon."""
    energies = list(ctx.attached_energies(ctx.attacker))
    if energies:
        await ctx.discard_cards(energies)
    pool = ctx.opponent_pokemon_in_play()
    if not pool:
        return
    target = await ctx.choose_pokemon(pool, "Choose 1 of your opponent's Pokémon to take 90 damage")
    await ctx.deal_damage(90, target=target or ctx.defender)

card = PokemonCardDef(
    guid="20f26ecc-fd8a-52ff-bda9-1288c4a2f4d9",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dartrix.Name",
    display_name="Dartrix",
    searchable_by=["Dartrix", "Stage 1", "Dartrix"],
    subtypes=["Stage 1"],
    collector_number=11,
    set_code="ME3",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Rowlet.Name",
    family_id=722,
    abilities=[
        Attack(
            title="Leafage",
            cost={PokemonTypes.GRASS: 1},
            damage=20,
        ),
        Attack(
            title="Feather Shot",
            game_text="Discard all Energy from this Pok\u00e9mon, and this attack does 90 damage to 1 of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 3},
            damage=0,
            effect=feather_shot,
        ),
    ],
)
