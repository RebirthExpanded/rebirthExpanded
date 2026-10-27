"""Larry's Braviary (ME2PT5 174 -- JP MC 609; English ASC/174). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="c13d26b3-57a2-5b0d-9102-7426c04145a6",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LarrysBraviary.Name",
    display_name="Larry's Braviary",
    searchable_by=["Larry's Braviary", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=174,
    set_code="ME2PT5",
    regulation_mark="J",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.LarrysRufflet.Name",
    family_id=627,
    abilities=[
        Attack(
            title="Clutch",
            game_text="During your opponent's next turn, the Defending Pokémon can't retreat.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=ac.condition_attack(no_retreat=True),
        ),
        Attack(
            title="Brave Bird",
            game_text="This Pokémon also does 30 damage to itself.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=120,
            effect=ac.recoil_attack(30),
        ),
    ],
)
