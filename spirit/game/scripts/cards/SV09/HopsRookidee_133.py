"""Hop's Rookidee (SV09 133 -- JP SV9 083; English JTG/133). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import passives_common as pc


card = PokemonCardDef(
    guid="e334bfa2-a4ee-53af-87b8-0d3dc0658269",
    key="SV09",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HopsRookidee.Name",
    display_name="Hop's Rookidee",
    searchable_by=["Hop's Rookidee", "Basic"],
    subtypes=["Basic"],
    collector_number=133,
    set_code="SV09",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=821,
    abilities=[
        Attack(
            title="Intimidating Stare",
            game_text="During your opponent's next turn, attacks used by the Defending Pokémon do 20 less damage (before applying Weakness and Resistance).",
            cost={PokemonTypes.COLORLESS: 1},
            effect=pc.debuff_defender_attacks(20),
        ),
        Attack(
            title="Peck",
            game_text="",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
