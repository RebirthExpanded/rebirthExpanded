"""Team Rocket's Tyranitar (SV10 96 -- JP SV10 050; English DRI/96). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac

from spirit.game.session.effects import is_basic_pokemon_in_play


async def sand_stream(ctx):
    me = ctx.source
    owner = me.owning_player_id
    if ctx.board.active_pokemon(owner) is not me:
        return
    other = next((pid for pid in ctx.board.player_ids if pid != owner), None)
    for p in list(ctx.board.pokemon_in_play(other)) if other else []:
        if is_basic_pokemon_in_play(p):
            await ctx.deal_damage(20, target=p, apply_modifiers=False, as_counters=True)


card = PokemonCardDef(
    guid="01eba6e1-0c22-569e-b690-ca9ca288f1bc",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsTyranitar.Name",
    display_name="Team Rocket's Tyranitar",
    searchable_by=["Team Rocket's Tyranitar", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=96,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Rare,
    hp=180,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsPupitar.Name",
    family_id=246,
    abilities=[
        Ability(
            title="Sand Stream",
            game_text="During Pokémon Checkup, if this Pokémon is in the Active Spot, put 2 damage counters on each of your opponent's Basic Pokémon.",
            trigger=Triggers.BETWEEN_TURNS,
            effect=sand_stream,
        ),
        Attack(
            title="Demolition Tackle",
            game_text="Discard an Energy from your opponent's Active Pokémon.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 3},
            damage=180,
            effect=ac.discard_opponent_energy_attack(1),
        ),
    ],
)
