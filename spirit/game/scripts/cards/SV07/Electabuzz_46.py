"""Electabuzz (SV07 46 -- JP SV7 028; English SCR/46). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su


card = PokemonCardDef(
    guid="bd2cfcc0-61f3-56f0-89f3-38aa79654aa1",
    key="SV07",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Electabuzz.Name",
    display_name="Electabuzz",
    searchable_by=["Electabuzz", "Basic"],
    subtypes=["Basic"],
    collector_number=46,
    set_code="SV07",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=239,
    abilities=[
        Attack(
            title="Collect",
            game_text="Draw a card.",
            cost={PokemonTypes.LIGHTNING: 1},
            effect=su.draw_attack(1),
        ),
        Attack(
            title="Magnum Punch",
            game_text="",
            cost={PokemonTypes.LIGHTNING: 2},
            damage=40,
        ),
    ],
)
