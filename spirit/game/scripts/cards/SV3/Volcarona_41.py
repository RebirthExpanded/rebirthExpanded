"""Volcarona (SV3 41 -- JP SV1a 013; English OBF/41). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card


def _basic_fire(card):
    return is_basic_energy_card(card) and is_energy_of_type(card, PokemonTypes.FIRE)


async def flame_cloak(ctx):
    await ctx.deal_damage()
    pool = [c for c in ctx.discard_pile() if _basic_fire(c)]
    if pool and ctx.attacker not in ctx.knockouts:
        picks = await ctx.choose_cards(pool, 1, minimum=1, prompt="Choose a Basic Fire Energy card to attach")
        if picks:
            await ctx.attach_energy(picks[0], ctx.attacker)


card = PokemonCardDef(
    guid="e7e94ef7-942d-5b82-ab01-b1b44b12e8df",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Volcarona.Name",
    display_name="Volcarona",
    searchable_by=["Volcarona", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=41,
    set_code="SV3",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=140,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Larvesta.Name",
    family_id=636,
    abilities=[
        Attack(
            title="Flame Cloak",
            game_text="Attach a Basic Fire Energy card from your discard pile to this Pokémon.",
            cost={PokemonTypes.FIRE: 1},
            damage=30,
            effect=flame_cloak,
        ),
        Attack(
            title="Heat Blast",
            game_text="",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
        ),
    ],
)
