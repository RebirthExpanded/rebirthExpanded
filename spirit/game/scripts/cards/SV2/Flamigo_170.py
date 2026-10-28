"""Flamigo (SV2 170 -- JP SV2D 065; English PAF/211, PAL/170, PAL/227). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.data_utils import def_for, subtypes_for
from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES

from spirit.game.session.effects import is_pokemon_card


async def insta_flock(ctx):
    if not getattr(ctx, "benched_from_hand", True):
        return
    if not ctx.deck_top(1) or not await ctx.ask_yes_no("Use Insta-Flock?"):
        return
    picks = await ctx.search_deck(lambda c: c.get_attribute(AttrID.EVOLUTION_LOGIC_NAME) == "Flamigo",
                                  count=3, minimum=0, prompt="Choose up to 3 Flamigo.")
    if picks:
        await ctx.put_in_hand(picks)
    await ctx.shuffle_deck()


def _united_wings(ctx) -> int:
    return sum(1 for c in ctx.discard_pile() if is_pokemon_card(c)
               and any(getattr(a, "title", "") == "United Wings" for a in getattr(def_for(c.archetype_id), "abilities", [])))


card = PokemonCardDef(
    guid="77668fbb-db6d-5034-9b6f-c029f37d2fb6",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Flamigo.Name",
    display_name="Flamigo",
    searchable_by=["Flamigo", "Basic"],
    subtypes=["Basic"],
    collector_number=170,
    set_code="SV2",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=973,
    abilities=[
        Ability(
            title="Insta-Flock",
            game_text="When you play this Pokémon from your hand onto your Bench during your turn, you may search your deck for up to 3 Flamigo, reveal them, and put them into your hand. Then, shuffle your deck.",
            trigger=Triggers.ON_PLAY,
            effect=insta_flock,
        ),
        Attack(
            title="United Wings",
            game_text="This attack does 20 damage for each Pokémon in your discard pile that has the United Wings attack.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="x",
            effect=ac.damage_per(_united_wings, 20),
        ),
    ],
)
