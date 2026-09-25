"""Dragonite (SM - Unified Minds 151/236 -- JP SM11 057/094).

Stage 2 Dragon Pokemon, evolves from Dragonair. HP 160, weakness Fairy x2,
retreat 2.

  Ability  Hurricane Charge  Once during your turn (before your attack), you
                             may attach a [W] Energy card, a [L] Energy card,
                             or 1 of each from your hand to your Pokemon in
                             any way you like.
  Dragon Impact  [WLCC] 170  Discard 3 Energy from this Pokemon.

Up to one [W] and up to one [L] Energy card, each onto a Pokemon of the
player's choice; not offered with neither in hand.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import self_energy_discard_attack
from spirit.game.session.effects import is_energy_of_type
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef


def _energy_cards(hand, pokemon_type):
    return [c for c in hand if is_energy_of_type(c, pokemon_type)]


def _hurricane_charge_condition(board, player_id, pokemon) -> bool:
    hand = board.find_player_area(player_id, "hand")
    cards = list(hand.children) if hand else []
    return bool(_energy_cards(cards, PokemonTypes.WATER)
                or _energy_cards(cards, PokemonTypes.LIGHTNING))


async def hurricane_charge(ctx):
    for pokemon_type, label in ((PokemonTypes.WATER, "Water"),
                                (PokemonTypes.LIGHTNING, "Lightning")):
        cards = _energy_cards(ctx.hand(), pokemon_type)
        if not cards:
            continue
        picks = await ctx.choose_cards(
            cards, 1, minimum=0, prompt=f"Choose a {label} Energy card to attach (optional)")
        if not picks:
            continue
        target = await ctx.choose_pokemon(
            ctx.my_pokemon_in_play(), f"Choose a Pokémon to attach the {label} Energy to")
        if target is not None:
            await ctx.attach_energy(picks[0], target)


card = PokemonCardDef(
    guid="923ddb29-d2f6-5900-bdcc-77777250eb30",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dragonite.Name",
    display_name="Dragonite",
    searchable_by=['Dragonite', 'Stage 2', 'Dragonite'],
    subtypes=['Stage 2'],
    collector_number=151,
    set_code="SM11",
    rarity=Rarities.Rare,
    hp=160,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FAIRY,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Dragonair.Name",
    family_id=147,
    abilities=[
        Ability(
            title="Hurricane Charge",
            game_text="Once during your turn (before your attack), you may attach a Water Energy card, a Lightning Energy card, or 1 of each from your hand to your Pokémon in any way you like.",
            activation=Activations.ONCE_PER_TURN,
            condition=_hurricane_charge_condition,
            effect=hurricane_charge,
        ),
        Attack(title="Dragon Impact", game_text="Discard 3 Energy from this Pokémon.",
               cost={PokemonTypes.WATER: 1, PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2}, damage=170,
               effect=self_energy_discard_attack(count=3)),
    ],
)
