"""Tapu Koko (ME2PT5 67 -- JP M2a 054; English ASC/67). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


async def fast_flight(ctx):
    hand = list(ctx.hand())
    if hand:
        await ctx.discard_cards(hand)
    await ctx.draw_cards(5)


card = PokemonCardDef(
    guid="7f10cee1-f3e7-5ea3-a399-c570a0c82cd9",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TapuKoko.Name",
    display_name="Tapu Koko",
    searchable_by=["Tapu Koko", "Basic"],
    subtypes=["Basic"],
    collector_number=67,
    set_code="ME2PT5",
    regulation_mark="I",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=785,
    abilities=[
        Attack(
            title="Fast Flight",
            game_text="If you go first, you can use this attack during your first turn. Discard your hand and draw 5 cards.",
            cost={PokemonTypes.LIGHTNING: 1},
            effect=fast_flight,
            usable_first_turn=True,
        ),
        Attack(
            title="Thunder Blast",
            game_text="Discard 2 Energy from this Pokémon.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
            effect=ac.self_energy_discard_attack(count=2),
        ),
    ],
)
