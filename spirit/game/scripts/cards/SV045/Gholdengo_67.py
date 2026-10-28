"""Gholdengo (SV045 67 -- JP SV4a 133; English PAF/67). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.session.effects import is_energy_of_type, is_pokemon_card
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card


def _basic_metal(card):
    return is_basic_energy_card(card) and is_energy_of_type(card, PokemonTypes.METAL)


async def lavish_hospitality(ctx):
    pool = [c for c in ctx.hand() if _basic_metal(c)]
    if not pool:
        return
    picks = await ctx.choose_cards(pool, len(pool), minimum=0, prompt="Attach any number of Basic Metal Energy cards")
    for card in picks:
        target = await ctx.choose_pokemon(ctx.my_pokemon_in_play(), "Choose 1 of your Pokémon")
        if target is not None:
            await ctx.attach_energy(card, target)


async def scintillating_surfing(ctx):
    n = sum(1 for e in ctx.attached_energies(ctx.attacker) if is_energy_of_type(e, PokemonTypes.METAL))
    heads = sum(1 for r in await ctx.flip_coins(n, "Scintillating Surfing") if r) if n else 0
    if heads:
        await ctx.deal_damage(80 * heads)


card = PokemonCardDef(
    guid="c00dc61c-005e-59ef-b28b-5acef336b143",
    key="SV045",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gholdengo.Name",
    display_name="Gholdengo",
    searchable_by=["Gholdengo", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=67,
    set_code="SV045",
    regulation_mark="G",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Gimmighoul.Name",
    family_id=999,
    abilities=[
        Attack(
            title="Lavish Hospitality",
            game_text="You may attach any number of Basic Metal Energy cards from your hand to your Pokémon in any way you like.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=lavish_hospitality,
        ),
        Attack(
            title="Scintillating Surfing",
            game_text="Flip a coin for each Metal Energy attached to this Pokémon. This attack does 80 damage for each heads.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            damage_operator="x",
            effect=scintillating_surfing,
        ),
    ],
)
