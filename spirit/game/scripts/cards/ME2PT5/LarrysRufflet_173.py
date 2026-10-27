"""Larry's Rufflet (ME2PT5 173 -- JP MC 608; English ASC/173). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="fda2b8ca-2e32-5e10-a160-73f4057c20c5",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LarrysRufflet.Name",
    display_name="Larry's Rufflet",
    searchable_by=["Larry's Rufflet", "Basic"],
    subtypes=["Basic"],
    collector_number=173,
    set_code="ME2PT5",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=627,
    abilities=[
        Attack(
            title="Peck the Wound",
            game_text="If your opponent's Active Pokémon already has any damage counters on it, this attack does 80 more damage.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="+",
            effect=ac.bonus_if(ac.has_damage("defender"), 80),
        ),
    ],
)
