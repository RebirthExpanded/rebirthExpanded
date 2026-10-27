"""Miraidon (ME5 28 -- JP M5 027; English MEP/82, PBL/28). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card


def _basic_lightning(card):
    return is_basic_energy_card(card) and is_energy_of_type(card, PokemonTypes.LIGHTNING)



def _photon_applies(ctx) -> bool:
    return bool(getattr(ctx, "ko_from_attack", False) and getattr(ctx, "was_active_at_ko", False)
                and ctx.my_bench() and any(_basic_lightning(e) for e in ctx.attached_energies(ctx.source)))


async def photon_cord(ctx):
    pool = [e for e in ctx.attached_energies(ctx.source) if _basic_lightning(e)]
    bench = [p for p in ctx.my_bench() if p is not ctx.source]
    if not pool or not bench:
        return
    picks = await ctx.choose_cards(pool, min(2, len(pool)), minimum=0,
                                   prompt="Choose up to 2 Basic Lightning Energy cards to move")
    if not picks:
        return
    target = await ctx.choose_pokemon(bench, "Choose a Benched Pokémon to move the Energy to")
    if target is not None:
        for energy in picks:
            await ctx.move_energy(energy, target)


card = PokemonCardDef(
    guid="fd7046f0-5a93-50af-8dd4-0ae4dfbbb285",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Miraidon.Name",
    display_name="Miraidon",
    searchable_by=["Miraidon", "Basic"],
    subtypes=["Basic"],
    collector_number=28,
    set_code="ME5",
    regulation_mark="J",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=1008,
    abilities=[
        Ability(
            title="Photon Cord",
            game_text="If this Pokémon is in the Active Spot and is Knocked Out by damage from an attack from your opponent's Pokémon, move up to 2 Basic Lightning Energy cards from this Pokémon to 1 of your Benched Pokémon.",
            trigger=Triggers.ON_KNOCKED_OUT_IN_PLAY,
            trigger_applies=_photon_applies,
            effect=photon_cord,
        ),
        Attack(
            title="Thunder",
            game_text="This Pokémon also does 30 damage to itself.",
            cost={PokemonTypes.LIGHTNING: 2},
            damage=90,
            effect=ac.recoil_attack(30),
        ),
    ],
)
