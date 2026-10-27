"""Mamoswine (ME2 25 -- JP M2 025; English PFL/25). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


async def wreck(ctx):
    if ctx.stadium_in_play() is not None:
        await ctx.deal_damage(240)
        await ctx.discard_stadium()
    else:
        await ctx.deal_damage(120)


card = PokemonCardDef(
    guid="c19163bd-f10f-5cf4-8103-cfdfe60d2983",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mamoswine.Name",
    display_name="Mamoswine",
    searchable_by=["Mamoswine", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=25,
    set_code="ME2",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=180,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Piloswine.Name",
    family_id=220,
    abilities=[
        Attack(
            title="Wreck",
            game_text="If a Stadium is in play, this attack does 120 more damage. Then, discard that Stadium.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=120,
            damage_operator="+",
            effect=wreck,
        ),
        Attack(
            title="Blizzard Edge",
            game_text="Discard 2 Energy from this Pokémon.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 3},
            damage=200,
            effect=ac.self_energy_discard_attack(count=2),
        ),
    ],
)
