"""Exeggutor (SV045 24 -- JP SVEM 003; English PAF/24). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac


async def psychic_loop(ctx):
    await ctx.deal_damage()
    pool = list(ctx.attached_energies(ctx.attacker))
    n = min(2, len(pool))
    if n and ctx.attacker not in ctx.knockouts:
        picks = await ctx.choose_cards(pool, n, minimum=n, prompt="Choose 2 Energy to put into your hand")
        await ctx.put_in_hand(picks)


card = PokemonCardDef(
    guid="4b458c19-70d3-5746-9771-3cc8cef698c3",
    key="SV045",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Exeggutor.Name",
    display_name="Exeggutor",
    searchable_by=["Exeggutor", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=24,
    set_code="SV045",
    regulation_mark="G",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Exeggcute.Name",
    family_id=102,
    abilities=[
        Attack(
            title="Hypnoblast",
            game_text="Your opponent's Active Pokémon is now Asleep.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=ac.condition_attack(SpecialConditions.ASLEEP),
        ),
        Attack(
            title="Psychic Loop",
            game_text="Put 2 Energy attached to this Pokémon into your hand.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=160,
            effect=psychic_loop,
        ),
    ],
)
