"""Landorus (ZSV10PT5 53 -- JP SV11B 056; English BLK/131, BLK/53). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su
from spirit.game.card_effects import attacks_common as ac
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card


def _basic_fighting(card):
    return is_basic_energy_card(card) and is_energy_of_type(card, PokemonTypes.FIGHTING)


card = PokemonCardDef(
    guid="e8fabecf-d333-5fbd-a887-79ae7765c828",
    key="ZSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Landorus.Name",
    display_name="Landorus",
    searchable_by=["Landorus", "Basic"],
    subtypes=["Basic"],
    collector_number=53,
    set_code="ZSV10PT5",
    regulation_mark="I",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=645,
    abilities=[
        Attack(
            title="Abundant Harvest",
            game_text="Attach a Basic Fighting Energy card from your discard pile to this Pokémon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=su.attach_from_discard(_basic_fighting, count=1, target="self", minimum=0, prompt="Attach a Basic Fighting Energy card from your discard pile to this Pokémon."),
        ),
        Attack(
            title="Earthquake",
            game_text="This attack also does 10 damage to each of your Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=110,
            effect=ac.spread_damage(10, side="mine", also_base=True),
        ),
    ],
)
