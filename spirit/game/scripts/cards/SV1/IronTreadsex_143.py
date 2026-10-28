"""Iron Treads ex (SV1 143 -- JP SV1V 058; English SVI/143, SVI/233, SVI/248). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.card_effects import support_common as su


card = PokemonCardDef(
    guid="2ab0fffc-1f09-55a5-aaa9-1de514049435",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.IronTreadsex.Name",
    display_name="Iron Treads ex",
    searchable_by=["Iron Treads ex", "Basic", "ex"],
    subtypes=["Basic", "ex"],
    collector_number=143,
    set_code="SV1",
    regulation_mark="G",
    rarity=Rarities.RareHoloEX,
    hp=220,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    family_id=990,
    abilities=[
        Attack(
            title="Triple Laser",
            game_text="This attack does 30 damage to 3 of your opponent's Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.COLORLESS: 3},
            effect=ac.snipe_attack(30, pool="any", count=3),
        ),
        Attack(
            title="Cybernetic Wheels",
            game_text="Switch this Pokémon with 1 of your Benched Pokémon.",
            cost={PokemonTypes.METAL: 3, PokemonTypes.COLORLESS: 1},
            damage=160,
            effect=su.switch_self_attack(),
        ),
    ],
)
