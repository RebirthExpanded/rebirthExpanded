"""Clefable (SV035 36 -- JP SV2a 036; English MEW/36). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su


async def more_moon(ctx):
    d = ctx.opponent_active()
    await ctx.deal_damage()
    if d is not None and d in ctx.knockouts:
        ctx.extra_prizes += 1


card = PokemonCardDef(
    guid="3dd9f2e0-4349-59eb-896a-b65f1ab5be59",
    key="SV035",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Clefable.Name",
    display_name="Clefable",
    searchable_by=["Clefable", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=36,
    set_code="SV035",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Clefairy.Name",
    family_id=173,
    abilities=[
        Attack(
            title="Follow Me",
            game_text="Switch in 1 of your opponent's Benched Pokémon to the Active Spot.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=su.gust_attack(),
        ),
        Attack(
            title="More Moon",
            game_text="If your opponent's Pokémon is Knocked Out by damage from this attack, take 1 more Prize card.",
            cost={PokemonTypes.PSYCHIC: 3},
            damage=50,
            effect=more_moon,
        ),
    ],
)
