"""Espeon ex (MF 14 -- JP MF 014; English 30C/70). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="4836771b-880e-5c33-b2b3-5e9b95aa102b",
    key="MF",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Espeonex.Name",
    display_name="Espeon ex",
    searchable_by=["Espeon ex", "Stage 1", "ex"],
    subtypes=["Stage 1", "ex"],
    collector_number=14,
    set_code="MF",
    regulation_mark="J",
    rarity=Rarities.RareHoloEX,
    hp=260,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    family_id=133,
    abilities=[
        Attack(
            title="Solar Beatdown",
            game_text="This attack does 30 damage for each of your Pokémon in play.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="x",
            effect=ac.damage_per(ac.count_in_play("mine"), 30),
        ),
    ],
)
