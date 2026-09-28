from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.data_utils import Triggers, def_for
from spirit.game.card_effects.support_common import _gust


async def defiant_horn(ctx):
    """Evolved from hand: you may switch in 1 of the opponent's Benched Pokemon."""
    if not getattr(ctx, "evolved_from_hand", True) or not ctx.opponent_bench():
        return
    if await ctx.ask_yes_no("Switch in 1 of your opponent's Benched Pokémon to the Active Spot?"):
        await _gust(ctx)

card = PokemonCardDef(
    guid="73e71022-0a4b-5928-8439-8c2bca289187",
    key="SV09",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HopsDubwool.Name",
    display_name="Hop's Dubwool",
    searchable_by=["Hop's Dubwool", "Stage 1", "HopsDubwool"],
    subtypes=["Stage 1"],
    collector_number=136,
    set_code="SV09",
    regulation_mark="I",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.HopsWooloo.Name",
    family_id=831,
    abilities=[
        Ability(
            title="Defiant Horn",
            game_text="When you play this Pok\u00e9mon from your hand to evolve 1 of your Pok\u00e9mon during your turn, you may switch in 1 of your opponent's Benched Pok\u00e9mon to the Active Spot.",
            trigger=Triggers.ON_EVOLVE,
            effect=defiant_horn,
        ),
        Attack(
            title="Headbutt",
            cost={PokemonTypes.COLORLESS: 3},
            damage=80,
        ),
    ],
)
