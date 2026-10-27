"""Bramblin (ME2 46 -- JP M2 040; English PFL/46). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

async def sneaky_placement(ctx):
    pool = ctx.opponent_pokemon_in_play()
    if not pool:
        return
    target = await ctx.choose_pokemon(pool, "Choose 1 of your opponent's Pokémon to place 1 damage counter on")
    if target is not None:
        await ctx.deal_damage(10, target=target, apply_modifiers=False, as_counters=True)


card = PokemonCardDef(
    guid="c28b2fd1-96f2-5fdd-9559-d52ff2a7ad10",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bramblin.Name",
    display_name="Bramblin",
    searchable_by=["Bramblin", "Basic"],
    subtypes=["Basic"],
    collector_number=46,
    set_code="ME2",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=946,
    abilities=[
        Attack(
            title="Sneaky Placement",
            game_text="Place 1 damage counter on 1 of your opponent's Pokémon.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=sneaky_placement,
        ),
    ],
)
