"""Lugia-EX (BW - Plasma Storm 108/135 -- JP BW7-B 059/070, Plasma Gale).

Team Plasma Basic Colorless Pokemon-EX. HP 180, weakness Lightning x2,
resistance Fighting -20, retreat 2.

  Ability  Overflow  If your opponent's Pokemon is Knocked Out by damage
                     from an attack of this Pokemon, take 1 more Prize card.
  Plasma Gale  [CCCC] 120  Discard a Plasma Energy attached to this Pokemon.
                           If you can't, this attack does nothing.

Overflow is an extra_prizes_for_knockout passive (Togekiss SV08's hook)
gated on this Lugia-EX's own attack damage.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Attack, PokemonCardDef, def_for
from spirit.game.session.passives import Passive, carrier_pokemon


class OverflowPassive(Passive):
    async def extra_prizes_for_knockout(self, pokemon, ctx, count, carrier):
        lugia = carrier_pokemon(carrier)
        if lugia is None or pokemon.owning_player_id == lugia.owning_player_id:
            return 0
        if not ctx.is_attack_effect() or ctx.attacker is not lugia:
            return 0
        return 1 if pokemon.entity_id in ctx.attack_damage else 0


def _is_plasma_energy(card) -> bool:
    return getattr(def_for(card.archetype_id), "display_name", None) == "Plasma Energy"


async def plasma_gale(ctx):
    plasma = [e for e in ctx.attached_energies(ctx.attacker) if _is_plasma_energy(e)]
    if not plasma:
        return
    picks = plasma if len(plasma) == 1 else await ctx.choose_cards(
        plasma, 1, minimum=1, prompt="Choose a Plasma Energy to discard")
    if not picks:
        return
    await ctx.discard_cards(picks)
    await ctx.deal_damage()


card = PokemonCardDef(
    guid="805da86d-26b1-547e-8047-1e16bb501e1f",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LugiaEX.Name",
    display_name="Lugia-EX",
    searchable_by=["Lugia-EX", "Basic", "EX", "Team Plasma", "LugiaEX"],
    subtypes=["Basic", "EX", "Team Plasma"],
    collector_number=108,
    set_code="BW8",
    rarity=Rarities.RareHoloEX,
    hp=180,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=249,
    abilities=[
        Ability(
            title="Overflow",
            game_text="If your opponent's Pokémon is Knocked Out by damage from an attack of this Pokémon, take 1 more Prize card.",
            passive=OverflowPassive(),
        ),
        Attack(
            title="Plasma Gale",
            game_text="Discard a Plasma Energy attached to this Pokémon. If you can't, this attack does nothing.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=120,
            effect=plasma_gale,
        ),
    ],
)
