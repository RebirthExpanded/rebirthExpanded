from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import count_prizes_taken, damage_per


async def _discard_one(ctx):
    """Discard an Energy from this Pokemon."""
    energies = ctx.attached_energies(ctx.attacker)
    if not energies:
        return
    picks = await ctx.choose_cards(energies, 1, prompt="Choose an Energy to discard from this Pokémon")
    if picks:
        await ctx.discard_cards(picks)

card = PokemonCardDef(
    guid="1699d25a-3bde-5edf-ab73-6f2dff41ce0b",
    key="RSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Reshiramex.Name",
    display_name="Reshiram ex",
    searchable_by=["Reshiram ex", "Basic", "ex", "Reshiramex"],
    subtypes=["Basic", "ex"],
    collector_number=20,
    set_code="RSV10PT5",
    regulation_mark="I",
    rarity=Rarities.RareHoloEX,
    hp=230,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=643,
    abilities=[
        Attack(
            title="Slash",
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
        Attack(
            title="Blazing Burst",
            game_text="This attack does 50 more damage for each Prize card your opponent has taken. Discard an Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
            damage_operator="+",
            effect=damage_per(count_prizes_taken("opponent"), 50, base=130, also=_discard_one),
        ),
    ],
)
