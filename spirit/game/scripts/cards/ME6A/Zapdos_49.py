"""Zapdos (ME6A 49 -- JP M6a 049; English 30C/133, 30C/55, MEP/98). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac

from spirit.game.data_utils import def_for


def _flapping(other_names, energy_type, title):
    def _names_in_play(board, player_id):
        return {getattr(def_for(p.archetype_id), "display_name", None) for p in board.pokemon_in_play(player_id)}

    def _pred(card):
        return is_basic_energy_card(card) and is_energy_of_type(card, energy_type)

    def condition(board, player_id, pokemon) -> bool:
        hand = board.find_player_area(player_id, "hand")
        return set(other_names) <= _names_in_play(board, player_id) and any(
            _pred(c) for c in (hand.children if hand else []))

    async def effect(ctx):
        pool = [c for c in ctx.hand() if _pred(c)]
        if not pool:
            return
        picks = await ctx.choose_cards(pool, 1, minimum=0, prompt=f"{title}: attach a Basic Energy card to this Pokémon")
        if picks:
            await ctx.attach_energy(picks[0], ctx.source)
    return condition, effect
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card


_flash_condition, _flash_effect = _flapping(("Moltres", "Articuno"), PokemonTypes.LIGHTNING, "Flash-Pop Flapping")


card = PokemonCardDef(
    guid="c9ba8f59-6777-59d3-9617-5552631c2efd",
    key="ME6A",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Zapdos.Name",
    display_name="Zapdos",
    searchable_by=["Zapdos", "Basic"],
    subtypes=["Basic"],
    collector_number=49,
    set_code="ME6A",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=120,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=145,
    abilities=[
        Ability(
            title="Flash-Pop Flapping",
            game_text="Once during your turn, if you have Moltres and Articuno in play, you may use this Ability. Attach a Basic Lightning Energy card from your hand to this Pokémon.",
            activation=Activations.ONCE_PER_TURN,
            condition=_flash_condition,
            effect=_flash_effect,
        ),
        Attack(
            title="Thundering Lightning",
            game_text="This Pokémon also does 60 damage to itself.",
            cost={PokemonTypes.LIGHTNING: 3, PokemonTypes.COLORLESS: 1},
            damage=210,
            effect=ac.recoil_attack(60),
        ),
    ],
)
