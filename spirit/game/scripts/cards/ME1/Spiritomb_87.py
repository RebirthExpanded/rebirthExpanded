"""Spiritomb (ME1 87 -- JP M1L 039; English MEG/148, MEG/87). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.session.passives import Passive, carrier_pokemon
from spirit.game.card_effects import attacks_common as ac
from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES



class SpitefulSwirlPassive(Passive):
    """Your Active Darkness Pokemon damaged by an opposing attack: 1 damage
    counter on the Attacking Pokemon (an Ability)."""

    async def damage_interceptor(self, ctx, calc, target, carrier):
        me = carrier_pokemon(carrier)
        attacker = calc.attacker
        if not (calc.is_attack and calc.is_opposing and calc.amount > 0 and attacker is not None):
            return None
        if target.owning_player_id != me.owning_player_id or ctx.board.active_pokemon(target.owning_player_id) is not target:
            return None
        if PokemonTypes.DARKNESS.value not in (target.get_attribute(AttrID.POKEMON_TYPES) or []):
            return None
        await ctx.deal_damage(10, target=attacker, apply_modifiers=False, as_counters=True, is_attack=False)
        return None


card = PokemonCardDef(
    guid="f6f06424-32c8-5307-a7b2-6b7c280157e7",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Spiritomb.Name",
    display_name="Spiritomb",
    searchable_by=["Spiritomb", "Basic"],
    subtypes=["Basic"],
    collector_number=87,
    set_code="ME1",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=442,
    abilities=[
        Ability(
            title="Spiteful Swirl",
            game_text="If your Active Darkness Pokémon is damaged by an attack from your opponent's Pokémon (even if your Active Darkness Pokémon is Knocked Out), place 1 damage counter on the Attacking Pokémon.",
            passive=SpitefulSwirlPassive(),
        ),
        Attack(
            title="Mountain Breaker",
            game_text="Discard the top card of your opponent's deck.",
            cost={PokemonTypes.DARKNESS: 1},
            damage=10,
            effect=ac.mill_attack(1),
        ),
    ],
)
