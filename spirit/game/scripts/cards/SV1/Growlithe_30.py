"""Growlithe (SV1 30 -- JP SVAL 001; English SVI/30). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="f448b113-1c77-591b-bf53-951eaa30f942",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Growlithe.Name",
    display_name="Growlithe",
    searchable_by=["Growlithe", "Basic"],
    subtypes=["Basic"],
    collector_number=30,
    set_code="SV1",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=58,
    abilities=[
        Attack(
            title="Relentless Flames",
            game_text="Flip a coin until you get tails. This attack does 30 damage for each heads.",
            cost={PokemonTypes.FIRE: 1},
            damage=30,
            damage_operator="x",
            effect=ac.flip_damage(until_tails=True, per_heads=30),
        ),
    ],
)
