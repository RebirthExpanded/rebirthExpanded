from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import self_energy_discard_attack


async def corkscrew_dive(ctx):
    """100. You may draw cards until you have 6 cards in your hand."""
    await ctx.deal_damage()
    if ctx.hand_size() < 6 and ctx.deck() and await ctx.ask_yes_no(
            "Draw cards until you have 6 cards in your hand?"):
        await ctx.draw_until(6)

card = PokemonCardDef(
    guid="57546798-cbda-5c55-a021-b887b8e2d0c7",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.CynthiasGarchompex.Name",
    display_name="Cynthia's Garchomp ex",
    searchable_by=["Cynthia's Garchomp ex", "Stage 2", "ex", "CynthiasGarchompex"],
    subtypes=["Stage 2", "ex"],
    collector_number=104,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.RareHoloEX,
    hp=330,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.CynthiasGabite.Name",
    family_id=443,
    abilities=[
        Attack(
            title="Corkscrew Dive",
            game_text="You may draw cards until you have 6 cards in your hand.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=100,
            effect=corkscrew_dive,
        ),
        Attack(
            title="Draconic Buster",
            game_text="Discard all Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 2},
            damage=260,
            effect=self_energy_discard_attack(all_energy=True),
        ),
    ],
)
