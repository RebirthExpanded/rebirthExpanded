"""Paldean Clodsire ex (SV09 94 -- JP SVM 074; English JTG/94). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac


async def _hit_then_lock(ctx):
    await ctx.deal_damage()
    ac.lock_all_attacks(ctx, ctx.attacker)


card = PokemonCardDef(
    guid="efb7a606-0e76-57cd-a440-b05c58e43dd2",
    key="SV09",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.PaldeanClodsireex.Name",
    display_name="Paldean Clodsire ex",
    searchable_by=["Paldean Clodsire ex", "Stage 1", "ex"],
    subtypes=["Stage 1", "ex"],
    collector_number=94,
    set_code="SV09",
    regulation_mark="H",
    rarity=Rarities.RareHoloEX,
    hp=280,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.PaldeanWooper.Name",
    family_id=194,
    abilities=[
        Attack(
            title="Poison Ring",
            game_text="Your opponent's Active Pokémon is now Poisoned. During your opponent's next turn, that Pokémon can't retreat.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
            effect=ac.condition_attack(SpecialConditions.POISONED, no_retreat=True),
        ),
        Attack(
            title="Giga Impact",
            game_text="During your next turn, this Pokémon can't attack.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=220,
            effect=_hit_then_lock,
        ),
    ],
)
