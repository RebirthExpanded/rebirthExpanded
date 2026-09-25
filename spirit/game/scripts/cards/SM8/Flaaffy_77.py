"""Flaaffy (SM - Lost Thunder 77/214 -- JP SM8 035/095).

Stage 1 Lightning Pokemon, evolves from Mareep. HP 80, weakness Fighting x2,
resistance Metal -20, retreat 1.

  Signal Beam  [LL] 40  Your opponent's Active Pokemon is now Confused.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.data_utils import Attack, PokemonCardDef


card = PokemonCardDef(
    guid="879b329f-40b9-5eb0-9ef2-af7cf9043d6c",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Flaaffy.Name",
    display_name="Flaaffy",
    searchable_by=['Flaaffy', 'Stage 1', 'Flaaffy'],
    subtypes=['Stage 1'],
    collector_number=77,
    set_code="SM8",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Mareep.Name",
    family_id=179,
    abilities=[
        Attack(title="Signal Beam", game_text="Your opponent's Active Pokémon is now Confused.",
               cost={PokemonTypes.LIGHTNING: 2}, damage=40,
               effect=condition_attack(SpecialConditions.CONFUSED)),
    ],
)
