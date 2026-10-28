"""Gourgeist (SV4 78 -- JP SV4M 030; English PAR/78). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


def _ko_by_opponent(ctx) -> bool:
    attacker = getattr(ctx, "ko_attacker", None)
    return (bool(getattr(ctx, "ko_from_attack", False)) and attacker is not None
            and attacker.owning_player_id != ctx.source.owning_player_id)


async def startling_pumpkin(ctx):
    await ac.discard_random_from_hand(ctx, ctx.opponent_id, count=2)


card = PokemonCardDef(
    guid="9f93d606-4d0c-572e-9ab1-ce796e78111b",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gourgeist.Name",
    display_name="Gourgeist",
    searchable_by=["Gourgeist", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=78,
    set_code="SV4",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pumpkaboo.Name",
    family_id=710,
    abilities=[
        Ability(
            title="Startling Pumpkin",
            game_text="If this Pokémon is Knocked Out by damage from an attack from your opponent's Pokémon, discard 2 random cards from your opponent's hand.",
            trigger=Triggers.ON_KNOCKED_OUT,
            trigger_applies=_ko_by_opponent,
            effect=startling_pumpkin,
        ),
        Attack(
            title="Shadow Bind",
            game_text="During your opponent's next turn, the Defending Pokémon can't retreat.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
            effect=ac.condition_attack(no_retreat=True),
        ),
    ],
)
