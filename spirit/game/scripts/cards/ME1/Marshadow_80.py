"""Marshadow (ME1 80 -- JP M1L 032; English MEG/146, MEG/80). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import passives_common as pc


async def shadowy_side_kick(ctx):
    target = ctx.opponent_active()
    await ctx.deal_damage()
    if target is not None and target in ctx.knockouts:
        await pc.apply_protection(ctx, prevent=True, effects_too=True)


card = PokemonCardDef(
    guid="f1e84bd6-9e31-5b1a-b0a2-269f289ca0b3",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Marshadow.Name",
    display_name="Marshadow",
    searchable_by=["Marshadow", "Basic"],
    subtypes=["Basic"],
    collector_number=80,
    set_code="ME1",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=802,
    abilities=[
        Attack(
            title="Shadowy Side Kick",
            game_text="If your opponent's Pokémon is Knocked Out by damage from this attack, during your opponent's next turn, prevent all damage from and effects of attacks done to this Pokémon.",
            cost={PokemonTypes.FIGHTING: 2},
            damage=60,
            effect=shadowy_side_kick,
        ),
    ],
)
