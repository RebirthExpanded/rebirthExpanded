"""Garganacl ex (SV07 89 -- JP SVP 115; English SCR/89). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import passives_common as pc


card = PokemonCardDef(
    guid="dd6439ea-f7de-51cb-bd1b-149b75a61951",
    key="SV07",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Garganaclex.Name",
    display_name="Garganacl ex",
    searchable_by=["Garganacl ex", "Stage 2", "ex"],
    subtypes=["Stage 2", "ex"],
    collector_number=89,
    set_code="SV07",
    regulation_mark="G",
    rarity=Rarities.RareHoloEX,
    hp=340,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Naclstack.Name",
    family_id=932,
    abilities=[
        Ability(
            title="Salty Body",
            game_text="This Pokémon can't be affected by any Special Conditions.",
            passive=pc.condition_immunity_passive(),
        ),
        Attack(
            title="Block Hammer",
            game_text="During your opponent's next turn, this Pokémon takes 60 less damage from attacks (after applying Weakness and Resistance).",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=170,
            effect=pc.protect_next_turn(reduce=60),
        ),
    ],
)
