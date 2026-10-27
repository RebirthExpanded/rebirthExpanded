"""Bouffalant ex (RSV10PT5 77 -- JP SV11W 075; English WHT/162, WHT/170, WHT/77). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import passives_common as pc
from spirit.game.card_effects import attacks_common as ac
from spirit.game.data_utils import def_for, subtypes_for


def _defender_ex(ctx) -> bool:
    return ctx.defender is not None and "ex" in (subtypes_for(ctx.defender.archetype_id) or [])


card = PokemonCardDef(
    guid="76dc2ba7-e667-5d98-bd19-87ee0175acdf",
    key="RSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bouffalantex.Name",
    display_name="Bouffalant ex",
    searchable_by=["Bouffalant ex", "Basic", "ex"],
    subtypes=["Basic", "ex"],
    collector_number=77,
    set_code="RSV10PT5",
    regulation_mark="I",
    rarity=Rarities.RareHoloEX,
    hp=220,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=626,
    abilities=[
        Ability(
            title="Bouffer",
            game_text="This Pokémon takes 30 less damage from attacks (after applying Weakness and Resistance).",
            passive=pc.takes_less_passive(30),
        ),
        Attack(
            title="Gold Breaker",
            game_text="If your opponent's Active Pokémon is a Pokémon ex, this attack does 100 more damage.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=100,
            damage_operator="+",
            effect=ac.bonus_if(_defender_ex, 100),
        ),
    ],
)
