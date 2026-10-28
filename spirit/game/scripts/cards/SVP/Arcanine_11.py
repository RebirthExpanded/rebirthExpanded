"""Arcanine (SVP 11 -- JP SVP 003; English SVP/11). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

async def _flip_discard_energy(ctx):
    await ctx.deal_damage()
    results = await ctx.flip_coins(1, ctx.ability.title if ctx.ability else "")
    target = ctx.opponent_active()
    if results and results[0] and target is not None and not ctx.effects_blocked(target) \
            and ctx.attached_energies(target):
        await ctx.discard_energy_from(target, 1, minimum=1,
                                      prompt="Choose an Energy to discard from your opponent's Active Pokémon")


card = PokemonCardDef(
    guid="486c1e26-3d8c-5d60-9931-dd52abfff930",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Arcanine.Name",
    display_name="Arcanine",
    searchable_by=["Arcanine", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=11,
    set_code="SVP",
    regulation_mark="G",
    rarity=Rarities.RarePromo,
    hp=130,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Growlithe.Name",
    family_id=58,
    abilities=[
        Attack(
            title="Crunch",
            game_text="Flip a coin. If heads, discard an Energy from your opponent's Active Pokémon.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=_flip_discard_energy,
        ),
        Attack(
            title="Fire Mane",
            game_text="",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
        ),
    ],
)
