"""Firefighter Pikachu (JP SM-P promo, Pokemon Center Tokyo DX special box --
pool-local Promo_SM 903: no English print).

Basic Lightning Pokemon. HP 60, weakness Fighting x2, resistance Metal -20,
retreat 1.

  Extinguish [C]  Discard a [R] Energy from your opponent's Active Pokemon.
  Quick Attack [CC] 20+  Flip a coin. If heads, this attack does 10 more
                         damage.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import flip_damage
from spirit.game.card_effects.pokemon import energy_provides_type
from spirit.game.data_utils import Attack, PokemonCardDef


async def extinguish(ctx):
    defender = ctx.defender
    if defender is None or ctx.effects_blocked(defender):
        return
    fire = [e for e in ctx.attached_energies(defender)
            if energy_provides_type(e, PokemonTypes.FIRE.value)]
    if not fire:
        return
    picks = await ctx.choose_cards(fire, 1, minimum=1, prompt="Choose a [R] Energy to discard")
    if picks:
        await ctx.discard_cards(picks)


card = PokemonCardDef(
    guid="a84d28fc-9125-5a59-8483-8b7ccfa05c0b",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.FirefighterPikachu.Name",
    display_name="Firefighter Pikachu",
    searchable_by=["Firefighter Pikachu", "Basic", "Pikachu", "FirefighterPikachu"],
    subtypes=["Basic"],
    collector_number=903,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=60,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=25,
    abilities=[
        Attack(title="Extinguish",
               game_text="Discard a [R] Energy from your opponent's Active Pokémon.",
               cost={PokemonTypes.COLORLESS: 1}, effect=extinguish),
        Attack(title="Quick Attack",
               game_text="Flip a coin. If heads, this attack does 10 more damage.",
               cost={PokemonTypes.COLORLESS: 2},
               damage=20, damage_operator="+",
               effect=flip_damage(coins=1, base=20, bonus_per_heads=10)),
    ],
)
