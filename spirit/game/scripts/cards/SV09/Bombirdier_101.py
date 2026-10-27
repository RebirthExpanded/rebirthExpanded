"""Bombirdier (SV09 101 -- JP SVM 080; English JTG/101). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


async def drop_shot(ctx):
    pool = list(ctx.attached_energies(ctx.attacker))
    if pool:
        await ctx.discard_cards(pool)
    await ac.snipe_attack(120, pool="any")(ctx)


card = PokemonCardDef(
    guid="e22a67d2-8f91-5263-a495-8ef21974b107",
    key="SV09",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bombirdier.Name",
    display_name="Bombirdier",
    searchable_by=["Bombirdier", "Basic"],
    subtypes=["Basic"],
    collector_number=101,
    set_code="SV09",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=120,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=962,
    abilities=[
        Attack(
            title="Glide",
            game_text="",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
        Attack(
            title="Drop Shot",
            game_text="Discard all Energy from this Pokémon, and this attack does 120 damage to 1 of your opponent's Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            effect=drop_shot,
        ),
    ],
)
