"""Scolipede (SV06 117 -- JP SV6 070; English TWM/117). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES


async def dastardly_jab(ctx):
    d = ctx.opponent_active()
    if d is None:
        return
    hp = d.get_attribute(AttrID.HP, 0) or 0
    if hp > 10:
        await ctx.deal_damage(hp - 10, target=d, apply_modifiers=False, as_counters=True)


card = PokemonCardDef(
    guid="0f86e855-f7d0-502d-b7f8-f0d0daf79f73",
    key="SV06",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Scolipede.Name",
    display_name="Scolipede",
    searchable_by=["Scolipede", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=117,
    set_code="SV06",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    hp=170,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Whirlipede.Name",
    family_id=543,
    abilities=[
        Attack(
            title="Dastardly Jab",
            game_text="Put damage counters on your opponent's Active Pokémon until its remaining HP is 10.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            effect=dastardly_jab,
        ),
        Attack(
            title="Sludge Bomb",
            game_text="",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=160,
        ),
    ],
)
