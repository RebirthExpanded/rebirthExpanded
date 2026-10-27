"""Camerupt (ME2PT5 28 -- JP M2a 023; English ASC/28). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="76b03606-736c-52af-8839-fe580773e383",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Camerupt.Name",
    display_name="Camerupt",
    searchable_by=["Camerupt", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=28,
    set_code="ME2PT5",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=140,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Numel.Name",
    family_id=322,
    abilities=[
        Attack(
            title="Roasting Burn",
            game_text="If your opponent's Active Pokémon isn't Burned, this attack does nothing.",
            cost={PokemonTypes.FIRE: 1},
            damage=110,
            effect=ac.bonus_if(ac.defender_has_condition(SpecialConditions.BURNED), 0, else_nothing=True),
        ),
        Attack(
            title="Power Stomp",
            game_text="Discard 2 Energy from this Pokémon.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 3},
            damage=170,
            effect=ac.self_energy_discard_attack(count=2),
        ),
    ],
)
