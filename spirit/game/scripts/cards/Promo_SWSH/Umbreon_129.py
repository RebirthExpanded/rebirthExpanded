"""Umbreon (Promo_SWSH 129 -- JP SP 161; English SP/129). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.attributes import SpecialConditions
from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES



async def _blindside(ctx):
    pool = [p for p in ctx.opponent_pokemon_in_play()
            if p.get_attribute(AttrID.HP, 0) < ctx.max_hp(p)]
    if not pool:
        return
    target = await ctx.choose_pokemon(pool, "Choose 1 of your opponent's Pokémon that has damage counters on it.")
    if target is not None:
        await ctx.deal_damage(60, target=target)


card = PokemonCardDef(
    guid="f8b25617-b598-5794-85d1-d7a5c754843c",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Umbreon.Name",
    display_name="Umbreon",
    searchable_by=["Umbreon", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=129,
    set_code="Promo_SWSH",
    regulation_mark="E",
    rarity=Rarities.RarePromo,
    hp=110,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    family_id=133,
    abilities=[
        Attack(
            title="Blindside",
            game_text="This attack does 60 damage to 1 of your opponent's Pokémon that has any damage counters on it. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.DARKNESS: 1},
            effect=_blindside,
        ),
        Attack(
            title="Moon Mirage",
            game_text="Your opponent's Active Pokémon is now Confused.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            effect=ac.condition_attack(SpecialConditions.CONFUSED),
        ),
    ],
)
