from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.session.passives import Passive, carrier_pokemon


class PersistentCellsPassive(Passive):
    """Knocked Out by damage from an opponent's attack: into the hand
    instead of the discard pile (attached cards are discarded normally). A
    destination, decided as the stack leaves play -- with Lost City (or
    Splash Energy) also redirecting it, its owner chooses."""

    def knockout_destination(self, pokemon, carrier):
        if carrier_pokemon(carrier) is not pokemon:
            return None
        return "hand" if getattr(pokemon, "ko_by_opposing_attack_damage", False) else None


async def cell_fork(ctx):
    """60, then choose 2 of the opponent's Benched Pokemon and put 3 damage
    counters on each of them."""
    await ctx.deal_damage()
    bench = ctx.opponent_bench()
    if not bench:
        return
    count = min(2, len(bench))
    targets = await ctx.choose_cards(
        bench, count, prompt="Choose 2 of your opponent's Benched Pokémon",
    )
    for target in targets:
        await ctx.deal_damage(30, target=target, apply_modifiers=False, as_counters=True)


card = PokemonCardDef(
    guid="79ea0736-1f12-54b1-b4c1-0c82144860b8",
    key="SWSH12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Reuniclus.Name",
    display_name="Reuniclus",
    searchable_by=["Reuniclus", "Stage 2", "Reuniclus"],
    subtypes=["Stage 2"],
    collector_number=78,
    set_code="SWSH12",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Duosion.Name",
    family_id=577,
    abilities=[
        Ability(
            title="Persistent Cells",
            game_text="If this Pok\u00e9mon is Knocked Out by damage from an attack from your opponent's Pok\u00e9mon, put it into your hand instead of the discard pile. (Discard all attached cards.)",
            passive=PersistentCellsPassive(),
        ),
        Attack(
            title="Cell Fork",
            game_text="Choose 2 of your opponent's Benched Pok\u00e9mon and put 3 damage counters on each of them.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=cell_fork,
        ),
    ],
)