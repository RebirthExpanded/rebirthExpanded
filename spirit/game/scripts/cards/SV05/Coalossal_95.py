"""Coalossal (SV05 95 -- JP SV5K 041; English TEF/95). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac

from spirit.game.attributes import PokemonTypes as _PT


card = PokemonCardDef(
    guid="d7a887e1-ef18-5326-ae5b-0792c079b88f",
    key="SV05",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Coalossal.Name",
    display_name="Coalossal",
    searchable_by=["Coalossal", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=95,
    set_code="SV05",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    hp=180,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Carkol.Name",
    family_id=837,
    abilities=[
        Attack(
            title="Gatling Tar",
            game_text="This attack does 80 more damage for each Fire Energy attached to this Pokémon.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=40,
            damage_operator="+",
            effect=ac.damage_per(ac.count_energy("self", _PT.FIRE), 80, base=40),
        ),
        Attack(
            title="Cragalanche",
            game_text="Discard the top 2 cards of your opponent's deck.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 3},
            damage=150,
            effect=ac.mill_attack(2),
        ),
    ],
)
