"""Trevenant (SV3 12 -- JP SV3 008; English OBF/12). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


async def forest_miasma(ctx):
    me = ctx.source
    owner = me.owning_player_id
    if ctx.board.active_pokemon(owner) is not me:
        return
    other = next((pid for pid in ctx.board.player_ids if pid != owner), None)
    d = ctx.board.active_pokemon(other) if other else None
    if d is not None:
        await ctx.deal_damage(10, target=d, apply_modifiers=False, as_counters=True)


card = PokemonCardDef(
    guid="ea261b1f-9bb5-5081-900b-8951aa02de05",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Trevenant.Name",
    display_name="Trevenant",
    searchable_by=["Trevenant", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=12,
    set_code="SV3",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=140,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Phantump.Name",
    family_id=708,
    abilities=[
        Ability(
            title="Forest Miasma",
            game_text="During Pokémon Checkup, if this Pokémon is in the Active Spot, put 1 damage counter on your opponent's Active Pokémon.",
            trigger=Triggers.BETWEEN_TURNS,
            effect=forest_miasma,
        ),
        Attack(
            title="Lock Up",
            game_text="During your opponent's next turn, the Defending Pokémon can't retreat.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=100,
            effect=ac.condition_attack(no_retreat=True),
        ),
    ],
)
