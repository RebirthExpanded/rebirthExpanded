"""Xatu (M7 27 -- JP M7 027/078 ネイティオ). Japanese art.

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
    guid="9db189fe-34b3-5081-9014-c681e0fee768",
    key="M7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Xatu.Name",
    display_name='Xatu',
    searchable_by=['Xatu', 'Stage 1', 'Xatu'],
    subtypes=['Stage 1'],
    collector_number=27,
    set_code="M7",
    regulation_mark="J",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Natu.Name",
    family_id=177,
    abilities=[
        Ability(
            title='Energy Leap',
            game_text="When you play this Pokémon from your hand to evolve 1 of your Pokémon during your turn, you may look at your opponent's hand and attach an Energy card you find there to 1 of their Pokémon.",
            trigger=Triggers.ON_EVOLVE,
            effect=m7.energy_leap,
        ),
        Attack(
            title='Psychic',
            game_text="This attack does 40 more damage for each Energy attached to your opponent's Active Pokémon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator='+',
            effect=ac.damage_per(ac.count_energy('defender'), 40, base=20),
        ),
    ],
)
