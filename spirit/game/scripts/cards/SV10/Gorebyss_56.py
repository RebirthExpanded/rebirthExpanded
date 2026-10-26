"""Gorebyss (SV - Destined Rivals 56/182 -- JP SV10 025/098, the art here).

Stage 1 Water Pokemon (evolves from Clamperl). HP 90, weakness Lightning
x2, retreat 1.

  Crescendo Wave  [W]  30x  This attack does 30 damage for each Water
                            Energy attached to this Pokemon. Before doing
                            damage, you may attach any number of Basic
                            Water Energy cards from your hand to this
                            Pokemon.

The attaches come first and count (official Q&A: they can push the Energy
past Mr. Mime's Mimic Barrier count, and the damage is still done after
Gengar ex's curse counters Knock Gorebyss Out -- the Knock Out is handled
after the attack).
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import count_energy
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.data_utils import Attack, PokemonCardDef
from spirit.game.session.effects import is_energy_of_type

_water_on_self = count_energy("self", PokemonTypes.WATER)


async def crescendo_wave(ctx):
    me = ctx.attacker
    hand = [c for c in ctx.hand()
            if is_basic_energy_card(c) and is_energy_of_type(c, PokemonTypes.WATER)]
    if hand:
        picks = await ctx.choose_cards(
            hand, len(hand), minimum=0,
            prompt="Attach any number of Basic Water Energy cards to this Pokémon.")
        for energy in picks:
            await ctx.attach_energy(energy, me)
    await ctx.deal_damage(30 * _water_on_self(ctx))


card = PokemonCardDef(
    guid="2e002f24-1988-56b5-ad25-f7b631cf1be0",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gorebyss.Name",
    display_name="Gorebyss",
    searchable_by=["Gorebyss", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=56,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Clamperl.Name",
    family_id=366,
    abilities=[
        Attack(
            title="Crescendo Wave",
            game_text="This attack does 30 damage for each Water Energy attached to this Pokémon. Before doing damage, you may attach any number of Basic Water Energy cards from your hand to this Pokémon.",
            cost={PokemonTypes.WATER: 1},
            damage=30,
            damage_operator="x",
            effect=crescendo_wave,
        ),
    ],
)
