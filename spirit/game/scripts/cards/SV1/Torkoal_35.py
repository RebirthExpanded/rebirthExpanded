"""Torkoal (SV1 35 -- JP SV1S 009; English SVI/35). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.session.effects import is_energy_of_type, is_pokemon_card


async def concentrated_fire(ctx):
    n = sum(1 for e in ctx.attached_energies(ctx.attacker) if is_energy_of_type(e, PokemonTypes.FIRE))
    heads = sum(1 for r in await ctx.flip_coins(n, "Concentrated Fire") if r) if n else 0
    if heads:
        await ctx.deal_damage(80 * heads)


card = PokemonCardDef(
    guid="5f6c59e5-be6c-50dd-98bb-c5d12785957f",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Torkoal.Name",
    display_name="Torkoal",
    searchable_by=["Torkoal", "Basic"],
    subtypes=["Basic"],
    collector_number=35,
    set_code="SV1",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    family_id=324,
    abilities=[
        Attack(
            title="Stampede",
            game_text="",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
        Attack(
            title="Concentrated Fire",
            game_text="Flip a coin for each Fire Energy attached to this Pokémon. This attack does 80 damage for each heads.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            damage_operator="x",
            effect=concentrated_fire,
        ),
    ],
)
