"""Erika's Victreebel (ME2PT5 6 -- JP MC 008; English ASC/6). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.data_utils import def_for


def _is_erikas(card) -> bool:
    return (getattr(def_for(card.archetype_id), "display_name", "") or "").startswith("Erika's ")


card = PokemonCardDef(
    guid="85065483-ddfe-5a5a-882c-11f4aa3376b3",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ErikasVictreebel.Name",
    display_name="Erika's Victreebel",
    searchable_by=["Erika's Victreebel", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=6,
    set_code="ME2PT5",
    regulation_mark="J",
    rarity=Rarities.Rare,
    hp=150,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.ErikasWeepinbell.Name",
    family_id=69,
    abilities=[
        Attack(
            title="Flower Garden Rondo",
            game_text="This attack does 40 damage for each of your Erika's Pokémon in play.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            damage_operator="x",
            effect=ac.damage_per(ac.count_in_play("mine", pred=_is_erikas), 40),
        ),
        Attack(
            title="Solar Beam",
            game_text="",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
        ),
    ],
)
