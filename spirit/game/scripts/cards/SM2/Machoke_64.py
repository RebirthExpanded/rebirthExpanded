"""Machoke (SM - Guardians Rising 64/145 -- JP SM2K 029/050, the art here).

Stage 1 Fighting Pokemon (evolves from Machop). HP 100, weakness Psychic
x2, retreat 3.

  Daunting Pose  (Ability)  Prevent all damage done to your Benched
                            Pokemon by your opponent's attacks. Your
                            opponent's attacks and Abilities can't put
                            damage counters on your Benched Pokemon.
  Cross Chop     [FFC] 30+  Flip a coin. If heads, this attack does 30
                            more damage.

Manaphy's Wave Veil plus Battle Cage's counter half, both scoped to the
carrier's own Bench; the shield works from anywhere in play (Machoke
need not be Active), as printed.
"""

from spirit.game.attributes import AttrID, PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import flip_damage
from spirit.game.data_utils import Ability, Attack, PokemonCardDef
from spirit.game.session.passives import Passive


def _my_benched(target, carrier) -> bool:
    if target is None or target.owning_player_id != carrier.owning_player_id:
        return False
    parent = target.parent
    return bool(parent) and parent.get_attribute(AttrID.NAME) == "bench"


class _DauntingPosePassive(Passive):
    """The carrier's Benched Pokemon take no damage from opposing attacks
    and no damage counters from the opponent's attacks or Abilities."""

    def prevents_damage(self, calc, carrier):
        return (calc.is_attack and calc.is_opposing
                and _my_benched(calc.target, carrier))

    def blocks_damage_counters(self, target, carrier):
        return _my_benched(target, carrier)


card = PokemonCardDef(
    guid="9f0280d6-5027-589b-880c-8902d0d2b49d",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Machoke.Name",
    display_name="Machoke",
    searchable_by=["Machoke", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=64,
    set_code="SM2",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Machop.Name",
    family_id=66,
    abilities=[
        Ability(
            title="Daunting Pose",
            game_text="Prevent all damage done to your Benched Pokémon by your opponent's attacks. Your opponent's attacks and Abilities can't put damage counters on your Benched Pokémon.",
            passive=_DauntingPosePassive(),
        ),
        Attack(
            title="Cross Chop",
            game_text="Flip a coin. If heads, this attack does 30 more damage.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="+",
            effect=flip_damage(bonus=30, require_all=True),
        ),
    ],
)
