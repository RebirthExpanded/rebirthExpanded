"""Mudsdale (SV05 92 -- JP SV5K 038; English TEF/175, TEF/92). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card


def _basic_fighting(card):
    return is_basic_energy_card(card) and is_energy_of_type(card, PokemonTypes.FIGHTING)


async def mud_stock(ctx):
    for p in list(ctx.my_bench()):
        pool = [c for c in ctx.discard_pile() if _basic_fighting(c)]
        if not pool:
            break
        await ctx.attach_energy(pool[0], p)


card = PokemonCardDef(
    guid="5c183448-63c0-5205-a79b-d708453d503e",
    key="SV05",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mudsdale.Name",
    display_name="Mudsdale",
    searchable_by=["Mudsdale", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=92,
    set_code="SV05",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    hp=150,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Mudbray.Name",
    family_id=749,
    abilities=[
        Attack(
            title="Mud Stock",
            game_text="Attach a Basic Fighting Energy card from your discard pile to each of your Benched Pokémon.",
            cost={PokemonTypes.FIGHTING: 1},
            effect=mud_stock,
        ),
        Attack(
            title="High Horsepower",
            game_text="This Pokémon also does 40 damage to itself.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=140,
            effect=ac.recoil_attack(40),
        ),
    ],
)
