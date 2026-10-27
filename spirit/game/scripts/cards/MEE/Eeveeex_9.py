"""Eevee ex (MEE 9 -- JP MEE 009; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su
from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="562ae163-7d0b-5820-9e79-8c6f718729af",
    key="MEE",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Eeveeex.Name",
    display_name="Eevee ex",
    searchable_by=["Eevee ex", "Basic", "ex"],
    subtypes=["Basic", "ex"],
    collector_number=9,
    set_code="MEE",
    regulation_mark="J",
    rarity=Rarities.RareHoloEX,
    hp=200,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=133,
    abilities=[
        Attack(
            title="Collect",
            game_text="Draw 3 cards.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=su.draw_attack(3),
        ),
        Attack(
            title="Brave Dash",
            game_text="Flip a coin. If tails, this Pokémon also does 30 damage to itself.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=200,
            effect=ac.flip_damage(tails_self_damage=30),
        ),
    ],
)
