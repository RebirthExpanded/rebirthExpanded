"""Regirock ex (SV10 101 -- JP SV10 115; English ASC/107, DRI/101, DRI/214). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su
from spirit.game.card_effects import attacks_common as ac
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card


def _basic_fighting(card):
    return is_basic_energy_card(card) and is_energy_of_type(card, PokemonTypes.FIGHTING)

from spirit.game.session.effects import is_stage2_pokemon


card = PokemonCardDef(
    guid="baad1cd4-9d76-5964-9508-57f79941aba1",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Regirockex.Name",
    display_name="Regirock ex",
    searchable_by=["Regirock ex", "Basic", "ex"],
    subtypes=["Basic", "ex"],
    collector_number=101,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.RareHoloEX,
    hp=230,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    family_id=377,
    abilities=[
        Attack(
            title="Regi Charge",
            game_text="Attach up to 2 Basic Fighting Energy cards from your discard pile to this Pokémon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=su.attach_from_discard(_basic_fighting, count=2, target="self", minimum=0, prompt="Attach up to 2 Basic Fighting Energy cards from your discard pile to this Pokémon."),
        ),
        Attack(
            title="Giant Rock",
            game_text="If your opponent's Active Pokémon is a Stage 2 Pokémon, this attack does 140 more damage.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 3},
            damage=140,
            damage_operator="+",
            effect=ac.bonus_if(ac.active_is(is_stage2_pokemon), 140),
        ),
    ],
)
