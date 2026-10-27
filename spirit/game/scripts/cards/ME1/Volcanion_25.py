"""Volcanion (ME1 25 -- JP M1L 014; English MEG/25). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card


async def backfire(ctx):
    await ctx.deal_damage()
    pool = [e for e in ctx.attached_energies(ctx.attacker) if is_energy_of_type(e, PokemonTypes.FIRE)]
    if pool:
        n = min(2, len(pool))
        picks = await ctx.choose_cards(pool, n, minimum=n, prompt="Choose 2 Fire Energy to put into your hand")
        if picks:
            await ctx.put_in_hand(picks)


card = PokemonCardDef(
    guid="112c7a0c-0662-5e64-a8b6-dc13bf42b95a",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Volcanion.Name",
    display_name="Volcanion",
    searchable_by=["Volcanion", "Basic"],
    subtypes=["Basic"],
    collector_number=25,
    set_code="ME1",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=721,
    abilities=[
        Attack(
            title="Singe",
            game_text="Your opponent's Active Pokémon is now Burned.",
            cost={PokemonTypes.FIRE: 1},
            effect=ac.condition_attack(SpecialConditions.BURNED),
        ),
        Attack(
            title="Backfire",
            game_text="Put 2 Fire Energy attached to this Pokémon into your hand.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
            effect=backfire,
        ),
    ],
)
