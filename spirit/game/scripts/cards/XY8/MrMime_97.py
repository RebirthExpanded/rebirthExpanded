"""Mr. Mime (XY - BREAKthrough 97/162 -- JP XY8 045/059, the art here).

Basic Psychic Pokemon. HP 70, weakness Psychic x2, resistance Fighting
-20, retreat 1.

  Bench Barrier  (Ability)  Prevent all damage done to your Benched
                            Pokemon by attacks.
  Juggling       [CC] 10x   Flip 4 coins. This attack does 10 damage
                            times the number of heads.

Manaphy's Wave Veil worded without "from your opponent's attacks", so it
also stops an attack of MY OWN reaching my Bench; the Ability works from
anywhere in play, the Bench included.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import flip_damage
from spirit.game.data_utils import Ability, Attack, PokemonCardDef
from spirit.game.session.passives import Passive


class _BenchBarrierPassive(Passive):
    """The carrier's Benched Pokemon take no attack damage, from either side."""

    def prevents_damage(self, calc, carrier):
        target = calc.target
        return (calc.is_attack and target is not None
                and target.owning_player_id == carrier.owning_player_id
                and not calc.to_active)


card = PokemonCardDef(
    guid="a2f2298f-ce91-5702-8bc0-d4c8258a8792",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MrMime.Name",
    display_name="Mr. Mime",
    searchable_by=["Mr. Mime", "Basic", "MrMime"],
    subtypes=["Basic"],
    collector_number=97,
    set_code="XY8",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=122,
    abilities=[
        Ability(
            title="Bench Barrier",
            game_text="Prevent all damage done to your Benched Pokémon by attacks.",
            passive=_BenchBarrierPassive(),
        ),
        Attack(
            title="Juggling",
            game_text="Flip 4 coins. This attack does 10 damage times the number of heads.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=10,
            damage_operator="x",
            effect=flip_damage(coins=4, per_heads=10),
        ),
    ],
)
