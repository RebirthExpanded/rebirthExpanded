"""Thundurus (SM - Unified Minds 68/236 -- JP SM10a 024/054).

Basic Lightning Pokemon. HP 120, weakness Fighting x2, resistance Metal -20,
retreat 1.

  Thunderous Gale  [CC] 20+    If Tornadus is on your Bench, this attack
                               does 50 more damage.
  Raging Thunder   [LLC] 120   This attack does 40 damage to 1 of your
                               Benched Pokemon.
"""

from spirit.game.attributes import AttrID, PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import bonus_if, snipe_attack
from spirit.game.data_utils import Attack, PokemonCardDef


def _tornadus_on_bench(ctx) -> bool:
    return any(p.get_attribute(AttrID.EVOLUTION_LOGIC_NAME) == "Tornadus"
               for p in ctx.my_bench())


card = PokemonCardDef(
    guid="374c125a-6f6f-558d-be23-98d0282fa7f4",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Thundurus.Name",
    display_name="Thundurus",
    searchable_by=['Thundurus', 'Basic', 'Thundurus'],
    subtypes=['Basic'],
    collector_number=68,
    set_code="SM11",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=642,
    abilities=[
        Attack(title="Thunderous Gale", game_text="If Tornadus is on your Bench, this attack does 50 more damage.",
               cost={PokemonTypes.COLORLESS: 2}, damage=20, damage_operator="+",
               effect=bonus_if(_tornadus_on_bench, 50)),
        Attack(title="Raging Thunder", game_text="This attack does 40 damage to 1 of your Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
               cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1}, damage=120,
               effect=snipe_attack(40, pool="bench", side="mine", also_base=True)),
    ],
)
