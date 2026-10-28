"""Skeledirge ex (SV4 137 -- JP SVEL 008; English PAR/137). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers
from spirit.game.card_effects.pokemon import TeraRulePassive

from spirit.game.card_effects import attacks_common as ac
from spirit.game.session.passives import Passive, carrier_pokemon
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card


def _basic_fire(card):
    return is_basic_energy_card(card) and is_energy_of_type(card, PokemonTypes.FIRE)



class _IncendiarySong(Passive):
    """Game-level: during that turn the owner's attacks do 60 more to the
    opponent's Active (before W/R)."""

    def __init__(self, owner, turn):
        self.owner, self.turn = owner, turn

    def modify_damage_dealt(self, calc, carrier):
        ts = getattr(calc.board, "turn_state", None)
        a = calc.attacker
        if (ts is not None and ts.turn_number == self.turn and calc.is_attack and calc.is_opposing and calc.to_active
                and a is not None and a.owning_player_id == self.owner):
            calc.amount += 60


def _song_condition(board, player_id, pokemon) -> bool:
    hand = board.find_player_area(player_id, "hand")
    return bool(hand) and any(_basic_fire(c) for c in hand.children)


async def incendiary_song(ctx):
    paid = await ctx.discard_from_hand(1, minimum=1, predicate=_basic_fire, prompt="Discard a Basic Fire Energy card")
    if paid:
        ctx.add_game_passive(_IncendiarySong(ctx.player_id, ctx.session.turn_state.turn_number))


card = PokemonCardDef(
    guid="08a16458-0362-50a2-9e41-452462e0e9c8",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Skeledirgeex.Name",
    display_name="Skeledirge ex",
    searchable_by=["Skeledirge ex", "Stage 2", "ex", "Tera"],
    subtypes=["Stage 2", "ex", "Tera"],
    collector_number=137,
    set_code="SV4",
    regulation_mark="G",
    rarity=Rarities.RareHoloEX,
    hp=330,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Crocalor.Name",
    family_id=909,
    passive=TeraRulePassive(),
    abilities=[
        Ability(
            title="Incendiary Song",
            game_text="Once during your turn, you may discard a Basic Fire Energy card from your hand in order to use this Ability. During this turn, attacks used by your Pokémon do 60 more damage to your opponent's Active Pokémon (before applying Weakness and Resistance).",
            activation=Activations.ONCE_PER_TURN,
            condition=_song_condition,
            effect=incendiary_song,
        ),
        Attack(
            title="Luster Burn",
            game_text="This attack's damage isn't affected by any effects on your opponent's Active Pokémon.",
            cost={PokemonTypes.FIRE: 2},
            damage=160,
            effect=ac.ignore_effects_attack(),
        ),
    ],
)
