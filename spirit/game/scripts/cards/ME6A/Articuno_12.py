"""Articuno (ME6A 12 -- JP M6a 012; English 30C/132, 30C/18, MEP/97). Japanese art.
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


_frosty_condition, _frosty_effect = _flapping(("Moltres", "Zapdos"), PokemonTypes.WATER, "Frosty Flapping")


card = PokemonCardDef(
    guid="17b387ce-272f-55be-bee0-3a35aa5e0765",
    key="ME6A",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Articuno.Name",
    display_name="Articuno",
    searchable_by=["Articuno", "Basic"],
    subtypes=["Basic"],
    collector_number=12,
    set_code="ME6A",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=144,
    abilities=[
        Ability(
            title="Frosty Flapping",
            game_text="Once during your turn, if you have Moltres and Zapdos in play, you may use this Ability. Attach a Basic Water Energy card from your hand to this Pokémon.",
            activation=Activations.ONCE_PER_TURN,
            condition=_frosty_condition,
            effect=_frosty_effect,
        ),
        Attack(
            title="Hail",
            game_text="This attack does 30 damage to each of your opponent's Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            effect=ac.damage_all_opponents(30),
        ),
    ],
)
