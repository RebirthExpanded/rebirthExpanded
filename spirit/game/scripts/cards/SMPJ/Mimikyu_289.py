"""Mimikyu (SMPJ 289 -- JP SMP 289; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.attributes import SpecialConditions


card = PokemonCardDef(
    guid="66c80151-7f84-5bf0-9917-fdc330e74eb2",
    key="SMPJ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mimikyu.Name",
    display_name="Mimikyu",
    searchable_by=["Mimikyu", "Basic"],
    subtypes=["Basic"],
    collector_number=289,
    set_code="SMPJ",
    regulation_mark="B",
    rarity=Rarities.RarePromo,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    family_id=778,
    abilities=[
        Attack(
            title="Scream",
            game_text="Both Active Pokémon are now Confused.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=ac.condition_attack(SpecialConditions.CONFUSED, both_actives=True),
        ),
    ],
)
