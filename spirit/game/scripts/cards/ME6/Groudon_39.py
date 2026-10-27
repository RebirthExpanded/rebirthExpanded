"""Groudon (ME6 39 -- JP M6 039; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.data_utils import def_for, subtypes_for


def _legendary_stadium(board) -> bool:
    area = board.find_global_area("activeStadium")
    return any("Legendary" in (getattr(def_for(c.archetype_id), "display_name", "") or "")
               for c in (area.children if area else []))


def _legendary(ctx) -> bool:
    return _legendary_stadium(ctx.board)


card = PokemonCardDef(
    guid="facd20d7-eaca-525c-8fb2-7f53cf72a71c",
    key="ME6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Groudon.Name",
    display_name="Groudon",
    searchable_by=["Groudon", "Basic"],
    subtypes=["Basic"],
    collector_number=39,
    set_code="ME6",
    regulation_mark="J",
    rarity=Rarities.Rare,
    hp=150,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    family_id=383,
    abilities=[
        Attack(
            title="Strength",
            game_text="",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
        ),
        Attack(
            title="Raging Earth",
            game_text="If a Stadium with \"Legendary\" in its name is in play, this attack does 170 more damage.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
            damage_operator="+",
            effect=ac.bonus_if(_legendary, 170),
        ),
    ],
)
