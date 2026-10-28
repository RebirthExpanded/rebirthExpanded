"""Murkrow (SVP 21 -- JP SV2P 045; English PAF/181, PAL/131, SVP/21). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su
from spirit.game.card_effects import attacks_common as ac
from spirit.game.data_utils import def_for, subtypes_for

from spirit.game.session.effects import is_pokemon_card


def _united_wings(ctx) -> int:
    return sum(1 for c in ctx.discard_pile() if is_pokemon_card(c)
               and any(getattr(a, "title", "") == "United Wings" for a in getattr(def_for(c.archetype_id), "abilities", [])))


card = PokemonCardDef(
    guid="6f1761b9-fe17-5663-9f29-df7f4cf5b544",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Murkrow.Name",
    display_name="Murkrow",
    searchable_by=["Murkrow", "Basic"],
    subtypes=["Basic"],
    collector_number=21,
    set_code="SVP",
    regulation_mark="G",
    rarity=Rarities.RarePromo,
    hp=60,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=198,
    abilities=[
        Attack(
            title="Spin Turn",
            game_text="Switch this Pokémon with 1 of your Benched Pokémon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=su.switch_self_attack(),
        ),
        Attack(
            title="United Wings",
            game_text="This attack does 20 damage for each Pokémon in your discard pile that has the United Wings attack.",
            cost={PokemonTypes.DARKNESS: 1},
            damage=20,
            damage_operator="x",
            effect=ac.damage_per(_united_wings, 20),
        ),
    ],
)
