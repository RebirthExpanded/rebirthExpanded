"""Team Rocket's Exeggutor (ME2PT5 78 -- JP M2a 062; English ASC/78). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


async def tri_kinesis(ctx):
    results = await ctx.flip_coins(3, "Tri Kinesis")
    if not (results and all(results)):
        return
    pool = [p for p in ctx.opponent_pokemon_in_play() if not ctx.effects_blocked(p)]
    target = await ctx.choose_pokemon(pool, "Choose 1 of your opponent's Pokémon to Knock Out") if pool else None
    if target is not None:
        await ctx.knock_out(target)


card = PokemonCardDef(
    guid="4d2f5fb2-b6e6-5c65-9ab8-b2935e69ae96",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsExeggutor.Name",
    display_name="Team Rocket's Exeggutor",
    searchable_by=["Team Rocket's Exeggutor", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=78,
    set_code="ME2PT5",
    regulation_mark="I",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsExeggcute.Name",
    family_id=102,
    abilities=[
        Attack(
            title="Tri Kinesis",
            game_text="Flip 3 coins. If all of them are heads, Knock Out 1 of your opponent's Pokémon.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=tri_kinesis,
        ),
        Attack(
            title="Double-Edge",
            game_text="This Pokémon also does 30 damage to itself.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=150,
            effect=ac.recoil_attack(30),
        ),
    ],
)
