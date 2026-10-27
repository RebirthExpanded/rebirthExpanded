"""Tinkaton (ME1 98 -- JP M1L 050; English MEG/98). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


async def windup_swing(ctx):
    amount = max(0, 240 - 60 * ac.count_energy("defender", cards=True)(ctx))
    if amount:
        await ctx.deal_damage(amount)


card = PokemonCardDef(
    guid="85546190-a5d7-51cc-9558-01dc42cdb43e",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tinkaton.Name",
    display_name="Tinkaton",
    searchable_by=["Tinkaton", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=98,
    set_code="ME1",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=160,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Tinkatuff.Name",
    family_id=957,
    abilities=[
        Attack(
            title="Windup Swing",
            game_text="This attack does 60 less damage for each Energy attached to your opponent's Active Pokémon.",
            cost={PokemonTypes.METAL: 1},
            damage=240,
            damage_operator="-",
            effect=windup_swing,
        ),
    ],
)
