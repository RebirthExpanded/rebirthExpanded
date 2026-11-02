"""Red's Pikachu (SMPJ 270 -- JP SMP 270; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="ab6902d4-f52a-549c-a99f-8cdc917f800d",
    key="SMPJ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RedsPikachu.Name",
    display_name="Red's Pikachu",
    searchable_by=["Red's Pikachu", "Basic"],
    subtypes=["Basic"],
    collector_number=270,
    set_code="SMPJ",
    regulation_mark="B",
    rarity=Rarities.RarePromo,
    hp=70,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=172,
    abilities=[
        Attack(
            title="Volt Tackle",
            game_text="This Pokémon also does 30 damage to itself.",
            cost={PokemonTypes.LIGHTNING: 3},
            damage=100,
            effect=ac.recoil_attack(30),
        ),
    ],
)
