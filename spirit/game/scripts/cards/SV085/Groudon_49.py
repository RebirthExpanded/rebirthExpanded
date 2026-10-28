"""Groudon (SV085 49 -- JP SV3a 026; English PAR/199, PAR/93, PRE/49). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card


def _basic_fighting(card):
    return is_basic_energy_card(card) and is_energy_of_type(card, PokemonTypes.FIGHTING)


async def swelling_power(ctx):
    pool = [c for c in ctx.hand() if _basic_fighting(c)]
    if not pool:
        return
    picks = await ctx.choose_cards(pool, 1, minimum=1, prompt="Choose a Basic Fighting Energy card to attach")
    target = await ctx.choose_pokemon(ctx.my_pokemon_in_play(), "Choose 1 of your Pokémon") if picks else None
    if target is not None:
        await ctx.attach_energy(picks[0], target)


async def magma_purge(ctx):
    pool = [e for p in ctx.my_pokemon_in_play() for e in ctx.attached_energies(p)]
    if not pool:
        return
    picks = await ctx.choose_cards(pool, min(4, len(pool)), minimum=0, prompt="Discard up to 4 Energy from your Pokémon")
    if picks:
        await ctx.discard_cards(picks)
        await ctx.deal_damage(60 * len(picks))


card = PokemonCardDef(
    guid="f748edaa-4e65-54ea-a9e1-bdb6315bf2bf",
    key="SV085",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Groudon.Name",
    display_name="Groudon",
    searchable_by=["Groudon", "Basic"],
    subtypes=["Basic"],
    collector_number=49,
    set_code="SV085",
    regulation_mark="G",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    family_id=383,
    abilities=[
        Attack(
            title="Swelling Power",
            game_text="Attach a Basic Fighting Energy card from your hand to 1 of your Pokémon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=swelling_power,
        ),
        Attack(
            title="Magma Purge",
            game_text="Discard up to 4 Energy from your Pokémon. This attack does 60 damage for each card you discarded in this way.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=60,
            damage_operator="x",
            effect=magma_purge,
        ),
    ],
)
