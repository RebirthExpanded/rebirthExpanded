"""Hop's Corvisquire (SV09 134 -- JP SV9 084; English JTG/134). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="13a19347-5d9f-588f-8cad-a0b4cd88d519",
    key="SV09",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HopsCorvisquire.Name",
    display_name="Hop's Corvisquire",
    searchable_by=["Hop's Corvisquire", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=134,
    set_code="SV09",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.HopsRookidee.Name",
    family_id=821,
    abilities=[
        Attack(
            title="Speed Dive",
            game_text="",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
        Attack(
            title="Razor Wing",
            game_text="",
            cost={PokemonTypes.COLORLESS: 3},
            damage=80,
        ),
    ],
)
