from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import self_energy_discard_attack
from spirit.game.card_effects.pokemon import energy_provides_type
from spirit.game.session.effects import is_basic_energy


_KINDS = ((PokemonTypes.FIRE, "Basic [R]"), (PokemonTypes.FIGHTING, "Basic [F]"))


def _basic_of(cards, pokemon_type):
    return [c for c in cards
            if is_basic_energy(c) and energy_provides_type(c, pokemon_type.value)]


def _pyro_dance_condition(board, player_id, pokemon) -> bool:
    hand = board.find_player_area(player_id, "hand")
    cards = list(hand.children) if hand else []
    return any(_basic_of(cards, t) for t, _ in _KINDS)


async def pyro_dance(ctx):
    """Up to one Basic [R] and up to one Basic [F] Energy card from hand,
    each onto a Pokemon of your choice."""
    for pokemon_type, label in _KINDS:
        cards = _basic_of(ctx.hand(), pokemon_type)
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
    guid="74a00f13-520d-5233-a92a-6c34db5ed46b",
    key="SV06",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Infernape.Name",
    display_name="Infernape",
    searchable_by=["Infernape", "Stage 2", "Infernape"],
    subtypes=["Stage 2"],
    collector_number=33,
    set_code="SV06",
    regulation_mark="H",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Monferno.Name",
    family_id=390,
    abilities=[
        Ability(
            title="Pyro Dance",
            game_text="Once during your turn, you may attach a Basic [R] Energy card, a Basic [F] Energy card, or 1 of each from your hand to your Pokémon in any way you like.",
            activation=Activations.ONCE_PER_TURN,
            condition=_pyro_dance_condition,
            effect=pyro_dance,
        ),
        Attack(
            title="Scorching Fire",
            game_text="Discard an Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=200,
            effect=self_energy_discard_attack(count=1),
        ),
    ],
)
