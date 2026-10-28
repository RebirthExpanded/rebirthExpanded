"""Florges (SV1 93 -- JP SV1V 044; English SVI/93). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import passives_common as pc


card = PokemonCardDef(
    guid="bf419132-9998-56c7-93c1-31f5c7176810",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Florges.Name",
    display_name="Florges",
    searchable_by=["Florges", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=93,
    set_code="SV1",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=140,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Floette.Name",
    family_id=669,
    abilities=[
        Ability(
            title="Blooming Garden",
            game_text="Your Pokémon in play have no Weakness.",
            passive=pc.no_weakness_passive(protects="team"),
        ),
        Attack(
            title="Moonblast",
            game_text="During your opponent's next turn, the Defending Pokémon's attacks do 30 less damage (before applying Weakness and Resistance).",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=120,
            effect=pc.debuff_defender_attacks(30),
        ),
    ],
)
