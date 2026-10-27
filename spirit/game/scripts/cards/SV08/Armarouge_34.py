"""Armarouge (SV08 34 -- JP SV8 021; English SSP/34). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card


async def crimson_blaster(ctx):
    fire = [e for e in ctx.attached_energies(ctx.attacker) if is_energy_of_type(e, PokemonTypes.FIRE)]
    if fire:
        await ctx.discard_cards(fire)
    await ac.snipe_attack(180, pool="bench")(ctx)


card = PokemonCardDef(
    guid="7ef3a924-4ac4-5a42-a18b-55bb9c801edd",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Armarouge.Name",
    display_name="Armarouge",
    searchable_by=["Armarouge", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=34,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    hp=140,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Charcadet.Name",
    family_id=935,
    abilities=[
        Attack(
            title="Combustion",
            game_text="",
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
        Attack(
            title="Crimson Blaster",
            game_text="Discard all Fire Energy from this Pokémon, and this attack does 180 damage to 1 of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            effect=crimson_blaster,
        ),
    ],
)
