"""Lugia (ME6A 97 -- JP M6a 097; English 30C/121). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.session.effects import is_energy_of_type, is_pokemon_card


async def elemental_blast(ctx):
    await ctx.deal_damage()
    for t in (PokemonTypes.FIRE, PokemonTypes.WATER, PokemonTypes.LIGHTNING):
        pool = [e for e in ctx.attached_energies(ctx.attacker) if is_energy_of_type(e, t)]
        if not pool:
            continue
        picks = pool[:1] if len(pool) == 1 else await ctx.choose_cards(
            pool, 1, minimum=1, prompt=f"Choose a {t.name.capitalize()} Energy to discard")
        if picks:
            await ctx.discard_cards(picks)


card = PokemonCardDef(
    guid="ee98337b-6327-587b-93e7-32302ad754c7",
    key="ME6A",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lugia.Name",
    display_name="Lugia",
    searchable_by=["Lugia", "Basic"],
    subtypes=["Basic"],
    collector_number=97,
    set_code="ME6A",
    regulation_mark="J",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=249,
    abilities=[
        Attack(
            title="Elemental Blast",
            game_text="Discard a Fire Energy, a Water Energy, and a Lightning Energy from this Pokémon.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.WATER: 1, PokemonTypes.LIGHTNING: 1},
            damage=250,
            effect=elemental_blast,
        ),
    ],
)
