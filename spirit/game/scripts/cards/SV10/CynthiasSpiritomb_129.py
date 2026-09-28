from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities
from spirit.game.data_utils import def_for


def _is_cynthias(pokemon) -> bool:
    name = getattr(def_for(pokemon.archetype_id), "display_name", "") or ""
    return name.startswith("Cynthia's ")


async def raging_curse(ctx):
    """10 for each damage counter on your Benched Cynthia's Pokemon; no Weakness."""
    counters = sum(max(0, ctx.max_hp(p) - p.get_attribute(AttrID.HP, 0)) // 10
                   for p in ctx.my_bench() if _is_cynthias(p))
    if counters:
        await ctx.deal_damage(10 * counters, ignore_weakness=True)

card = PokemonCardDef(
    guid="23106883-9ef6-550e-a458-df558307bae0",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.CynthiasSpiritomb.Name",
    display_name="Cynthia's Spiritomb",
    searchable_by=["Cynthia's Spiritomb", "Basic", "CynthiasSpiritomb"],
    subtypes=["Basic"],
    collector_number=129,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=442,
    abilities=[
        Attack(
            title="Raging Curse",
            game_text="This attack does 10 damage for each damage counter on all of your Benched Cynthia's Pok\u00e9mon. This attack's damage isn't affected by Weakness.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="x",
            effect=raging_curse,
        ),
    ],
)
