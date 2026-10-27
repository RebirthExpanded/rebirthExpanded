"""Carkol (ME2PT5 119 -- JP M2a 096; English ASC/119). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import passives_common as pc


card = PokemonCardDef(
    guid="e63933f1-bccd-584f-9558-a88a628a7feb",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Carkol.Name",
    display_name="Carkol",
    searchable_by=["Carkol", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=119,
    set_code="ME2PT5",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=110,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Rolycoly.Name",
    family_id=837,
    abilities=[
        Attack(
            title="Guard Press",
            game_text="During your opponent's next turn, this Pokémon takes 20 less damage from attacks (after applying Weakness and Resistance).",
            cost={PokemonTypes.FIGHTING: 1},
            damage=20,
            effect=pc.protect_next_turn(reduce=20),
        ),
        Attack(
            title="Power Gem",
            game_text="",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
        ),
    ],
)
