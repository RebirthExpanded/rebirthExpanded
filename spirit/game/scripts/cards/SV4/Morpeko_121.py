"""Morpeko (SV4 121 -- JP SV4K 051; English PAR/121, PAR/206). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.session.passives import Passive, carrier_pokemon
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card

from spirit.game.models.board import EnergyEntity


class HungryHurryPassive(Passive):
    def modify_retreat_cost(self, cost, pokemon, carrier, board):
        if pokemon is carrier and not any(isinstance(c, EnergyEntity) for c in pokemon.children):
            return 0
        return cost


async def energizer_wheel(ctx):
    await ctx.deal_damage()
    pool = [e for e in ctx.attached_energies(ctx.attacker) if is_energy_of_type(e, PokemonTypes.DARKNESS)]
    bench = ctx.my_bench()
    if not pool or not bench or ctx.attacker in ctx.knockouts:
        return
    target = await ctx.choose_pokemon(bench, "Choose 1 of your Benched Pokémon")
    if target is None:
        return
    n = min(2, len(pool))
    picks = await ctx.choose_cards(pool, n, minimum=n, prompt="Choose 2 Darkness Energy to move")
    for e in picks:
        await ctx.move_energy(e, target)


card = PokemonCardDef(
    guid="b1af1e2d-1c7c-5aff-9c1d-47aa7d574542",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Morpeko.Name",
    display_name="Morpeko",
    searchable_by=["Morpeko", "Basic"],
    subtypes=["Basic"],
    collector_number=121,
    set_code="SV4",
    regulation_mark="G",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=877,
    abilities=[
        Ability(
            title="In a Hungry Hurry",
            game_text="If this Pokémon has no Energy attached, it has no Retreat Cost.",
            passive=HungryHurryPassive(),
        ),
        Attack(
            title="Energizer Wheel",
            game_text="Move 2 Darkness Energy from this Pokémon to 1 of your Benched Pokémon.",
            cost={PokemonTypes.DARKNESS: 2},
            damage=70,
            effect=energizer_wheel,
        ),
    ],
)
