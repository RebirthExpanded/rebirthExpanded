"""Okidogi (ME2PT5 122 -- JP M2a 098; English ASC/122). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


def _taken_last_turn(ctx) -> int:
    return ctx.session.turn_state.prizes_taken_last_turn.get(ctx.opponent_id, 0)


card = PokemonCardDef(
    guid="97c10ad3-ff1f-5b4d-b6f5-a8e77005f860",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Okidogi.Name",
    display_name="Okidogi",
    searchable_by=["Okidogi", "Basic"],
    subtypes=["Basic"],
    collector_number=122,
    set_code="ME2PT5",
    regulation_mark="I",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=0,
    abilities=[
        Attack(
            title="Light Punch",
            game_text="",
            cost={PokemonTypes.FIGHTING: 1},
            damage=20,
        ),
        Attack(
            title="Settle the Score",
            game_text="This attack does 60 more damage for each Prize card your opponent took during their last turn.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
            damage_operator="+",
            effect=ac.damage_per(_taken_last_turn, 60, base=80),
        ),
    ],
)
