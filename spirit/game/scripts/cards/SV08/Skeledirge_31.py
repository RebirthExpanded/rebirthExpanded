"""Skeledirge (SV08 31 -- JP SV8 019; English SSP/31). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import passives_common as pc
from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="d18ea740-4116-570f-bf40-fdcc532a5c24",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Skeledirge.Name",
    display_name="Skeledirge",
    searchable_by=["Skeledirge", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=31,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.Rare,
    hp=180,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Crocalor.Name",
    family_id=909,
    abilities=[
        Ability(
            title="Unaware",
            game_text="Prevent all effects of attacks used by your opponent's Pokémon done to this Pokémon. (Damage is not an effect.)",
            passive=pc.attack_effect_shield_passive(),
        ),
        Attack(
            title="Torcherto",
            game_text="This attack does 20 more damage for each Benched Pokémon (both yours and your opponent's).",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
            damage_operator="+",
            effect=ac.damage_per(ac.count_bench("both"), 20, base=60),
        ),
    ],
)
