"""Medicham ex (SV07 80 -- JP SV7 054; English SCR/161, SCR/80). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES


async def chi_atsu(ctx):
    d = ctx.opponent_active()
    if d is None:
        return
    hp = d.get_attribute(AttrID.HP, 0) or 0
    if hp > 50:
        await ctx.deal_damage(hp - 50, target=d, apply_modifiers=False, as_counters=True)


async def yoga_kick(ctx):
    await ctx.deal_damage(ignore_weakness=True, ignore_resistance=True)


card = PokemonCardDef(
    guid="1c6d00c1-581d-577f-a519-f693ddc355d1",
    key="SV07",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Medichamex.Name",
    display_name="Medicham ex",
    searchable_by=["Medicham ex", "Stage 1", "ex"],
    subtypes=["Stage 1", "ex"],
    collector_number=80,
    set_code="SV07",
    regulation_mark="H",
    rarity=Rarities.RareHoloEX,
    hp=260,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Meditite.Name",
    family_id=307,
    abilities=[
        Attack(
            title="Chi-Atsu",
            game_text="Put damage counters on your opponent's Active Pokémon until its remaining HP is 50.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=chi_atsu,
        ),
        Attack(
            title="Yoga Kick",
            game_text="This attack's damage isn't affected by Weakness or Resistance.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=190,
            effect=yoga_kick,
        ),
    ],
)
