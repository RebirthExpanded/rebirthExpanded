"""Lapras ex (SV07 32 -- JP SV7 019; English SCR/158, SCR/32, SVP/164). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers
from spirit.game.card_effects.pokemon import TeraRulePassive

from spirit.game.card_effects import attacks_common as ac
from spirit.game.card_effects import support_common as su

from spirit.game.session.effects import is_energy_card


card = PokemonCardDef(
    guid="34e88f86-b6e6-5469-8222-2a5ea5a54f5f",
    key="SV07",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Laprasex.Name",
    display_name="Lapras ex",
    searchable_by=["Lapras ex", "Basic", "ex", "Tera"],
    subtypes=["Basic", "ex", "Tera"],
    collector_number=32,
    set_code="SV07",
    regulation_mark="H",
    rarity=Rarities.RareHoloEX,
    hp=220,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    family_id=131,
    passive=TeraRulePassive(),
    abilities=[
        Attack(
            title="Power Splash",
            game_text="This attack does 40 damage for each Energy attached to this Pokémon.",
            cost={PokemonTypes.WATER: 1},
            damage=40,
            damage_operator="x",
            effect=ac.damage_per(ac.count_energy("self"), 40),
        ),
        Attack(
            title="Larimar Rain",
            game_text="Look at the top 20 cards of your deck and attach any number of Energy cards you find there to your Pokémon in any way you like. Shuffle the other cards back into your deck.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.PSYCHIC: 1, PokemonTypes.METAL: 1},
            effect=su.look_top_attach_energy(20, predicate=is_energy_card),
        ),
    ],
)
