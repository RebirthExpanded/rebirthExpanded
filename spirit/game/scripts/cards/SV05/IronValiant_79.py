"""Iron Valiant (SV05 79 -- JP SVHM 010; English TEF/79). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="d931baf3-dd97-5e2e-b776-6f1494736d73",
    key="SV05",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.IronValiant.Name",
    display_name="Iron Valiant",
    searchable_by=["Iron Valiant", "Basic", "Future"],
    subtypes=["Basic", "Future"],
    collector_number=79,
    set_code="SV05",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    family_id=1006,
    abilities=[
        Attack(
            title="Gemini Laser",
            game_text="This attack also does 20 damage to 1 of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=ac.snipe_attack(20, pool="bench", also_base=True),
        ),
        Attack(
            title="Zen Blade",
            game_text="During your next turn, this Pokémon can't use Zen Blade.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            locks_next_turn=True,
        ),
    ],
)
