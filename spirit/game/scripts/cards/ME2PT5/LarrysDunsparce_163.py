"""Larry's Dunsparce (ME2PT5 163 -- JP MC 576; English ASC/163). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="db24209c-68a1-56a3-a869-d6c118c1aae3",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LarrysDunsparce.Name",
    display_name="Larry's Dunsparce",
    searchable_by=["Larry's Dunsparce", "Basic"],
    subtypes=["Basic"],
    collector_number=163,
    set_code="ME2PT5",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=206,
    abilities=[
        Attack(
            title="Rising Lunge",
            game_text="Flip a coin. If heads, this attack does 20 more damage.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="+",
            effect=ac.flip_bonus(20),
        ),
    ],
)
