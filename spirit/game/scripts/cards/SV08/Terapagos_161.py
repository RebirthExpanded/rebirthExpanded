"""Terapagos (SV08 161 -- JP SV8 093; English ASC/178, SSP/161). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.data_utils import def_for, subtypes_for


def _has_sub(card, sub) -> bool:
    return card is not None and sub in (subtypes_for(card.archetype_id) or [])
from spirit.game.data_utils import def_for, subtypes_for


async def prism_charge(ctx):
    teras = [p for p in ctx.my_pokemon_in_play() if _has_sub(p, "Tera")]
    if not teras:
        await ctx.shuffle_deck()
        return
    got = set()
    for _ in range(3):
        picks = await ctx.search_deck(lambda c: is_basic_energy_card(c) and getattr(def_for(c.archetype_id), "display_name", "") not in got,
                                      count=1, minimum=0, prompt="Choose a Basic Energy card of a different type.")
        if not picks:
            break
        got.add(getattr(def_for(picks[0].archetype_id), "display_name", ""))
        target = await ctx.choose_pokemon(teras, "Choose 1 of your Tera Pokémon to attach it to")
        if target is not None:
            await ctx.attach_energy(picks[0], target)
    await ctx.shuffle_deck()


card = PokemonCardDef(
    guid="1c5aa52b-cb9b-5163-8843-efdaf121d46e",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Terapagos.Name",
    display_name="Terapagos",
    searchable_by=["Terapagos", "Basic"],
    subtypes=["Basic"],
    collector_number=161,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=1024,
    abilities=[
        Attack(
            title="Prism Charge",
            game_text="Search your deck for up to 3 Basic Energy cards of different types and attach them to your Tera Pokémon in any way you like. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=prism_charge,
        ),
        Attack(
            title="Hard Tackle",
            game_text="",
            cost={PokemonTypes.COLORLESS: 3},
            damage=100,
        ),
    ],
)
