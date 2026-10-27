"""Drifblim (SV07 61 -- JP SV7 041; English SCR/61, SVP/135). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES


def _drifs(ctx):
    return [p for p in ctx.my_pokemon_in_play()
            if p.get_attribute(AttrID.EVOLUTION_LOGIC_NAME) in ("Drifloon", "Drifblim")]


async def everyone_explode_now(ctx):
    crew = _drifs(ctx)
    await ctx.deal_damage(50 * len(crew))
    for p in crew:
        await ctx.deal_damage(30, target=p, apply_modifiers=False)


card = PokemonCardDef(
    guid="d200bf77-3874-5180-99e7-213eb210eadc",
    key="SV07",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Drifblim.Name",
    display_name="Drifblim",
    searchable_by=["Drifblim", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=61,
    set_code="SV07",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Drifloon.Name",
    family_id=425,
    abilities=[
        Attack(
            title="Everyone Explode Now",
            game_text="This attack does 50 damage for each of your Drifloon and Drifblim in play. This attack also does 30 damage to each of your Drifloon and Drifblim. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=50,
            damage_operator="x",
            effect=everyone_explode_now,
        ),
    ],
)
