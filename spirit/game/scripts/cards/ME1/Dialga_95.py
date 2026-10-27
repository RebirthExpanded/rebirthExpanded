"""Dialga (ME1 95 -- JP M1L 047; English MEG/95). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

async def chrono_burst(ctx):
    pool = list(ctx.attached_energies(ctx.attacker))
    if pool and await ctx.ask_yes_no("Shuffle all Energy attached to this Pokémon into your deck for 80 more damage?"):
        await ctx.shuffle_into_deck(pool, ctx.player_id)
        await ctx.deal_damage(160)
    else:
        await ctx.deal_damage(80)


card = PokemonCardDef(
    guid="7996c45a-9c6b-5fa5-a00e-c1e559dd6e48",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dialga.Name",
    display_name="Dialga",
    searchable_by=["Dialga", "Basic"],
    subtypes=["Basic"],
    collector_number=95,
    set_code="ME1",
    regulation_mark="I",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    family_id=483,
    abilities=[
        Attack(
            title="Beam",
            game_text="",
            cost={PokemonTypes.METAL: 1},
            damage=30,
        ),
        Attack(
            title="Chrono Burst",
            game_text="You may shuffle all Energy attached to this Pokémon into your deck and have this attack do 80 more damage.",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
            damage_operator="+",
            effect=chrono_burst,
        ),
    ],
)
