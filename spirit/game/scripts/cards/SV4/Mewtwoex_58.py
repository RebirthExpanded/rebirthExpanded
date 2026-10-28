"""Mewtwo ex (SV4 58 -- JP SVEM 001; English PAR/58). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers
from spirit.game.card_effects.pokemon import TeraRulePassive

from spirit.game.card_effects import attacks_common as ac
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card


def _basic_psychic(card):
    return is_basic_energy_card(card) and is_energy_of_type(card, PokemonTypes.PSYCHIC)


async def transfer_charge(ctx):
    pool = [c for c in ctx.discard_pile() if _basic_psychic(c)]
    if not pool:
        return
    picks = await ctx.choose_cards(pool, min(2, len(pool)), minimum=0, prompt="Attach up to 2 Basic Psychic Energy cards")
    for card in picks:
        target = await ctx.choose_pokemon(ctx.my_pokemon_in_play(), "Choose 1 of your Pokémon")
        if target is not None:
            await ctx.attach_energy(card, target)


def _psy_in_play(ctx) -> int:
    return sum(1 for p in ctx.my_pokemon_in_play() for e in ctx.attached_energies(p) if is_energy_of_type(e, PokemonTypes.PSYCHIC))


card = PokemonCardDef(
    guid="081a2e0e-efd2-54d8-9142-350bea4c6c98",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mewtwoex.Name",
    display_name="Mewtwo ex",
    searchable_by=["Mewtwo ex", "Basic", "ex", "Tera"],
    subtypes=["Basic", "ex", "Tera"],
    collector_number=58,
    set_code="SV4",
    regulation_mark="G",
    rarity=Rarities.RareHoloEX,
    hp=230,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=150,
    passive=TeraRulePassive(),
    abilities=[
        Attack(
            title="Transfer Charge",
            game_text="Attach up to 2 Basic Psychic Energy cards from your discard pile to your Pokémon in any way you like.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=transfer_charge,
        ),
        Attack(
            title="Photon Kinesis",
            game_text="This attack does 30 more damage for each Psychic Energy attached to all of your Pokémon.",
            cost={PokemonTypes.PSYCHIC: 2},
            damage=10,
            damage_operator="+",
            effect=ac.damage_per(_psy_in_play, 30, base=10),
        ),
    ],
)
