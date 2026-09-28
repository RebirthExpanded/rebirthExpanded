from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import AttrID
from spirit.game.session.passives import Passive, carrier_pokemon


class _StageShield(Passive):
    """During the opponent's next turn: prevent all damage done to this
    Pokemon by attacks from Basic Pokemon (damage only, not effects)."""

    def prevents_damage(self, calc, carrier):
        if not (calc.is_attack and calc.is_opposing) or calc.attacker is None:
            return False
        if carrier_pokemon(carrier) is not calc.target:
            return False
        basic = calc.attacker.get_attribute(AttrID.STAGE) == PokemonStage.BASIC.value
        return basic


async def _shielded(ctx):
    await ctx.deal_damage()
    ctx.add_passive_through_opponents_turn(ctx.attacker, _StageShield())
    if ctx.attacker.entity_id not in ctx.visual_targets:
        ctx.visual_targets.append(ctx.attacker.entity_id)


async def riotous_blasting(ctx):
    """200; you may discard all Energy from this Pokemon for +130."""
    amount = 200
    energies = ctx.attached_energies(ctx.attacker)
    if energies and await ctx.ask_yes_no("Discard all Energy from this Pokémon for 130 more damage?"):
        await ctx.discard_cards(list(energies))
        amount += 130
    await ctx.deal_damage(amount)

card = PokemonCardDef(
    guid="62cf3e27-ab4d-5a9a-9746-b9fe7036aa84",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MegaManectricex.Name",
    display_name="Mega Manectric ex",
    searchable_by=["Mega Manectric ex", "Stage 1", "ex", "SV_Mega", "MegaManectricex"],
    subtypes=["Stage 1", "ex", "SV_Mega"],
    collector_number=50,
    set_code="ME1",
    regulation_mark="I",
    rarity=Rarities.RareHoloEX,
    hp=330,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Electrike.Name",
    family_id=309,
    abilities=[
        Attack(
            title="Flash Ray",
            game_text="During your opponent's next turn, prevent all damage done to this Pok\u00e9mon by attacks from Basic Pok\u00e9mon.",
            cost={PokemonTypes.LIGHTNING: 2},
            damage=120,
            effect=_shielded,
        ),
        Attack(
            title="Riotous Blasting",
            game_text="You may discard all Energy from this Pok\u00e9mon and have this attack do 130 more damage.",
            cost={PokemonTypes.LIGHTNING: 3},
            damage=200,
            damage_operator="+",
            effect=riotous_blasting,
        ),
    ],
)
