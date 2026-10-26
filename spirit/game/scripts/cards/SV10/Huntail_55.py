"""Huntail (SV - Destined Rivals 55/182 -- JP SV10 024/098, the art here).

Stage 1 Water Pokemon (evolves from Clamperl). HP 110, weakness Lightning
x2, retreat 1.

  Diver's Catch  (Ability)  When 1 of your Water Pokemon is Knocked Out by
                            damage from an attack from your opponent's
                            Pokemon, you may put all Basic Water Energy
                            attached to that Pokemon into your hand instead
                            of the discard pile.
  Wave Splash  [WCC]  80

Lanturn's Energy Grounding shape (ON_ALLY_KNOCKED_OUT, before the stack
moves), plus ON_KNOCKED_OUT_IN_PLAY for Huntail itself, which is one of
"your Water Pokemon" too. Official Q&A: two Water Pokemon Knocked Out at
once both give their Energy back; an Ability lock (the opponent's Milotic)
stops it.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.data_utils import Ability, Attack, PokemonCardDef, Triggers
from spirit.game.session.effects import is_energy_of_type, is_pokemon_of_type


def _water_ko(ctx) -> bool:
    ko = getattr(ctx, "ko_pokemon", None)
    return bool(getattr(ctx, "ko_from_attack", False) and ko is not None
                and is_pokemon_of_type(ko, PokemonTypes.WATER))


async def divers_catch(ctx):
    if not _water_ko(ctx):
        return
    ko = ctx.ko_pokemon
    water = [e for e in ctx.attached_energies(ko)
             if is_basic_energy_card(e) and is_energy_of_type(e, PokemonTypes.WATER)]
    if not water:
        return
    if not await ctx.ask_yes_no(
            "Diver's Catch: put all Basic Water Energy from that Pokémon into your hand?"):
        return
    await ctx.put_in_hand(water)


card = PokemonCardDef(
    guid="251065eb-0a50-5189-b41f-f5c6b95b95c5",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Huntail.Name",
    display_name="Huntail",
    searchable_by=["Huntail", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=55,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Clamperl.Name",
    family_id=366,
    abilities=[
        Ability(
            title="Diver's Catch",
            game_text="When 1 of your Water Pokémon is Knocked Out by damage from an attack from your opponent's Pokémon, you may put all Basic Water Energy attached to that Pokémon into your hand instead of the discard pile.",
            trigger=(Triggers.ON_ALLY_KNOCKED_OUT, Triggers.ON_KNOCKED_OUT_IN_PLAY),
            trigger_applies=_water_ko,
            effect=divers_catch,
        ),
        Attack(
            title="Wave Splash",
            game_text="",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
        ),
    ],
)
