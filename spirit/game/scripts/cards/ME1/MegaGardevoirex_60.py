from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import count_energy, damage_per
from spirit.game.card_effects.pokemon import energy_provides_type
from spirit.game.session.effects import is_basic_energy


def _basic_psychic(card) -> bool:
    return is_basic_energy(card) and energy_provides_type(card, PokemonTypes.PSYCHIC.value)


async def overflowing_wishes(ctx):
    """A Basic [P] Energy from the deck onto each of your Benched Pokemon."""
    bench = list(ctx.my_bench())
    if bench:
        picks = await ctx.search_deck(_basic_psychic, count=len(bench), minimum=0,
                                      prompt="Choose a Basic [P] Energy card for each of your Benched Pokémon.")
        for pokemon, energy in zip(bench, picks):
            await ctx.attach_energy(energy, pokemon)
    await ctx.shuffle_deck()

card = PokemonCardDef(
    guid="acebc836-1d64-5090-9d47-7ca1616a10d8",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MegaGardevoirex.Name",
    display_name="Mega Gardevoir ex",
    searchable_by=["Mega Gardevoir ex", "Stage 2", "ex", "SV_Mega", "MegaGardevoirex"],
    subtypes=["Stage 2", "ex", "SV_Mega"],
    collector_number=60,
    set_code="ME1",
    regulation_mark="I",
    rarity=Rarities.RareHoloEX,
    hp=360,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Kirlia.Name",
    family_id=280,
    abilities=[
        Attack(
            title="Overflowing Wishes",
            game_text="For each of your Benched Pok\u00e9mon, search your deck for a Basic [P] Energy card and attach it to that Pok\u00e9mon. Then, shuffle your deck.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=0,
            effect=overflowing_wishes,
        ),
        Attack(
            title="Mega Symphonia",
            game_text="This attack does 50 damage for each [P] Energy attached to all of your Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=50,
            damage_operator="x",
            effect=damage_per(count_energy("mine", PokemonTypes.PSYCHIC), 50),
        ),
    ],
)
