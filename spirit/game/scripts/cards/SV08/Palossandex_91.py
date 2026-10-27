"""Palossand ex (SV08 91 -- JP SV8 057; English SSP/221, SSP/91). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers
from spirit.game.card_effects.pokemon import TeraRulePassive

from spirit.game.card_effects import attacks_common as ac
from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES


async def _down_to(ctx, target, hp_left):
    hp = target.get_attribute(AttrID.HP, 0) or 0
    if hp > hp_left:
        await ctx.deal_damage(hp - hp_left, target=target, apply_modifiers=False, as_counters=True)


async def barite_jail(ctx):
    for p in list(ctx.opponent_bench()):
        if not ctx.effects_blocked(p):
            await _down_to(ctx, p, 100)


card = PokemonCardDef(
    guid="0085f6b7-3bc5-542d-9031-7d1be422b5b1",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Palossandex.Name",
    display_name="Palossand ex",
    searchable_by=["Palossand ex", "Stage 1", "ex", "Tera"],
    subtypes=["Stage 1", "ex", "Tera"],
    collector_number=91,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.RareHoloEX,
    hp=280,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Sandygast.Name",
    family_id=769,
    passive=TeraRulePassive(),
    abilities=[
        Attack(
            title="Sand Tomb",
            game_text="During your opponent's next turn, the Defending Pokémon can't retreat.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=160,
            effect=ac.condition_attack(no_retreat=True),
        ),
        Attack(
            title="Barite Jail",
            game_text="Put damage counters on each of your opponent's Benched Pokémon until its remaining HP is 100.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.PSYCHIC: 1, PokemonTypes.FIGHTING: 1},
            effect=barite_jail,
        ),
    ],
)
