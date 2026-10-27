"""Dedenne (ME3 29 -- JP M3 028; English POR/29, POR/93). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac
from spirit.game.card_effects import support_common as su
from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card


def _basic_lightning(card):
    return is_basic_energy_card(card) and is_energy_of_type(card, PokemonTypes.LIGHTNING)



async def tail_generator(ctx):
    n = ac.count_energy("opponent")(ctx)
    pool = [c for c in ctx.recoverable_discard() if _basic_lightning(c)]
    targets = [p for p in ctx.my_pokemon_in_play()
               if PokemonTypes.LIGHTNING.value in (p.get_attribute(AttrID.POKEMON_TYPES) or [])]
    if n <= 0 or not pool or not targets:
        return
    picks = await ctx.choose_cards(pool, min(n, len(pool)), minimum=0,
                                   prompt=f"Choose up to {n} Basic Lightning Energy cards to attach.")
    if picks:
        await su.distribute_energy(ctx, picks, targets)


card = PokemonCardDef(
    guid="4bcd612a-5d2c-5cb8-9390-a5da4bc6a7ef",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dedenne.Name",
    display_name="Dedenne",
    searchable_by=["Dedenne", "Basic"],
    subtypes=["Basic"],
    collector_number=29,
    set_code="ME3",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=702,
    abilities=[
        Attack(
            title="Tail Generator",
            game_text="Choose Basic Lightning Energy cards from your discard pile up to the amount of Energy attached to all of your opponent's Pokémon and attach them to your Lightning Pokémon in any way you like.",
            cost={PokemonTypes.LIGHTNING: 1},
            effect=tail_generator,
        ),
        Attack(
            title="Thunder Shock",
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Paralyzed.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=ac.condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
    ],
)
