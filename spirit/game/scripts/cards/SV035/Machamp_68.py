"""Machamp (SV035 68 -- JP SV2a 068; English MEW/68). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import passives_common as pc
from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="d463bec9-6392-50ab-b3ef-be4459d8f98c",
    key="SV035",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Machamp.Name",
    display_name="Machamp",
    searchable_by=["Machamp", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=68,
    set_code="SV035",
    regulation_mark="G",
    rarity=Rarities.Rare,
    hp=180,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Machoke.Name",
    family_id=66,
    abilities=[
        Ability(
            title="Guts",
            game_text="If this Pokémon would be Knocked Out by damage from an attack, flip a coin. If heads, this Pokémon is not Knocked Out, and its remaining HP becomes 10.",
            passive=pc.guts_survive_passive(hp_floor=10, title="Guts", flip=True),
        ),
        Attack(
            title="Mountain Chopping",
            game_text="Discard the top 2 cards of your opponent's deck.",
            cost={PokemonTypes.FIGHTING: 2},
            damage=100,
            effect=ac.mill_attack(2),
        ),
    ],
)
