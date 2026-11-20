"""Falinks (M7 47 -- JP M7 047/078 タイレーツ). Japanese art.

Provisional English name and text (no English release yet).
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers
from spirit.game.card_effects import attacks_common as ac
from spirit.game.card_effects import passives_common as pc
from spirit.game.card_effects import support_common as su
from spirit.game.card_effects import m7
from spirit.game.card_effects.pokemon import AttackTwicePassive
from spirit.game.session.effects import is_pokemon_card, is_supporter_card


card = PokemonCardDef(
    guid="40d44788-b8c5-5fa4-8275-b18b097ec43d",
    key="M7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Falinks.Name",
    display_name='Falinks',
    searchable_by=['Falinks', 'Basic', 'Falinks'],
    subtypes=['Basic'],
    collector_number=47,
    set_code="M7",
    regulation_mark="J",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=870,
    abilities=[
        Ability(
            title='United Formation',
            game_text='Once during your turn, if this Pokémon is in the Active Spot, you may search your deck for a Basic Fighting Energy card for each of your Benched Pokémon with "Falinks" in its name and attach 1 to each of them. Then, shuffle your deck.',
            activation=Activations.ONCE_PER_TURN,
            condition=m7.united_formation_condition,
            effect=m7.united_formation,
        ),
        Attack(
            title='Strong Attack',
            game_text='Discard an Energy from this Pokémon.',
            cost={PokemonTypes.FIGHTING: 3},
            damage=120,
            effect=ac.self_energy_discard_attack(count=1),
        ),
    ],
)
