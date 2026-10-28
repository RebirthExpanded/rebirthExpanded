"""Growlithe (SV035 58 -- JP SV2a 058; English MEW/58). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.session.effects import is_energy_of_type, is_pokemon_card


async def vaporize(ctx):
    await ctx.deal_damage()
    d = ctx.opponent_active()
    if d is None or d in ctx.knockouts or ctx.effects_blocked(d):
        return
    pool = [e for e in ctx.attached_energies(d) if is_energy_of_type(e, PokemonTypes.WATER)]
    if pool:
        picks = await ctx.choose_cards(pool, 1, minimum=1, prompt="Choose a Water Energy to discard")
        await ctx.discard_cards(picks)


card = PokemonCardDef(
    guid="752b6c52-ee75-50a5-b986-aea0071ffbed",
    key="SV035",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Growlithe.Name",
    display_name="Growlithe",
    searchable_by=["Growlithe", "Basic"],
    subtypes=["Basic"],
    collector_number=58,
    set_code="SV035",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=58,
    abilities=[
        Attack(
            title="Vaporize",
            game_text="Discard a Water Energy from your opponent's Active Pokémon.",
            cost={PokemonTypes.FIRE: 1},
            damage=10,
            effect=vaporize,
        ),
    ],
)
