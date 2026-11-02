"""Sakura Afro Pikachu (SMPJ 211 -- JP SMP 211; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES



async def _cherry_blossoms(ctx):
    """Flip 2 coins. Heal 30 damage times the number of heads from 1 of your Pokemon."""
    results = await ctx.flip_coins(2, ctx.ability.title if ctx.ability else "")
    amount = 30 * sum(1 for r in results if r)
    if not amount:
        return
    damaged = [p for p in ctx.my_pokemon_in_play() if ctx.max_hp(p) > p.get_attribute(AttrID.HP, 0)]
    if not damaged:
        return
    target = await ctx.choose_pokemon(damaged, "Choose a Pokémon to heal")
    if target is not None:
        await ctx.heal(amount, target)


card = PokemonCardDef(
    guid="236f3e13-d9e3-5272-b6cf-eec529d3cde8",
    key="SMPJ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.SakuraAfroPikachu.Name",
    display_name="Sakura Afro Pikachu",
    searchable_by=["Sakura Afro Pikachu", "Basic"],
    subtypes=["Basic"],
    collector_number=211,
    set_code="SMPJ",
    regulation_mark="B",
    rarity=Rarities.RarePromo,
    hp=60,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=172,
    abilities=[
        Attack(
            title="Cherry Blossoms Bloom",
            game_text="Flip 2 coins. Heal 30 damage for each heads from 1 of your Pokémon.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=_cherry_blossoms,
        ),
        Attack(
            title="Pika Bolt",
            game_text="",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
    ],
)
