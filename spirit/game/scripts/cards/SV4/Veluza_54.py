"""Veluza (SV4 54 -- JP SV4K 026; English PAR/192, PAR/54). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.card_effects import passives_common as pc
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card


def _ko_by_opponent(ctx) -> bool:
    attacker = getattr(ctx, "ko_attacker", None)
    return (bool(getattr(ctx, "ko_from_attack", False)) and attacker is not None
            and attacker.owning_player_id != ctx.source.owning_player_id)

from spirit.game.attributes import PokemonTypes as _PT


def _memento_applies(ctx) -> bool:
    return _ko_by_opponent(ctx) and pc.is_in_active_spot(ctx.source)


async def fillet_memento(ctx):
    pool = [e for e in ctx.attached_energies(ctx.source) if is_energy_of_type(e, PokemonTypes.WATER)]
    bench = [p for p in ctx.my_bench() if p is not ctx.source]
    if not pool or not bench:
        return
    target = await ctx.choose_pokemon(bench, "Choose 1 of your Benched Pokémon")
    if target is None:
        return
    picks = await ctx.choose_cards(pool, min(2, len(pool)), minimum=0, prompt="Move up to 2 Water Energy cards")
    for e in picks:
        await ctx.move_energy(e, target)


card = PokemonCardDef(
    guid="627e8c32-2ae6-5eb0-a559-5a80451563a0",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Veluza.Name",
    display_name="Veluza",
    searchable_by=["Veluza", "Basic"],
    subtypes=["Basic"],
    collector_number=54,
    set_code="SV4",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=976,
    abilities=[
        Ability(
            title="Fillet Memento",
            game_text="If this Pokémon is in the Active Spot and is Knocked Out by damage from an attack from your opponent's Pokémon, move up to 2 Water Energy cards from this Pokémon to 1 of your Benched Pokémon.",
            trigger=Triggers.ON_KNOCKED_OUT,
            trigger_applies=_memento_applies,
            effect=fillet_memento,
        ),
        Attack(
            title="Hydro Pump",
            game_text="This attack does 20 more damage for each Water Energy attached to this Pokémon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
            damage_operator="+",
            effect=ac.damage_per(ac.count_energy("self", _PT.WATER), 20, base=60),
        ),
    ],
)
