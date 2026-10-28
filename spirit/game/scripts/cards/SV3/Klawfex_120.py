"""Klawf ex (SV3 120 -- JP SVP 027; English OBF/120). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import passives_common as pc
from spirit.game.card_effects import attacks_common as ac


async def counterattacking_pincer(ctx):
    attacker = ctx.damaged_by
    if attacker is not None and ctx.attached_energies(attacker) and not ctx.effects_blocked(attacker):
        await ctx.discard_energy_from(attacker, 1, minimum=1, prompt="Choose an Energy to discard from the Attacking Pokémon")


card = PokemonCardDef(
    guid="44038125-c7fb-5296-89c9-9cd8812032f6",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Klawfex.Name",
    display_name="Klawf ex",
    searchable_by=["Klawf ex", "Basic", "ex"],
    subtypes=["Basic", "ex"],
    collector_number=120,
    set_code="SV3",
    regulation_mark="G",
    rarity=Rarities.RareHoloEX,
    hp=220,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    family_id=950,
    abilities=[
        Ability(
            title="Counterattacking Pincer",
            game_text="If this Pokémon is in the Active Spot and is damaged by an attack from your opponent's Pokémon (even if this Pokémon is Knocked Out), discard an Energy from the Attacking Pokémon.",
            trigger=Triggers.ON_DAMAGED_BY_ATTACK,
            trigger_applies=pc.hit_in_active_by_opponent,
            effect=counterattacking_pincer,
        ),
        Attack(
            title="Falling Press",
            game_text="Flip a coin. If heads, this attack does 80 more damage.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
            damage_operator="+",
            effect=ac.flip_bonus(80),
        ),
    ],
)
