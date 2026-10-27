"""Team Rocket's Nidoking ex (SV10 119 -- JP SV10 063; English DRI/119, DRI/216, DRI/233, SVP/217). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="1dd1e957-c5b9-5610-8de6-8ff86266a477",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsNidokingex.Name",
    display_name="Team Rocket's Nidoking ex",
    searchable_by=["Team Rocket's Nidoking ex", "Stage 2", "ex"],
    subtypes=["Stage 2", "ex"],
    collector_number=119,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.RareHoloEX,
    hp=330,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsNidorino.Name",
    family_id=32,
    abilities=[
        Attack(
            title="Tainted Horn",
            game_text="Your opponent's Active Pokémon is now Poisoned. During Pokémon Checkup, put 8 damage counters on that Pokémon instead of 1.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
            effect=ac.condition_attack(SpecialConditions.POISONED, counters=8),
        ),
        Attack(
            title="Kingly Impact",
            game_text="",
            cost={PokemonTypes.DARKNESS: 3, PokemonTypes.COLORLESS: 1},
            damage=240,
        ),
    ],
)
