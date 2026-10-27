"""Falinks (SV07 88 -- JP SV7 060; English SCR/88). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su
from spirit.game.card_effects import attacks_common as ac


def _used_last_turn(title):
    def cond(ctx) -> bool:
        history = ctx.board.turn_state.attacks_prev_turn_by_player.get(ctx.player_id) or []
        return any(used_id == ctx.attacker.entity_id and t == title for used_id, _arch, t in history)
    return cond


card = PokemonCardDef(
    guid="5b59788a-9bff-50ed-bf2a-3fdfa9febe33",
    key="SV07",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Falinks.Name",
    display_name="Falinks",
    searchable_by=["Falinks", "Basic"],
    subtypes=["Basic"],
    collector_number=88,
    set_code="SV07",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=110,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=870,
    abilities=[
        Attack(
            title="Form Ranks",
            game_text="Search your deck for up to 2 Basic Pokémon and put them onto your Bench. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=su.search_to_bench(count=2, prompt="Choose up to 2 Basic Pokémon to put onto your Bench."),
        ),
        Attack(
            title="All-Out Attack",
            game_text="If this Pokémon used Form Ranks during your last turn, this attack does 90 more damage.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="+",
            effect=ac.bonus_if(_used_last_turn("Form Ranks"), 90),
        ),
    ],
)
