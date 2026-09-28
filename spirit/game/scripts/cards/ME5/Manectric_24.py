from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import AttrID
from spirit.game.session.passives import Passive, carrier_pokemon


class _StageShield(Passive):
    """During the opponent's next turn: prevent all damage done to this
    Pokemon by attacks from Evolution Pokemon (damage only, not effects)."""

    def prevents_damage(self, calc, carrier):
        if not (calc.is_attack and calc.is_opposing) or calc.attacker is None:
            return False
        if carrier_pokemon(carrier) is not calc.target:
            return False
        basic = calc.attacker.get_attribute(AttrID.STAGE) == PokemonStage.BASIC.value
        return not basic


async def _shielded(ctx):
    await ctx.deal_damage()
    ctx.add_passive_through_opponents_turn(ctx.attacker, _StageShield())
    if ctx.attacker.entity_id not in ctx.visual_targets:
        ctx.visual_targets.append(ctx.attacker.entity_id)


async def sonic_edge(ctx):
    """110, not affected by any effects on the opponent's Active Pokemon."""
    await ctx.deal_damage(ignore_target_effects=True)

card = PokemonCardDef(
    guid="a828b923-e849-54c9-8a22-561cce5bac99",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Manectric.Name",
    display_name="Manectric",
    searchable_by=["Manectric", "Stage 1", "Manectric"],
    subtypes=["Stage 1"],
    collector_number=24,
    set_code="ME5",
    regulation_mark="J",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Electrike.Name",
    family_id=309,
    abilities=[
        Attack(
            title="Flashing Barrier",
            game_text="During your opponent's next turn, prevent all damage done to this Pok\u00e9mon by attacks from Evolution Pok\u00e9mon.",
            cost={PokemonTypes.LIGHTNING: 2},
            damage=50,
            effect=_shielded,
        ),
        Attack(
            title="Sonic Edge",
            game_text="This attack's damage isn't affected by any effects on your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.LIGHTNING: 3},
            damage=110,
            effect=sonic_edge,
        ),
    ],
)
