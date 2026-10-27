"""Zarude (SV08 11 -- JP SV7a 005; English SSP/11). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su


async def jungle_whip(ctx):
    pool = list(ctx.attached_energies(ctx.attacker))
    if pool and await ctx.ask_yes_no("Put all Energy attached to this Pokémon into your hand for 80 more damage?"):
        await ctx.put_in_hand(pool, reveal=False)
        await ctx.deal_damage(160)
    else:
        await ctx.deal_damage(80)


card = PokemonCardDef(
    guid="50ff54a1-c4fa-5b90-84bf-7d4d8e377bf4",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Zarude.Name",
    display_name="Zarude",
    searchable_by=["Zarude", "Basic"],
    subtypes=["Basic"],
    collector_number=11,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=893,
    abilities=[
        Attack(
            title="Leaf Drain",
            game_text="Heal 20 damage from this Pokémon.",
            cost={PokemonTypes.GRASS: 1},
            damage=20,
            effect=su.heal_attack(20),
        ),
        Attack(
            title="Jungle Whip",
            game_text="You may put all Energy attached to this Pokémon into your hand to have this attack do 80 more damage.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
            damage_operator="+",
            effect=jungle_whip,
        ),
    ],
)
