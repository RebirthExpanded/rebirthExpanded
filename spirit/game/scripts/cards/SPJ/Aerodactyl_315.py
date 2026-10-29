"""Aerodactyl (SPJ 315 -- JP SP 315; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="f0b5c33f-7271-5a47-848c-cf59ad8c4b1a",
    key="SPJ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Aerodactyl.Name",
    display_name="Aerodactyl",
    searchable_by=["Aerodactyl", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=315,
    set_code="SPJ",
    regulation_mark="F",
    rarity=Rarities.RarePromo,
    hp=130,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.trainer.AntiqueOldAmber.Name",
    family_id=142,
    abilities=[
        Attack(
            title="Linear Attack",
            game_text="This attack does 50 damage to 1 of your opponent's Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.COLORLESS: 1},
            effect=ac.snipe_attack(50, pool="any"),
        ),
        Attack(
            title="Jet Dive",
            game_text="Discard an Energy from this Pokémon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=120,
            effect=ac.self_energy_discard_attack(1),
        ),
    ],
)
