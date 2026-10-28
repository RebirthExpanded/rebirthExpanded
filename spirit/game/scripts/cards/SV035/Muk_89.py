"""Muk (SV035 89 -- JP SV2a 089; English MEW/89). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import passives_common as pc


async def sticky_jail(ctx):
    await ctx.deal_damage()
    await pc.apply_defender_attack_cost_raise(ctx, 1)
    await pc.apply_defender_retreat_cost_raise(ctx, 1)


card = PokemonCardDef(
    guid="d30e8ad6-3f14-5c8e-ab68-f54fd63baa67",
    key="SV035",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Muk.Name",
    display_name="Muk",
    searchable_by=["Muk", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=89,
    set_code="SV035",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=150,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Grimer.Name",
    family_id=88,
    abilities=[
        Attack(
            title="Sticky Jail",
            game_text="During your opponent's next turn, attacks used by the Defending Pokémon cost Colorless more, and its Retreat Cost is Colorless more.",
            cost={PokemonTypes.DARKNESS: 1},
            damage=30,
            effect=sticky_jail,
        ),
        Attack(
            title="Sludge Bomb",
            game_text="",
            cost={PokemonTypes.DARKNESS: 3, PokemonTypes.COLORLESS: 1},
            damage=180,
        ),
    ],
)
