"""Team Rocket's Dugtrio (ME2PT5 101 -- JP M2a 083; English ASC/101, ASC/239). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

def _holes_applies(ctx) -> bool:
    moved = getattr(ctx, "moved_pokemon", None)
    return moved is not None and moved.owning_player_id != ctx.source.owning_player_id


async def holes(ctx):
    if ctx.moved_pokemon is None:
        return
    await ctx.deal_damage(20, target=ctx.moved_pokemon, apply_modifiers=False, as_counters=True, is_attack=False)


card = PokemonCardDef(
    guid="aef50e5b-2e6d-5f8c-88d2-84367b220372",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsDugtrio.Name",
    display_name="Team Rocket's Dugtrio",
    searchable_by=["Team Rocket's Dugtrio", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=101,
    set_code="ME2PT5",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsDiglett.Name",
    family_id=50,
    abilities=[
        Ability(
            title="Holes",
            game_text="Whenever your opponent's Active Pokémon moves to the Bench during their turn, place 2 damage counters on that Pokémon.",
            trigger=Triggers.ON_OPPONENT_MOVE_TO_BENCH,
            trigger_applies=_holes_applies,
            effect=holes,
        ),
        Attack(
            title="Mud Shot",
            game_text="",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
    ],
)
