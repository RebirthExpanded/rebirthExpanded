"""Tyranitar ex (SV085 64 -- JP SVM 078; English PRE/64). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


async def tyrannical_crush(ctx):
    await ctx.deal_damage()
    await ac.discard_random_from_hand(ctx, ctx.opponent_id, count=1)


card = PokemonCardDef(
    guid="9841d670-508a-56aa-9907-ff95e46e1f50",
    key="SV085",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tyranitarex.Name",
    display_name="Tyranitar ex",
    searchable_by=["Tyranitar ex", "Stage 2", "ex"],
    subtypes=["Stage 2", "ex"],
    collector_number=64,
    set_code="SV085",
    regulation_mark="H",
    rarity=Rarities.RareHoloEX,
    hp=340,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pupitar.Name",
    family_id=246,
    abilities=[
        Attack(
            title="Grind",
            game_text="This attack does 50 damage for each Energy attached to this Pokémon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=50,
            damage_operator="x",
            effect=ac.damage_per(ac.count_energy("self"), 50),
        ),
        Attack(
            title="Tyrannical Crush",
            game_text="Discard a random card from your opponent's hand.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=150,
            effect=tyrannical_crush,
        ),
    ],
)
