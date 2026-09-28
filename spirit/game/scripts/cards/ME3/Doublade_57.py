from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.data_utils import def_for


_SWORDS = ("Honedge", "Doublade", "Aegislash")


async def weaponized_swords(ctx):
    """Reveal any number of Honedge / Doublade / Aegislash from hand; 60 each."""
    pool = [c for c in ctx.hand()
            if getattr(def_for(c.archetype_id), "display_name", None) in _SWORDS]
    picks = []
    if pool:
        picks = await ctx.choose_cards(pool, len(pool), minimum=0,
                                       prompt="Reveal any number of Honedge, Doublade and Aegislash")
    if picks:
        await ctx.reveal_cards(picks)
        await ctx.deal_damage(60 * len(picks))

card = PokemonCardDef(
    guid="5808e145-10ff-59ed-bb61-c41dd83e4a95",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Doublade.Name",
    display_name="Doublade",
    searchable_by=["Doublade", "Stage 1", "Doublade"],
    subtypes=["Stage 1"],
    collector_number=57,
    set_code="ME3",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Honedge.Name",
    family_id=679,
    abilities=[
        Attack(
            title="Weaponized Swords",
            game_text="Reveal any number of Honedge, Doublade, and Aegislash from your hand, and this attack does 60 damage for each card you revealed in this way.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator="x",
            effect=weaponized_swords,
        ),
    ],
)
