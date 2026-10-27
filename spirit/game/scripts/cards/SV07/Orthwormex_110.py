"""Orthworm ex (SV07 110 -- JP SV7 074; English SCR/110, SCR/162). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card


def _payback_applies(ctx) -> bool:
    attacker = ctx.damaged_by
    return attacker is not None and attacker.owning_player_id != ctx.source.owning_player_id


async def pummeling_payback(ctx):
    n = sum(1 for e in ctx.source.children if is_energy_of_type(e, PokemonTypes.METAL))
    if n and ctx.damaged_by is not None:
        await ctx.deal_damage(20 * n, target=ctx.damaged_by, apply_modifiers=False, as_counters=True, is_attack=False)


card = PokemonCardDef(
    guid="b2948813-eed3-5c6b-ac0d-16b5dbd37e8a",
    key="SV07",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Orthwormex.Name",
    display_name="Orthworm ex",
    searchable_by=["Orthworm ex", "Basic", "ex"],
    subtypes=["Basic", "ex"],
    collector_number=110,
    set_code="SV07",
    regulation_mark="H",
    rarity=Rarities.RareHoloEX,
    hp=220,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    family_id=968,
    abilities=[
        Ability(
            title="Pummeling Payback",
            game_text="If this Pokémon is damaged by an attack from your opponent's Pokémon (even if this Pokémon is Knocked Out), put 2 damage counters on the Attacking Pokémon for each Metal Energy attached to this Pokémon.",
            trigger=Triggers.ON_DAMAGED_BY_ATTACK,
            trigger_applies=_payback_applies,
            effect=pummeling_payback,
        ),
        Attack(
            title="Rock Tomb",
            game_text="During your opponent's next turn, the Defending Pokémon can't retreat.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=150,
            effect=ac.condition_attack(no_retreat=True),
        ),
    ],
)
