"""Throh (SM - Cosmic Eclipse 118/236 -- JP SM11a 032/064).

Basic Fighting Pokemon. HP 120, weakness Psychic x2, retreat 2.

  Reverse Shoulder Throw  [FC] 30+  If your Benched Pokemon have any damage
                                    counters on them, this attack does 90
                                    more damage.
"""

from spirit.game.attributes import AttrID, PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import bonus_if
from spirit.game.session.passives import effective_max_hp
from spirit.game.data_utils import Attack, PokemonCardDef


def _any_damaged_bench(ctx) -> bool:
    return any(p.get_attribute(AttrID.HP, 0) < effective_max_hp(ctx.board, p)
               for p in ctx.my_bench())


card = PokemonCardDef(
    guid="4ac4a90a-7fae-52f5-9de8-b34bdfdd8d5a",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Throh.Name",
    display_name="Throh",
    searchable_by=['Throh', 'Basic', 'Throh'],
    subtypes=['Basic'],
    collector_number=118,
    set_code="SM12",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=538,
    abilities=[
        Attack(title="Reverse Shoulder Throw", game_text="If your Benched Pokémon have any damage counters on them, this attack does 90 more damage.",
               cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1}, damage=30, damage_operator="+",
               effect=bonus_if(_any_damaged_bench, 90)),
    ],
)
