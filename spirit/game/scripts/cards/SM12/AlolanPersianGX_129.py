"""Alolan Persian-GX (SM - Cosmic Eclipse 129/236 -- JP SM11a 040/064).

Stage 1 Darkness Pokemon-GX. HP 200, weakness Fighting x2, resistance
Psychic -20, retreat 2. Evolves from Alolan Meowth.

  Ability  Smug Face  Prevent all effects of attacks, including damage,
                      done to this Pokemon by your opponent's TAG TEAM
                      Pokemon and Ultra Beasts, and by your opponent's
                      Pokemon that have any Special Energy attached to them.

  Claw Slash         [DCC] 120
  Stalking Claws-GX  [DCC]      This attack does 120 damage to 1 of your
                                opponent's Pokemon. This damage isn't
                                affected by Weakness, Resistance, or any
                                other effects on that Pokemon.

Smug Face is the first shield in the pool that reads the ATTACKER rather
than the target, so blocks_attack_effects now takes the attacking Pokemon
where the caller knows it (EffectContext.effects_blocked passes ctx.attacker)
and the older shields ignore the argument. The damage half needs no such
plumbing: DamageCalc has carried the attacker all along.

Three ways in, any one of them enough: a TAG TEAM, an Ultra Beast, or any
Pokemon carrying a Special Energy -- which is a live condition, so
discarding that Energy re-opens the attack the same turn.

Stalking Claws-GX is aimed damage that ignores everything on the way in:
no Weakness, no Resistance, and no effects on the target, which is what
ignore_target_effects is for -- another Alolan Persian-GX across the table
does not stop it.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Attack, PokemonCardDef, subtypes_for
from spirit.game.models.board import BoardState
from spirit.game.session.effects import is_special_energy
from spirit.game.session.passives import Passive, carrier_pokemon

SNIPE = 120


def _is_smug_face_attacker(pokemon) -> bool:
    """A TAG TEAM, an Ultra Beast, or anything holding a Special Energy.

    The attached cards are the Pokemon's own children, so this needs no
    board -- which is what lets the effect half of the shield answer with
    only the attacker in hand.
    """
    if pokemon is None:
        return False
    subtypes = subtypes_for(pokemon.archetype_id)
    if "TAG TEAM" in subtypes or "Ultra Beast" in subtypes:
        return True
    return any(is_special_energy(e)
               for e in BoardState.attached_energies(pokemon))


class SmugFacePassive(Passive):
    """Nothing from a TAG TEAM, an Ultra Beast or a Special-Energy holder
    reaches the carrier -- damage included."""

    def prevents_damage(self, calc, carrier):
        holder = carrier_pokemon(carrier)
        if holder is None or calc.target is not holder:
            return False
        if not (calc.is_attack and calc.is_opposing):
            return False
        return _is_smug_face_attacker(calc.attacker)

    def blocks_attack_effects(self, target, carrier, source=None):
        holder = carrier_pokemon(carrier)
        if holder is None or target is not holder:
            return False
        return _is_smug_face_attacker(source)


async def stalking_claws_gx(ctx):
    """120 to any one of their Pokemon, through everything."""
    targets = ctx.opponent_pokemon_in_play()
    if not targets:
        return
    target = await ctx.choose_pokemon(
        targets, "Choose 1 of your opponent's Pokémon.")
    if target is None:
        target = targets[0]
    await ctx.deal_damage(SNIPE, target=target, ignore_weakness=True,
                          ignore_resistance=True, ignore_target_effects=True)


card = PokemonCardDef(
    guid="f344796a-cafc-5889-b86d-8ad0ba56997b",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.AlolanPersianGX.Name",
    display_name="Alolan Persian-GX",
    searchable_by=["Alolan Persian-GX", "Stage 1", "GX", "AlolanPersianGX"],
    subtypes=["Stage 1", "GX"],
    collector_number=129,
    set_code="SM12",
    rarity=Rarities.RareHoloGX,
    hp=200,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.AlolanMeowth.Name",
    family_id=52,
    abilities=[
        Ability(
            title="Smug Face",
            game_text="Prevent all effects of attacks, including damage, done to this Pokémon by your opponent's TAG TEAM Pokémon and Ultra Beasts, and by your opponent's Pokémon that have any Special Energy attached to them.",
            passive=SmugFacePassive(),
        ),
        Attack(
            title="Claw Slash",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=120,
        ),
        Attack(
            title="Stalking Claws-GX",
            game_text="This attack does 120 damage to 1 of your opponent's Pokémon. This damage isn't affected by Weakness, Resistance, or any other effects on that Pokémon. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            gx=True,
            effect=stalking_claws_gx,
        ),
    ],
)
