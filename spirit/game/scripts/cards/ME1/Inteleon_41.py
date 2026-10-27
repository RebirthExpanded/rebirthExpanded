"""Inteleon (ME1 41 -- JP M1S 023; English MEG/142, MEG/41, MEP/2). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES


async def bring_down(ctx):
    pool = [p for pid in ctx.board.player_ids for p in ctx.board.pokemon_in_play(pid) if p is not ctx.attacker]
    if not pool:
        return
    low = min(p.get_attribute(AttrID.HP, 0) for p in pool)
    lowest = [p for p in pool if p.get_attribute(AttrID.HP, 0) == low]
    target = lowest[0] if len(lowest) == 1 else await ctx.choose_pokemon(lowest, "Choose a Pokémon to Knock Out")
    if target is not None:
        await ctx.knock_out(target)


card = PokemonCardDef(
    guid="071dc963-50b4-5d2a-ac7c-242f03f4470a",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Inteleon.Name",
    display_name="Inteleon",
    searchable_by=["Inteleon", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=41,
    set_code="ME1",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=150,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Drizzile.Name",
    family_id=816,
    abilities=[
        Attack(
            title="Bring Down",
            game_text="Choose a Pokémon in play (yours or your opponent's) that has the least HP remaining, except for this Pokémon, and it is Knocked Out.",
            cost={PokemonTypes.WATER: 1},
            effect=bring_down,
        ),
        Attack(
            title="Water Shot",
            game_text="Discard an Energy from this Pokémon.",
            cost={PokemonTypes.WATER: 1},
            damage=110,
            effect=ac.self_energy_discard_attack(count=1),
        ),
    ],
)
