"""Mienshao (SV4 97 -- JP SV4K 034; English PAR/200, PAR/97). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.data_utils import def_for, subtypes_for

from spirit.game.session.effects import is_pokemon_tool


def _tool_this_turn(ctx) -> bool:
    played = {aid for aid, _n, _t in ctx.session.turn_state.trainers_played}
    return any(is_pokemon_tool(c) and c.archetype_id in played for c in ctx.attacker.children)


card = PokemonCardDef(
    guid="706670af-908d-54fc-b731-cb93992f0d25",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mienshao.Name",
    display_name="Mienshao",
    searchable_by=["Mienshao", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=97,
    set_code="SV4",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Mienfoo.Name",
    family_id=619,
    abilities=[
        Attack(
            title="Three-Step Strike",
            game_text="Flip 3 coins. This attack does 20 damage for each heads.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=20,
            damage_operator="x",
            effect=ac.flip_damage(coins=3, per_heads=20),
        ),
        Attack(
            title="Whip Expert",
            game_text="If you attached a Pokémon Tool card from your hand to this Pokémon during this turn, this attack does 70 more damage.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator="+",
            effect=ac.bonus_if(_tool_this_turn, 70),
        ),
    ],
)
