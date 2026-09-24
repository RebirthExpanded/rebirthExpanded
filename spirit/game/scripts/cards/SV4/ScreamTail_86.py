"""Scream Tail (SV - Paradox Rift 086/182 -- JP SV4K 032/066, the art here).

Basic Psychic Pokemon (Ancient). HP 90, weakness Darkness x2, resistance
Fighting -30, retreat 1.

  Slap            [C] 30
  Roaring Scream  [PC]  This attack does 20 damage to 1 of your
                        opponent's Pokemon for each damage counter on
                        this Pokemon. (Don't apply Weakness and
                        Resistance for Benched Pokemon.)

The counters are read when the attack resolves, so damage taken on the
way in makes it hit harder. The target is any of theirs, the Active
included -- the parenthetical only excuses the Bench, so Weakness still
applies in the Active Spot.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import damage_counters_on
from spirit.game.data_utils import Attack, PokemonCardDef

PER_COUNTER = 20
_counters = damage_counters_on("self")


async def roaring_scream(ctx):
    amount = PER_COUNTER * _counters(ctx)
    if amount <= 0:
        return
    candidates = ctx.opponent_pokemon_in_play()
    if not candidates:
        return
    picks = await ctx.choose_cards(
        candidates, 1, minimum=1,
        prompt=f"Choose a Pokémon to take {amount} damage")
    for target in picks:
        await ctx.deal_damage(amount, target=target)


card = PokemonCardDef(
    guid="ed9b0109-4ce1-58ef-a132-641a9b214af4",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ScreamTail.Name",
    display_name="Scream Tail",
    searchable_by=["Scream Tail", "Basic", "Ancient", "ScreamTail"],
    subtypes=["Basic", "Ancient"],
    collector_number=86,
    set_code="SV4",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=985,
    abilities=[
        Attack(
            title="Slap",
            game_text="",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
        Attack(
            title="Roaring Scream",
            game_text="This attack does 20 damage to 1 of your opponent's Pokémon for each damage counter on this Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            effect=roaring_scream,
        ),
    ],
)
