"""Malamar (SV065 34 -- JP SV6a 034; English SFA/34). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.data_utils import def_for, subtypes_for


def _played_this_turn(ctx, display_name) -> bool:
    for archetype_id, _name, _type in ctx.session.turn_state.trainers_played:
        if getattr(def_for(archetype_id), "display_name", None) == display_name:
            return True
    return False


async def colluding_tentacles(ctx):
    if not _played_this_turn(ctx, "Xerosic's Machinations"):
        return
    old = ctx.opponent_active()
    bench = ctx.opponent_bench()
    if old is None or not bench or ctx.effects_blocked(old):
        return
    target = await ctx.choose_pokemon(bench, "Choose the opponent's new Active Pokémon")
    if target is not None and await ctx.switch_active(ctx.opponent_id, target):
        await ctx.deal_damage(120, target=target)


card = PokemonCardDef(
    guid="f75d12de-0ff9-5e00-9148-b671f2788466",
    key="SV065",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Malamar.Name",
    display_name="Malamar",
    searchable_by=["Malamar", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=34,
    set_code="SV065",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Inkay.Name",
    family_id=686,
    abilities=[
        Attack(
            title="Colluding Tentacles",
            game_text="Switch in 1 of your opponent's Benched Pokémon to the Active Spot. If you do, this attack does 120 damage to the new Active Pokémon. If you didn't play Xerosic's Machinations from your hand during this turn, this attack does nothing.",
            cost={PokemonTypes.DARKNESS: 1},
            effect=colluding_tentacles,
        ),
        Attack(
            title="Spinning Attack",
            game_text="",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
        ),
    ],
)
