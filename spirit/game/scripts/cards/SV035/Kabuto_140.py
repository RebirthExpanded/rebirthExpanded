"""Kabuto (SV035 140 -- JP SV2a 140; English MEW/140). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="b07bd869-9c7b-565e-811e-7200660d2495",
    key="SV035",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kabuto.Name",
    display_name="Kabuto",
    searchable_by=["Kabuto", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=140,
    set_code="SV035",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.trainer.AntiqueDomeFossil.Name",
    family_id=140,
    abilities=[
        Attack(
            title="Double Scratch",
            game_text="Flip 2 coins. This attack does 70 damage for each heads.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=70,
            damage_operator="x",
            effect=ac.flip_damage(coins=2, per_heads=70),
        ),
    ],
)
