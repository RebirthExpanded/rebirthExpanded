from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.data_utils import Triggers, def_for
from spirit.game.card_effects.attacks_common import damage_counters_on, damage_per


def _spiky_energy(card) -> bool:
    return getattr(def_for(card.archetype_id), "display_name", None) == "Spiky Energy"


async def spike_clad(ctx):
    """Evolved from hand: attach up to 2 Spiky Energy from the discard pile."""
    if not getattr(ctx, "evolved_from_hand", True):
        return
    pool = [c for c in ctx.discard_pile() if _spiky_energy(c)]
    if not pool or not await ctx.ask_yes_no("Attach up to 2 Spiky Energy from your discard pile to this Pokémon?"):
        return
    picks = await ctx.choose_cards(pool, min(2, len(pool)), minimum=0,
                                   prompt="Choose up to 2 Spiky Energy to attach")
    for pick in picks:
        await ctx.attach_energy(pick, ctx.source)

card = PokemonCardDef(
    guid="7ec216e9-b7b9-58e7-9f3c-12e719f2d227",
    key="SV09",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lycanroc.Name",
    display_name="Lycanroc",
    searchable_by=["Lycanroc", "Stage 1", "Lycanroc"],
    subtypes=["Stage 1"],
    collector_number=85,
    set_code="SV09",
    regulation_mark="I",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Rockruff.Name",
    family_id=744,
    abilities=[
        Ability(
            title="Spike-Clad",
            game_text="When you play this Pok\u00e9mon from your hand to evolve 1 of your Pok\u00e9mon during your turn, you may attach up to 2 Spiky Energy cards from your discard pile to this Pok\u00e9mon.",
            trigger=Triggers.ON_EVOLVE,
            effect=spike_clad,
        ),
        Attack(
            title="Clamping Fangs",
            game_text="This attack does 40 more damage for each damage counter on your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=40,
            damage_operator="+",
            effect=damage_per(damage_counters_on("defender"), 40, base=40),
        ),
    ],
)
