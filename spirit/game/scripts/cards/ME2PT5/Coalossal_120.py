"""Coalossal (ME2PT5 120 -- JP M2a 097; English ASC/120). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card


def _basic_fighting(card):
    return is_basic_energy_card(card) and is_energy_of_type(card, PokemonTypes.FIGHTING)


async def tar_cannon(ctx):
    if sum(1 for c in ctx.discard_pile() if _basic_fighting(c)) < 10:
        return
    await ac.snipe_attack(140, pool="any")(ctx)


card = PokemonCardDef(
    guid="8f9c58f8-d4d6-5245-9147-1553cd6002ce",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Coalossal.Name",
    display_name="Coalossal",
    searchable_by=["Coalossal", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=120,
    set_code="ME2PT5",
    regulation_mark="I",
    rarity=Rarities.Rare,
    hp=180,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Carkol.Name",
    family_id=837,
    abilities=[
        Attack(
            title="Tar Cannon",
            game_text="This attack does 140 damage to 1 of your opponent's Pokémon. If you don't have 10 or more Basic Fighting Energy cards in your discard pile, this attack does nothing. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.FIGHTING: 1},
            effect=tar_cannon,
        ),
        Attack(
            title="Bulky Bump",
            game_text="Discard 3 Energy from this Pokémon.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 3},
            damage=220,
            effect=ac.self_energy_discard_attack(count=3),
        ),
    ],
)
