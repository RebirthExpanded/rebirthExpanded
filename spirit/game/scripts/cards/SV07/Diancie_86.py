"""Diancie (SV07 86 -- JP SV7 058; English SCR/86). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.session.effects import is_special_energy


async def diffuse_reflection(ctx):
    n = sum(1 for p in ctx.opponent_pokemon_in_play() for e in ctx.attached_energies(p) if is_special_energy(e))
    if n:
        await ctx.deal_damage(40 * n)


card = PokemonCardDef(
    guid="6b1ce39c-5c22-56e2-87e9-1fb984e7af14",
    key="SV07",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Diancie.Name",
    display_name="Diancie",
    searchable_by=["Diancie", "Basic"],
    subtypes=["Basic"],
    collector_number=86,
    set_code="SV07",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=719,
    abilities=[
        Attack(
            title="Diffuse Reflection",
            game_text="This attack does 40 damage for each Special Energy attached to all of your opponent's Pokémon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=40,
            damage_operator="x",
            effect=diffuse_reflection,
        ),
        Attack(
            title="Power Gem",
            game_text="",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
        ),
    ],
)
