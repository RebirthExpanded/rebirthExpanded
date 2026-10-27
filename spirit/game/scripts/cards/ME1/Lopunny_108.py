"""Lopunny (ME1 108 -- JP M1S 054; English MEG/108). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="cb504110-cf0f-586c-847f-e6242f1a7209",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lopunny.Name",
    display_name="Lopunny",
    searchable_by=["Lopunny", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=108,
    set_code="ME1",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=110,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Buneary.Name",
    family_id=427,
    abilities=[
        Attack(
            title="Dashing Kick",
            game_text="This attack does 50 damage to 1 of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.COLORLESS: 1},
            effect=ac.snipe_attack(50, pool="bench"),
        ),
        Attack(
            title="Spiral Kick",
            game_text="",
            cost={PokemonTypes.COLORLESS: 2},
            damage=60,
        ),
    ],
)
