"""Lickilicky (SV05 125 -- JP SV5M 054; English TEF/125). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="d95c3149-7a7c-5692-b5f6-9f7836433696",
    key="SV05",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lickilicky.Name",
    display_name="Lickilicky",
    searchable_by=["Lickilicky", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=125,
    set_code="SV05",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=150,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Lickitung.Name",
    family_id=108,
    abilities=[
        Attack(
            title="Body Slam",
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Paralyzed.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=ac.condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
        Attack(
            title="Tonguenado",
            game_text="Flip 4 coins. This attack does 70 damage for each heads.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=70,
            damage_operator="x",
            effect=ac.flip_damage(coins=4, per_heads=70),
        ),
    ],
)
