from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import AttrID
from spirit.game.data_utils import subtypes_for
from spirit.game.session.effects import live_pokemon_types
from spirit.game.session.passives import effective_max_hp


def _damaged(board, pokemon) -> bool:
    return pokemon.get_attribute(AttrID.HP, 0) < effective_max_hp(board, pokemon)


def _excited_heal_condition(board, player_id, pokemon) -> bool:
    mine = list(board.pokemon_in_play(player_id))
    has_mega = any("SV_Mega" in subtypes_for(p.archetype_id)
                   and PokemonTypes.GRASS.value in live_pokemon_types(p) for p in mine)
    return has_mega and any(_damaged(board, p) for p in mine)


async def excited_heal(ctx):
    """Heal 60 damage from 1 of your Pokemon."""
    pool = [p for p in ctx.my_pokemon_in_play() if _damaged(ctx.board, p)]
    if not pool:
        return
    target = await ctx.choose_pokemon(pool, "Choose a Pokémon to heal 60 damage from")
    if target is not None:
        await ctx.heal(60, target)

card = PokemonCardDef(
    guid="380be4d4-6a64-5095-9916-9d0293e2ab4f",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ludicolo.Name",
    display_name="Ludicolo",
    searchable_by=["Ludicolo", "Stage 2", "Ludicolo"],
    subtypes=["Stage 2"],
    collector_number=7,
    set_code="ME2",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=160,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Lombre.Name",
    family_id=270,
    abilities=[
        Ability(
            title="Excited Heal",
            game_text="Once during your turn, if you have any [G] Mega Evolution Pok\u00e9mon ex in play, you may use this Ability. Heal 60 damage from 1 of your Pok\u00e9mon.",
            activation=Activations.ONCE_PER_TURN,
            condition=_excited_heal_condition,
            effect=excited_heal,
        ),
        Attack(
            title="Lunge Out",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=120,
        ),
    ],
)
