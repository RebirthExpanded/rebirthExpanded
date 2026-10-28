"""Pidgeot (SV035 18 -- JP SV2a 018; English MEW/18). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import passives_common as pc


async def fly(ctx):
    results = await ctx.flip_coins(1, "Fly")
    if not (results and results[0]):
        return
    await ctx.deal_damage()
    await pc.apply_protection(ctx, prevent=True, effects_too=True)


card = PokemonCardDef(
    guid="89727697-372c-5a87-be00-52ec8897b3b0",
    key="SV035",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pidgeot.Name",
    display_name="Pidgeot",
    searchable_by=["Pidgeot", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=18,
    set_code="SV035",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pidgeotto.Name",
    family_id=16,
    abilities=[
        Attack(
            title="Flap",
            game_text="",
            cost={PokemonTypes.COLORLESS: 1},
            damage=40,
        ),
        Attack(
            title="Fly",
            game_text="Flip a coin. If tails, this attack does nothing. If heads, during your opponent's next turn, prevent all damage from and effects of attacks done to this Pokémon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=150,
            effect=fly,
        ),
    ],
)
