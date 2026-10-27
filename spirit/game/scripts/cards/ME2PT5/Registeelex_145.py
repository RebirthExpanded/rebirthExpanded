"""Registeel ex (ME2PT5 145 -- JP MC 499; English ASC/145). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import passives_common as pc
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card
from spirit.game.card_effects import support_common as su


def _basic_metal(card):
    return is_basic_energy_card(card) and is_energy_of_type(card, PokemonTypes.METAL)


regi_charge = su.attach_from_discard(
    _basic_metal, count=2, target="self", minimum=0,
    prompt="Attach up to 2 Basic Metal Energy cards from your discard pile to this Pokémon.")


card = PokemonCardDef(
    guid="b5426536-f9e1-5ae3-ac6e-d91e87f33f84",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Registeelex.Name",
    display_name="Registeel ex",
    searchable_by=["Registeel ex", "Basic", "ex"],
    subtypes=["Basic", "ex"],
    collector_number=145,
    set_code="ME2PT5",
    regulation_mark="J",
    rarity=Rarities.RareHoloEX,
    hp=230,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    family_id=379,
    abilities=[
        Attack(
            title="Regi Charge",
            game_text="Attach up to 2 Basic Metal Energy cards from your discard pile to this Pokémon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=regi_charge,
        ),
        Attack(
            title="Protecting Steel",
            game_text="During your opponent's next turn, this Pokémon takes 50 less damage from attacks (after applying Weakness and Resistance).",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 3},
            damage=140,
            effect=pc.protect_next_turn(reduce=50),
        ),
    ],
)
