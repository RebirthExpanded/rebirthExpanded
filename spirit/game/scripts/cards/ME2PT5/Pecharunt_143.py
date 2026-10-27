"""Pecharunt (ME2PT5 143 -- JP M2a 115; English ASC/143). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import passives_common as pc


def _final_chain_applies(ctx) -> bool:
    attacker = getattr(ctx, "ko_attacker", None)
    return (bool(getattr(ctx, "ko_from_attack", False)) and attacker is not None
            and attacker.owning_player_id != ctx.source.owning_player_id)


async def final_chain(ctx):
    picks = await ctx.search_deck(count=1, minimum=0, prompt="Choose a card to put into your hand.")
    if picks:
        await ctx.put_in_hand(picks, reveal=False)
    await ctx.shuffle_deck()


card = PokemonCardDef(
    guid="a982f0f6-96fb-5b3b-8584-497228af35c9",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pecharunt.Name",
    display_name="Pecharunt",
    searchable_by=["Pecharunt", "Basic"],
    subtypes=["Basic"],
    collector_number=143,
    set_code="ME2PT5",
    regulation_mark="I",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=1025,
    abilities=[
        Ability(
            title="Final Chain",
            game_text="If this Pokémon is Knocked Out by damage from an attack from your opponent's Pokémon, search your deck for a card and put it into your hand. Then, shuffle your deck.",
            trigger=Triggers.ON_KNOCKED_OUT,
            trigger_applies=_final_chain_applies,
            effect=final_chain,
        ),
        Attack(
            title="Mochi Rush",
            game_text="During your next turn, this Pokémon's Mochi Rush attack does 50 more damage (before applying Weakness and Resistance).",
            cost={PokemonTypes.DARKNESS: 1},
            damage=20,
            effect=pc.boost_own_next_turn(50, "Mochi Rush"),
        ),
    ],
)
