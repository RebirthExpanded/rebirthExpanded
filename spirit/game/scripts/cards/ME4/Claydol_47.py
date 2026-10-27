"""Claydol (ME4 47 -- JP M4 047; English CRI/47, CRI/92). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES

from spirit.game.attributes import PokemonStage


async def devolution_ray(ctx):
    await ctx.deal_damage()
    target = ctx.opponent_active()
    if target is None or target in ctx.knockouts or ctx.effects_blocked(target):
        return
    if target.get_attribute(AttrID.STAGE) in (PokemonStage.STAGE1.value, PokemonStage.STAGE2.value):
        await ctx.devolve_pokemon(target, steps=1, destination="hand")


card = PokemonCardDef(
    guid="46f54581-159d-572c-a317-30a6df7c2e02",
    key="ME4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Claydol.Name",
    display_name="Claydol",
    searchable_by=["Claydol", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=47,
    set_code="ME4",
    regulation_mark="J",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Baltoy.Name",
    family_id=343,
    abilities=[
        Attack(
            title="Devolution Ray",
            game_text="If your opponent's Active Pokémon is an evolved Pokémon, devolve it by putting the highest Stage Evolution card on it into your opponent's hand.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=50,
            effect=devolution_ray,
        ),
    ],
)
