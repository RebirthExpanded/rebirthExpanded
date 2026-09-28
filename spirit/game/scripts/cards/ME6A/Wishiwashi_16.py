"""Wishiwashi (JP M6a 016/103 -- 30th Celebrations; English 30C 22).
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.data_utils import def_for
from spirit.game.card_effects.attacks_common import flip_or_nothing
from spirit.game.card_effects.passives_common import is_in_active_spot
from spirit.game.session.passives import Passive


class CounterattackGroupingPassive(Passive):
    """When your Active Wishiwashi / Wishiwashi ex takes attack damage from the
    opponent, 3 damage counters on the attacker (placed before the HP write,
    so it also works when that Pokemon is Knocked Out)."""

    async def damage_interceptor(self, ctx, calc, target, carrier):
        if not (calc.is_attack and calc.is_opposing and calc.amount > 0):
            return None
        if target.owning_player_id != carrier.owning_player_id or not is_in_active_spot(target):
            return None
        if getattr(def_for(target.archetype_id), "display_name", None) not in ("Wishiwashi", "Wishiwashi ex"):
            return None
        attacker = calc.attacker
        if attacker is not None:
            await ctx.deal_damage(30, target=attacker, apply_modifiers=False, as_counters=True)
        return None

card = PokemonCardDef(
    guid="cbde8338-ea53-5c0d-8c42-04777a0bdc83",
    key="ME6A",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Wishiwashi.Name",
    display_name="Wishiwashi",
    searchable_by=["Wishiwashi", "Basic", "Wishiwashi"],
    subtypes=["Basic"],
    collector_number=16,
    set_code="ME6A",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=746,
    abilities=[
        Ability(
            title="Counterattack Grouping",
            game_text="If your Wishiwashi or Wishiwashi ex is in the Active Spot and is damaged by an attack from your opponent's Pok\u00e9mon (even if your Pok\u00e9mon is Knocked Out), place 3 damage counters on the Attacking Pok\u00e9mon.",
            passive=CounterattackGroupingPassive(),
        ),
        Attack(
            title="Surprise Attack",
            game_text="Flip a coin. If tails, this attack does nothing.",
            cost={PokemonTypes.WATER: 1},
            damage=30,
            effect=flip_or_nothing(),
        ),
    ],
)
