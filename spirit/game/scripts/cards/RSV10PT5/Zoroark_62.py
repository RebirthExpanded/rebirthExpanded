"""Zoroark (RSV10PT5 62 -- JP SV11W 059; English WHT/143, WHT/62). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES

from spirit.game.data_utils import def_for as _def_for


async def foul_play(ctx):
    defender = ctx.opponent_active()
    if defender is None:
        return
    candidates = [(defender, a) for a in getattr(_def_for(defender.archetype_id), "abilities", []) if isinstance(a, Attack)]
    if not candidates:
        return
    picked = await ctx.choose_attack_to_copy(candidates, "Choose an attack to copy")
    if picked is not None:
        await ctx.use_attack(picked[1])


card = PokemonCardDef(
    guid="feb076ff-eea9-5d37-bb5a-868af8cb8c65",
    key="RSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Zoroark.Name",
    display_name="Zoroark",
    searchable_by=["Zoroark", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=62,
    set_code="RSV10PT5",
    regulation_mark="I",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Zorua.Name",
    family_id=570,
    abilities=[
        Attack(
            title="Mind Jack",
            game_text="This attack does 30 damage for each of your opponent's Benched Pokémon.",
            cost={PokemonTypes.DARKNESS: 1},
            damage=30,
            damage_operator="x",
            effect=ac.damage_per(ac.count_bench("opponent"), 30),
        ),
        Attack(
            title="Foul Play",
            game_text="Choose 1 of your opponent's Active Pokémon's attacks and use it as this attack.",
            cost={PokemonTypes.COLORLESS: 3},
            effect=foul_play,
        ),
    ],
)
