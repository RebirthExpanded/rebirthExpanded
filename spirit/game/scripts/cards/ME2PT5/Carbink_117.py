"""Carbink (ME2PT5 117 -- JP MC 400; English ASC/117, ASC/242). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac

from spirit.game.session.passives import Passive


class DoubleTypePassive(Passive):
    """As long as this Pokemon is in play it is Fighting and Psychic type
    (an Ability: a lock leaves only the printed Fighting type)."""

    def modify_pokemon_types(self, types, pokemon, carrier):
        if pokemon is not carrier:
            return types
        both = [PokemonTypes.FIGHTING.value, PokemonTypes.PSYCHIC.value]
        return both + [t for t in types if t not in both]


def _two_or_fewer(ctx) -> bool:
    return ac.count_prizes_remaining("opponent")(ctx) <= 2


card = PokemonCardDef(
    guid="236a1fec-8108-5abd-b66b-58078f1627b6",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Carbink.Name",
    display_name="Carbink",
    searchable_by=["Carbink", "Basic"],
    subtypes=["Basic"],
    collector_number=117,
    set_code="ME2PT5",
    regulation_mark="J",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=703,
    abilities=[
        Ability(
            title="Double Type",
            game_text="As long as this Pokémon is in play, it is Fighting and Psychic type.",
            passive=DoubleTypePassive(),
        ),
        Attack(
            title="Counter Jewel",
            game_text="If your opponent has 2 or fewer Prize cards remaining, this attack does 100 more damage.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=70,
            damage_operator="+",
            effect=ac.bonus_if(_two_or_fewer, 100),
        ),
    ],
)
