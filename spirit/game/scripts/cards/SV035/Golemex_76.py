"""Golem ex (SV035 76 -- JP SV2a 076; English MEW/189, MEW/76). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import passives_common as pc


async def rock_blaster(ctx):
    await ctx.deal_damage(ignore_resistance=True)


card = PokemonCardDef(
    guid="520e4966-e00b-5d62-a00e-cfb426efa671",
    key="SV035",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Golemex.Name",
    display_name="Golem ex",
    searchable_by=["Golem ex", "Stage 2", "ex"],
    subtypes=["Stage 2", "ex"],
    collector_number=76,
    set_code="SV035",
    regulation_mark="G",
    rarity=Rarities.RareHoloEX,
    hp=330,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Graveler.Name",
    family_id=74,
    abilities=[
        Attack(
            title="Dynamic Roll",
            game_text="During your next turn, attacks used by this Pokémon do 120 more damage to your opponent's Active Pokémon (before applying Weakness and Resistance).",
            cost={PokemonTypes.FIGHTING: 1},
            damage=50,
            effect=pc.boost_own_next_turn(120),
        ),
        Attack(
            title="Rock Blaster",
            game_text="This attack's damage isn't affected by Resistance.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=180,
            effect=rock_blaster,
        ),
    ],
)
