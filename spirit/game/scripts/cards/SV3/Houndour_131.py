"""Houndour (SV3 131 -- JP SV3 071; English OBF/131, OBF/204). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card


def _basic_darkness(card):
    return is_basic_energy_card(card) and is_energy_of_type(card, PokemonTypes.DARKNESS)


async def coordinated_pack(ctx):
    for p in list(ctx.my_bench()):
        if p.get_attribute(AttrID.EVOLUTION_LOGIC_NAME) != "Houndour":
            continue
        picks = await ctx.search_deck(_basic_darkness, count=1, minimum=0, prompt="Choose a Basic Darkness Energy card to attach")
        if picks:
            await ctx.attach_energy(picks[0], p)
    await ctx.shuffle_deck()


card = PokemonCardDef(
    guid="50b6ecec-9146-5de1-95e8-21cf72e98349",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Houndour.Name",
    display_name="Houndour",
    searchable_by=["Houndour", "Basic"],
    subtypes=["Basic"],
    collector_number=131,
    set_code="SV3",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=228,
    abilities=[
        Attack(
            title="Coordinated Pack",
            game_text="For each of your Benched Houndour, search your deck for a Basic Darkness Energy card and attach it to that Houndour. Then, shuffle your deck.",
            cost={PokemonTypes.DARKNESS: 1},
            effect=coordinated_pack,
        ),
        Attack(
            title="Focus Fangs",
            game_text="Flip a coin. If tails, this attack does nothing.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=ac.flip_or_nothing(),
        ),
    ],
)
