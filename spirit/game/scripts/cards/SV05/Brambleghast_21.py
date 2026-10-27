"""Brambleghast (SV05 21 -- JP SV5M 013; English TEF/21). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.session.passives import Passive, carrier_pokemon

from spirit.game.models.board import board_of


class ResilientSoulPassive(Passive):
    """+50 HP for each Prize card the opponent has taken (an Ability)."""

    def max_hp_bonus(self, pokemon, carrier):
        if pokemon is not carrier_pokemon(carrier):
            return 0
        board = board_of(pokemon)
        if board is None:
            return 0
        other = next((pid for pid in board.player_ids if pid != pokemon.owning_player_id), None)
        return 50 * board.prizes_taken(other) if other else 0


async def powerful_needles(ctx):
    n = len(ctx.attached_energies(ctx.attacker))
    heads = sum(1 for r in await ctx.flip_coins(n, "Powerful Needles") if r) if n else 0
    if heads:
        await ctx.deal_damage(80 * heads)


card = PokemonCardDef(
    guid="0f422444-fa58-5310-b872-9b5cd0fee177",
    key="SV05",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Brambleghast.Name",
    display_name="Brambleghast",
    searchable_by=["Brambleghast", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=21,
    set_code="SV05",
    regulation_mark="H",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Bramblin.Name",
    family_id=946,
    abilities=[
        Ability(
            title="Resilient Soul",
            game_text="This Pokémon gets +50 HP for each Prize card your opponent has taken.",
            passive=ResilientSoulPassive(),
        ),
        Attack(
            title="Powerful Needles",
            game_text="Flip a coin for each Energy attached to this Pokémon. This attack does 80 damage for each heads.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            damage_operator="x",
            effect=powerful_needles,
        ),
    ],
)
