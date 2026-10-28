"""Slowbro (SV035 80 -- JP SV2a 080; English MEW/80). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac


def _evolved_this_turn(ctx) -> bool:
    state = ctx.session.turn_state
    return state.entered_play_turn.get(ctx.attacker.entity_id) == state.turn_number


async def laid_back_tackle(ctx):
    if not _evolved_this_turn(ctx):
        await ctx.deal_damage()


card = PokemonCardDef(
    guid="076b40c8-e931-530f-a4ff-06608cd7fa86",
    key="SV035",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Slowbro.Name",
    display_name="Slowbro",
    searchable_by=["Slowbro", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=80,
    set_code="SV035",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Slowpoke.Name",
    family_id=79,
    abilities=[
        Attack(
            title="Big Yawn",
            game_text="Both Active Pokémon are now Asleep.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=ac.condition_attack(SpecialConditions.ASLEEP, both_actives=True),
        ),
        Attack(
            title="Laid-Back Tackle",
            game_text="If this Pokémon evolved during this turn, this attack does nothing.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=160,
            effect=laid_back_tackle,
        ),
    ],
)
