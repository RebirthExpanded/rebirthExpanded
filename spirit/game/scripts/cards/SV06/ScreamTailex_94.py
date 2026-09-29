from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import discard_opponent_energy_attack
from spirit.game.card_effects.trainers import second_players_first_turn
from spirit.game.session.effects import is_supporter_card


async def scream(ctx):
    """The opponent can't play Supporter cards from hand during their next
    turn (going second, first turn only)."""
    ctx.lock_plays(ctx.opponent_id, is_supporter_card)

card = PokemonCardDef(
    guid="41e8bd40-8aaa-50b9-82a7-6d2a46c7a4fa",
    key="SV06",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ScreamTailex.Name",
    display_name="Scream Tail ex",
    searchable_by=["Scream Tail ex", "Basic", "ex", "ScreamTailex"],
    subtypes=["Basic", "ex"],
    collector_number=94,
    set_code="SV06",
    regulation_mark="H",
    rarity=Rarities.RareHoloEX,
    hp=190,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=985,
    abilities=[
        Attack(
            title="Scream",
            game_text="You can use this attack only if you go second, and only during your first turn. Your opponent can't play any Supporter cards from their hand during their next turn.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=0,
            effect=scream,
            condition=second_players_first_turn,
        ),
        Attack(
            title="Crunch",
            game_text="Discard an Energy from your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=120,
            effect=discard_opponent_energy_attack(),
        ),
    ],
)
