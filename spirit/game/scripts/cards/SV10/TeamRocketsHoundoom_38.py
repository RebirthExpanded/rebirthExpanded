"""Team Rocket's Houndoom (SV10 38 -- JP SV10 017; English DRI/191, DRI/38). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="7b8b3c0f-99ad-5d62-8b88-e6ff69962c8f",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsHoundoom.Name",
    display_name="Team Rocket's Houndoom",
    searchable_by=["Team Rocket's Houndoom", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=38,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsHoundour.Name",
    family_id=228,
    abilities=[
        Attack(
            title="Cruel Coal",
            game_text="Your opponent's Active Pokémon is now Burned and Confused.",
            cost={PokemonTypes.FIRE: 1},
            effect=ac.condition_attack(SpecialConditions.BURNED, SpecialConditions.CONFUSED),
        ),
        Attack(
            title="Scorching Fire",
            game_text="Discard an Energy from this Pokémon.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=ac.self_energy_discard_attack(count=1),
        ),
    ],
)
