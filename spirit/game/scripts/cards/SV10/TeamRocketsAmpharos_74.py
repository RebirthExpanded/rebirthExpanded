"""Team Rocket's Ampharos (SV10 74 -- JP SV10 036; English DRI/74). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

def _darkest_impulse_applies(ctx) -> bool:
    pokemon = getattr(ctx, "evolved_pokemon", None)
    if pokemon is None or not getattr(ctx, "evolved_from_hand", False):
        return False
    owner = pokemon.owning_player_id
    return (owner is not None and owner != ctx.source.owning_player_id
            and pokemon in ctx.board.pokemon_in_play(owner))


async def darkest_impulse(ctx):
    """4 damage counters on the evolved Pokemon; doesn't stack."""
    pokemon = getattr(ctx, "evolved_pokemon", None)
    if pokemon is None:
        return
    mark = (ctx.session.turn_state.turn_number, pokemon.archetype_id)
    if getattr(pokemon, "_darkest_impulse", None) == mark:
        return
    pokemon._darkest_impulse = mark
    await ctx.deal_damage(40, target=pokemon, apply_modifiers=False, as_counters=True)


card = PokemonCardDef(
    guid="9d324ad7-5fec-5f7c-be5a-feab3cc7576a",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsAmpharos.Name",
    display_name="Team Rocket's Ampharos",
    searchable_by=["Team Rocket's Ampharos", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=74,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=140,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsFlaaffy.Name",
    family_id=179,
    abilities=[
        Ability(
            title="Darkest Impulse",
            game_text="Whenever your opponent plays a Pokémon from their hand to evolve 1 of their Pokémon, put 4 damage counters on that Pokémon. The effect of Darkest Impulse doesn't stack.",
            trigger=Triggers.ON_POKEMON_EVOLVED,
            trigger_applies=_darkest_impulse_applies,
            effect=darkest_impulse,
        ),
        Attack(
            title="Head Bolt",
            game_text="",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=140,
        ),
    ],
)
