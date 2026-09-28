from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.data_utils import Triggers, def_for
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


async def sneaky_bite(ctx):
    """Evolved from hand: you may put 2 damage counters on 1 opposing Pokemon."""
    if not getattr(ctx, "evolved_from_hand", True):
        return
    pool = ctx.opponent_pokemon_in_play()
    if not pool or not await ctx.ask_yes_no("Put 2 damage counters on 1 of your opponent's Pokémon?"):
        return
    target = await ctx.choose_pokemon(pool, "Choose 1 of your opponent's Pokémon")
    if target is not None:
        await ctx.deal_damage(20, target=target, apply_modifiers=False, as_counters=True)

card = PokemonCardDef(
    guid="c4e55c9e-4751-540f-a554-4fab9e6c254e",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsGolbat.Name",
    display_name="Team Rocket's Golbat",
    searchable_by=["Team Rocket's Golbat", "Stage 1", "TeamRocketsGolbat"],
    subtypes=["Stage 1"],
    collector_number=121,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsZubat.Name",
    family_id=41,
    abilities=[
        Ability(
            title="Sneaky Bite",
            game_text="When you play this Pok\u00e9mon from your hand to evolve 1 of your Pok\u00e9mon during your turn, you may put 2 damage counters on 1 of your opponent's Pok\u00e9mon.",
            trigger=Triggers.ON_EVOLVE,
            effect=sneaky_bite,
        ),
        Attack(
            title="Confuse Ray",
            game_text="Your opponent's Active Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.DARKNESS: 1},
            damage=30,
            effect=condition_attack(SpecialConditions.CONFUSED),
        ),
    ],
)
