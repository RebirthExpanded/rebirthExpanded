"""Kangaskhan ex (SVP 55 -- JP SV2a 115; English MEW/115, MEW/190, SVP/55). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su
from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="2cd5f566-ba4a-58bb-ac99-d32abe35cd37",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kangaskhanex.Name",
    display_name="Kangaskhan ex",
    searchable_by=["Kangaskhan ex", "Basic", "ex"],
    subtypes=["Basic", "ex"],
    collector_number=55,
    set_code="SVP",
    regulation_mark="G",
    rarity=Rarities.RarePromo,
    hp=230,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=115,
    abilities=[
        Attack(
            title="Triple Draw",
            game_text="Draw 3 cards.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=su.draw_attack(3),
        ),
        Attack(
            title="Incessant Punching",
            game_text="Flip 4 coins. This attack does 100 damage for each heads.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=100,
            damage_operator="x",
            effect=ac.flip_damage(coins=4, per_heads=100),
        ),
    ],
)
