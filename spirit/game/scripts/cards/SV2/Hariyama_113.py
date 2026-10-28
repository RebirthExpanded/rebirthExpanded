"""Hariyama (SV2 113 -- JP SV1a 048; English PAL/113). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import passives_common as pc


card = PokemonCardDef(
    guid="9ce9cde3-0b19-515b-be6c-b184316bef9e",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hariyama.Name",
    display_name="Hariyama",
    searchable_by=["Hariyama", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=113,
    set_code="SV2",
    regulation_mark="G",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Makuhita.Name",
    family_id=296,
    abilities=[
        Ability(
            title="Arm Thrust Practice",
            game_text="All of your Pokémon take 10 less damage from attacks from your opponent's Pokémon (after applying Weakness and Resistance).",
            passive=pc.takes_less_passive(10, protects="team"),
        ),
        Attack(
            title="Rocket Slap",
            game_text="",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=120,
        ),
    ],
)
