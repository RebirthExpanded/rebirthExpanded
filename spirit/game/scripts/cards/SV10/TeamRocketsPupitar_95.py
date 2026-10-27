"""Team Rocket's Pupitar (SV10 95 -- JP SV10 049; English DRI/95). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES


async def _evolve_from_deck(ctx, pokemon) -> bool:
    logic_name = pokemon.get_attribute(AttrID.EVOLUTION_LOGIC_NAME)
    if not logic_name:
        return False
    picks = await ctx.search_deck(
        lambda c, name=logic_name: c.get_attribute(AttrID.EVOLUTION_LOGIC_FROM) == name,
        count=1, minimum=0, prompt="Choose a card that evolves from this Pokémon.")
    if picks:
        await ctx.evolve_pokemon(pokemon, picks[0])
        return True
    return False


async def explosive_ascension(ctx):
    await ctx.deal_damage()
    if ctx.attacker in ctx.knockouts:
        return
    await _evolve_from_deck(ctx, ctx.attacker)
    await ctx.shuffle_deck()


card = PokemonCardDef(
    guid="79774f39-946f-5591-8da7-35f50027c20b",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsPupitar.Name",
    display_name="Team Rocket's Pupitar",
    searchable_by=["Team Rocket's Pupitar", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=95,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsLarvitar.Name",
    family_id=246,
    abilities=[
        Attack(
            title="Explosive Ascension",
            game_text="Search your deck for a card that evolves from this Pokémon and put it onto this Pokémon to evolve it. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=explosive_ascension,
        ),
    ],
)
