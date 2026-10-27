"""Slither Wing (SV065 26 -- JP SV6a 026; English SFA/26). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.data_utils import def_for, subtypes_for


def _has_sub(card, sub) -> bool:
    return card is not None and sub in (subtypes_for(card.archetype_id) or [])


def _opp_future(ctx) -> bool:
    return any(_has_sub(p, "Future") for p in ctx.opponent_pokemon_in_play())


card = PokemonCardDef(
    guid="c6cc5651-4c4a-5d82-b233-b6c6f6d408cb",
    key="SV065",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.SlitherWing.Name",
    display_name="Slither Wing",
    searchable_by=["Slither Wing", "Basic", "Ancient"],
    subtypes=["Basic", "Ancient"],
    collector_number=26,
    set_code="SV065",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    hp=140,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=988,
    abilities=[
        Attack(
            title="Iron Smasher",
            game_text="If your opponent has any Future Pokémon in play, this attack does 120 more damage.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="+",
            effect=ac.bonus_if(_opp_future, 120),
        ),
        Attack(
            title="Smashing Wing",
            game_text="Discard 2 Energy from this Pokémon.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
            effect=ac.self_energy_discard_attack(count=2),
        ),
    ],
)
