"""Galvantula ex (SV07 51 -- JP SV7 033; English SCR/159, SCR/168, SCR/51). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers
from spirit.game.card_effects.pokemon import TeraRulePassive

from spirit.game.card_effects import attacks_common as ac
from spirit.game.data_utils import def_for, subtypes_for


def _ex_or_v(pokemon) -> bool:
    subs = subtypes_for(pokemon.archetype_id) or [] if pokemon is not None else []
    return "ex" in subs or any(s in subs for s in ("V", "VMAX", "VSTAR", "V-UNION"))


def _defender_ex_or_v(ctx) -> bool:
    return ctx.defender is not None and _ex_or_v(ctx.defender)

from spirit.game.session.effects import is_item_card


async def fulgurite(ctx):
    await ctx.deal_damage()
    pool = list(ctx.attached_energies(ctx.attacker))
    if pool:
        await ctx.discard_cards(pool)
    ctx.lock_plays(ctx.opponent_id, is_item_card)


card = PokemonCardDef(
    guid="0d20e4f8-79d0-57aa-b093-9039a0a55774",
    key="SV07",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Galvantulaex.Name",
    display_name="Galvantula ex",
    searchable_by=["Galvantula ex", "Stage 1", "ex", "Tera"],
    subtypes=["Stage 1", "ex", "Tera"],
    collector_number=51,
    set_code="SV07",
    regulation_mark="H",
    rarity=Rarities.RareHoloEX,
    hp=260,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Joltik.Name",
    family_id=595,
    passive=TeraRulePassive(),
    abilities=[
        Attack(
            title="Charged Web",
            game_text="If your opponent's Active Pokémon is a Pokémon ex or Pokémon V, this attack does 110 more damage.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=110,
            damage_operator="+",
            effect=ac.bonus_if(_defender_ex_or_v, 110),
        ),
        Attack(
            title="Fulgurite",
            game_text="Discard all Energy from this Pokémon. During your opponent's next turn, they can't play any Item cards from their hand.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.LIGHTNING: 1, PokemonTypes.FIGHTING: 1},
            damage=180,
            effect=fulgurite,
        ),
    ],
)
