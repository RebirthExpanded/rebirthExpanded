"""Wattrel (SV2 80 -- JP SV1a 031; English PAF/145, PAL/80). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.data_utils import def_for, subtypes_for

from spirit.game.session.effects import is_pokemon_card


def _united_wings(ctx) -> int:
    return sum(1 for c in ctx.discard_pile() if is_pokemon_card(c)
               and any(getattr(a, "title", "") == "United Wings" for a in getattr(def_for(c.archetype_id), "abilities", [])))


card = PokemonCardDef(
    guid="a23fb268-a9a9-5927-91a9-d26bae0397ba",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Wattrel.Name",
    display_name="Wattrel",
    searchable_by=["Wattrel", "Basic"],
    subtypes=["Basic"],
    collector_number=80,
    set_code="SV2",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=940,
    abilities=[
        Attack(
            title="Peck",
            game_text="",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="United Wings",
            game_text="This attack does 20 damage for each Pokémon in your discard pile that has the United Wings attack.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="x",
            effect=ac.damage_per(_united_wings, 20),
        ),
    ],
)
