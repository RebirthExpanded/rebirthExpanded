"""Lechonk (SV045 71 -- JP SV1S 067; English PAF/207, PAF/71, SVI/156). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="e4a5dc53-51b5-55fc-9712-636d42f1b640",
    key="SV045",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lechonk.Name",
    display_name="Lechonk",
    searchable_by=["Lechonk", "Basic"],
    subtypes=["Basic"],
    collector_number=71,
    set_code="SV045",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=915,
    abilities=[
        Attack(
            title="Whimsy Tackle",
            game_text="Flip a coin. If tails, this attack does nothing.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=70,
            effect=ac.flip_or_nothing(),
        ),
    ],
)
