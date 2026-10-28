"""Starmie (SV045 119 -- JP SV2a 121; English MEW/121, PAF/119). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.session.effects import full_stack


def _comet_condition(board, player_id, pokemon) -> bool:
    return True


async def mysterious_comet(ctx):
    pool = ctx.opponent_pokemon_in_play()
    if not pool:
        return
    target = await ctx.choose_pokemon(pool, "Choose 1 of your opponent's Pokémon to put 2 damage counters on")
    if target is None:
        return
    placed = await ctx.deal_damage(20, target=target, apply_modifiers=False, as_counters=True)
    if placed:
        await ctx.discard_cards(full_stack(ctx.source))


card = PokemonCardDef(
    guid="fc809e69-94d6-508a-8336-0fce17041656",
    key="SV045",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Starmie.Name",
    display_name="Starmie",
    searchable_by=["Starmie", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=119,
    set_code="SV045",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Staryu.Name",
    family_id=120,
    abilities=[
        Ability(
            title="Mysterious Comet",
            game_text="Once during your turn, you may put 2 damage counters on 1 of your opponent's Pokémon. If you placed any damage counters in this way, discard this Pokémon and all attached cards.",
            activation=Activations.ONCE_PER_TURN,
            condition=_comet_condition,
            effect=mysterious_comet,
        ),
        Attack(
            title="Speed Attack",
            game_text="",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
    ],
)
