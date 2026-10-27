"""Moltres (ME6A 6 -- JP M6a 006; English 30C/11, 30C/130, MEP/96). Japanese art.
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


_fiery_condition, _fiery_effect = _flapping(("Articuno", "Zapdos"), PokemonTypes.FIRE, "Fiery Flapping")


card = PokemonCardDef(
    guid="8ffdbc1f-3578-5edc-a244-07545be9acc3",
    key="ME6A",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Moltres.Name",
    display_name="Moltres",
    searchable_by=["Moltres", "Basic"],
    subtypes=["Basic"],
    collector_number=6,
    set_code="ME6A",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=120,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=146,
    abilities=[
        Ability(
            title="Fiery Flapping",
            game_text="Once during your turn, if you have Articuno and Zapdos in play, you may use this Ability. Attach a Basic Fire Energy card from your hand to this Pokémon.",
            activation=Activations.ONCE_PER_TURN,
            condition=_fiery_condition,
            effect=_fiery_effect,
        ),
        Attack(
            title="Fire Spin",
            game_text="Discard 2 Energy from this Pokémon.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
            effect=ac.self_energy_discard_attack(count=2),
        ),
    ],
)
