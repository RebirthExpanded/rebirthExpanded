"""Team Rocket's Chingling (SV10 85 -- JP SV10 041; English DRI/85). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


async def _chiming_commotion(ctx):
    """Discard a random card from your opponent's hand."""
    await ac.discard_random_from_hand(ctx, ctx.opponent_id, count=1)


card = PokemonCardDef(
    guid="0d676b52-ead8-59c5-a42f-a88f105201a4",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsChingling.Name",
    display_name="Team Rocket's Chingling",
    searchable_by=["Team Rocket's Chingling", "Basic"],
    subtypes=["Basic"],
    collector_number=85,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=433,
    abilities=[
        Attack(
            title="Chiming Commotion",
            game_text="Discard a random card from your opponent's hand.",
            cost={},
            effect=_chiming_commotion,
        ),
    ],
)
