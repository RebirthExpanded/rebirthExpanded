"""Mischievous Pichu (SPJ 214 -- JP SP 214; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

async def _slapstick_party(ctx):
    heads = (await ctx.flip_coins(1, "Slapstick Party"))[0]
    targets = ctx.opponent_pokemon_in_play() if heads else ctx.my_pokemon_in_play()
    for p in list(targets):
        await ctx.deal_damage(10, target=p)


card = PokemonCardDef(
    guid="5807f406-08b8-5018-ad00-014c837087be",
    key="SPJ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MischievousPichu.Name",
    display_name="Mischievous Pichu",
    searchable_by=["Mischievous Pichu", "Basic"],
    subtypes=["Basic"],
    collector_number=214,
    set_code="SPJ",
    regulation_mark="F",
    rarity=Rarities.RarePromo,
    hp=30,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=172,
    abilities=[
        Attack(
            title="Slapstick Party",
            game_text="Flip a coin. If heads, this attack does 10 damage to all of your opponent's Pokémon. If tails, this attack does 10 damage to all your Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.COLORLESS: 1},
            effect=_slapstick_party,
        ),
    ],
)
