"""Ninetales ex (SV035 38 -- JP SV2a 038; English MEW/186, MEW/38). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac


def _same_hands(ctx) -> bool:
    return len(ctx.hand()) == len(ctx.hand(ctx.opponent_id))


card = PokemonCardDef(
    guid="f8fede85-028a-52be-9d89-944cf48481cd",
    key="SV035",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ninetalesex.Name",
    display_name="Ninetales ex",
    searchable_by=["Ninetales ex", "Stage 1", "ex"],
    subtypes=["Stage 1", "ex"],
    collector_number=38,
    set_code="SV035",
    regulation_mark="G",
    rarity=Rarities.RareHoloEX,
    hp=260,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Vulpix.Name",
    family_id=37,
    abilities=[
        Attack(
            title="Heat Wave",
            game_text="Your opponent's Active Pokémon is now Burned.",
            cost={PokemonTypes.FIRE: 1},
            damage=30,
            effect=ac.condition_attack(SpecialConditions.BURNED),
        ),
        Attack(
            title="Mirrored Flames",
            game_text="If you have the same number of cards in your hand as your opponent, this attack does 140 more damage.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=80,
            damage_operator="+",
            effect=ac.bonus_if(_same_hands, 140),
        ),
    ],
)
