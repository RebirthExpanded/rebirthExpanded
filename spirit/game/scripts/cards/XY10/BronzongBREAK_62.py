"""Bronzong BREAK (XY - Fates Collide 62/124 -- JP XY9-B 049/080).

BREAK Evolution of Bronzong. HP 130; keeps Bronzong's attacks, Ability,
Weakness, Resistance and Retreat Cost.

  Metal Rain  [MC]  Discard as many [M] Energy attached to this Pokemon as
                    you like. For each Energy card discarded in this way,
                    choose 1 of your opponent's Pokemon and do 30 damage
                    to it. Don't apply Weakness and Resistance. (You may
                    choose the same Pokemon more than once.)
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.pokemon import is_metal_energy
from spirit.game.data_utils import Attack, PokemonCardDef


async def metal_rain(ctx):
    attacker = ctx.attacker
    metal = [e for e in ctx.board.attached_energies(attacker) if is_metal_energy(e)]
    if not metal:
        return
    picks = await ctx.choose_cards(metal, len(metal), minimum=0,
                                   prompt="Choose any amount of [M] Energy to discard.")
    if not picks:
        return
    await ctx.discard_cards(picks)
    targets = ctx.opponent_pokemon_in_play()
    if not targets:
        return
    tally = {}
    for _ in picks:
        chosen = await ctx.choose_pokemon(targets, "Choose 1 of your opponent's Pokémon to damage.")
        if chosen is None:
            chosen = targets[0]
        tally[chosen.entity_id] = tally.get(chosen.entity_id, 0) + 1
    for target in targets:
        hits = tally.get(target.entity_id, 0)
        if hits:
            await ctx.deal_damage(30 * hits, target=target,
                                  ignore_weakness=True, ignore_resistance=True)


card = PokemonCardDef(
    guid="b851b9c0-e0f8-58db-a01e-bc32a7feec80",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.BronzongBREAK.Name",
    display_name="Bronzong BREAK",
    searchable_by=["Bronzong BREAK", "BREAK", "BronzongBREAK"],
    subtypes=["BREAK"],
    collector_number=62,
    set_code="XY10",
    rarity=Rarities.BreakRare,
    hp=130,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BREAK,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Bronzong.Name",
    family_id=436,
    abilities=[
        Attack(title="Metal Rain",
               game_text="Discard as many [M] Energy attached to this Pokémon as you like. For each Energy card discarded in this way, choose 1 of your opponent's Pokémon and do 30 damage to it. Don't apply Weakness and Resistance. (You may choose the same Pokémon more than once.)",
               cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1}, damage=0,
               effect=metal_rain),
    ],
)
