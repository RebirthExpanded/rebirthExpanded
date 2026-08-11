from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.pokemon import energy_provides_type


def _has_darkness_energy(board, player_id, pokemon) -> bool:
    return any(
        energy_provides_type(e, PokemonTypes.DARKNESS.value)
        for e in board.attached_energies(pokemon)
    )


async def adrena_brain(ctx):
    """Move up to 3 damage counters from 1 of your Pokémon to 1 of your
    opponent's Pokémon."""
    source = await ctx.choose_pokemon(
        ctx.my_pokemon_in_play(), "Choose a Pokémon to move damage counters from"
    )
    if source is None:
        return
    dest = await ctx.choose_pokemon(
        ctx.opponent_pokemon_in_play(),
        "Choose a Pokémon to move damage counters to",
    )
    if dest is None:
        return
    await ctx.move_damage_counters(source, dest, max_count=3)


card = PokemonCardDef(
    guid="42cc7ba1-a896-438d-8463-14459aa4b7c2",
    key="SV06",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Munkidori.Name",
    display_name="Munkidori",
    searchable_by=["Munkidori", "Basic", "Munkidori"],
    subtypes=["Basic"],
    collector_number=95,
    set_code="SV06",
    regulation_mark="H",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    abilities=[
        Ability(
            title="Adrena-Brain",
            game_text=(
                "Once during your turn, if this Pokémon has any [D] Energy "
                "attached, you may move up to 3 damage counters from 1 of your "
                "Pokémon to 1 of your opponent's Pokémon."
            ),
            activation=Activations.ONCE_PER_TURN,
            condition=_has_darkness_energy,
            effect=adrena_brain,
        ),
        Attack(
            title="Mind Bend",
            game_text="Your opponent's Active Pokémon is now Confused.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
            effect=condition_attack(SpecialConditions.CONFUSED),
        ),
    ],
)

