"""Raticate (ME3 61 -- JP M3 060; English POR/61, POR/99). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.data_utils import def_for, subtypes_for

from spirit.game.attributes import AttrID
from spirit.game.session.effects import is_pokemon_tool
from spirit.game.session.passives import effective_max_hp


async def scrape_off(ctx):
    target = ctx.opponent_active()
    if target is not None and not ctx.effects_blocked(target):
        tools = [c for c in target.children if is_pokemon_tool(c)]
        if tools:
            await ctx.discard_cards(tools)
    await ctx.deal_damage()


def _rattata_counters(ctx) -> int:
    total = 0
    for p in ctx.my_bench():
        if getattr(def_for(p.archetype_id), "display_name", None) == "Rattata":
            total += max(0, effective_max_hp(ctx.board, p) - p.get_attribute(AttrID.HP, 0)) // 10
    return total


card = PokemonCardDef(
    guid="46f12da7-005b-5b83-a21c-ca511623eaa3",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Raticate.Name",
    display_name="Raticate",
    searchable_by=["Raticate", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=61,
    set_code="ME3",
    regulation_mark="J",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Rattata.Name",
    family_id=19,
    abilities=[
        Attack(
            title="Scrape Off",
            game_text="Before doing damage, discard all Pokémon Tools from your opponent's Active Pokémon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=scrape_off,
        ),
        Attack(
            title="Retaliatory Incisors",
            game_text="This attack does 40 damage for each damage counter on all of your Benched Rattata.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=40,
            damage_operator="x",
            effect=ac.damage_per(_rattata_counters, 40),
        ),
    ],
)
