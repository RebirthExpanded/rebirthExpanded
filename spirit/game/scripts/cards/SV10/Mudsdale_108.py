"""Mudsdale (SV10 108 -- JP SV9a 046; English DRI/108). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import passives_common as pc


card = PokemonCardDef(
    guid="ddc98463-a128-5caf-ab4e-8408e1a6ed76",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mudsdale.Name",
    display_name="Mudsdale",
    searchable_by=["Mudsdale", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=108,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=150,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Mudbray.Name",
    family_id=749,
    abilities=[
        Ability(
            title="Mud Coat",
            game_text="This Pokémon takes 30 less damage from attacks (after applying Weakness and Resistance).",
            passive=pc.takes_less_passive(30),
        ),
        Attack(
            title="Heavy Impact",
            game_text="",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
        ),
    ],
)
