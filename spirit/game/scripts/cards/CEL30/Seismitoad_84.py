from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def quaking_fist(ctx):
    """60; the opponent must flip before each Trainer they use next turn."""
    await ctx.deal_damage()
    ctx.require_trainer_flip(ctx.opponent_id)

card = PokemonCardDef(
    guid="93e529fc-0699-5dec-9270-77178d131fc7",
    key="CEL30",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Seismitoad.Name",
    display_name="Seismitoad",
    searchable_by=["Seismitoad", "Stage 2", "Seismitoad"],
    subtypes=["Stage 2"],
    collector_number=84,
    set_code="CEL30",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=160,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Palpitoad.Name",
    family_id=535,
    abilities=[
        Attack(
            title="Quaking Fist",
            game_text="During your opponent's next turn, whenever they try to use a Trainer card from their hand, they flip a coin. If tails, your opponent discards that Trainer card instead of using it.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=60,
            effect=quaking_fist,
        ),
        Attack(
            title="Mega Punch",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 3},
            damage=180,
        ),
    ],
)
