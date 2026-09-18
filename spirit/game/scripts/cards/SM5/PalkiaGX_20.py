"""Palkia-GX (SM - Ultra Prism 20/156 -- JP SM5+ 010/050, the art here).

Basic Water Pokemon-GX. HP 180, weakness Grass x2, no resistance,
retreat 3. When Knocked Out, the opponent takes 2 Prize cards.

  Spatial Control  [W]           Move any number of Energy from your
                                 Benched Pokemon to this Pokemon.
  Hydro Pressure   [CCC] 60+     This attack does 20 more damage for each
                                 [W] Energy attached to this Pokemon.
  Zero Vanish-GX   [WWWCC] 150   Shuffle all Energy from each of your
                                 opponent's Pokemon into their deck. (You
                                 can't use more than 1 GX attack in a game.)

Spatial Control is the free-move primitive (pick an Energy, stop any time)
with this Pokemon as the only destination. Hydro Pressure counts [W]
Energy as provided.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import count_energy, damage_per
from spirit.game.data_utils import Attack, PokemonCardDef


async def spatial_control(ctx):
    await ctx.move_energy_freely(
        ctx.my_bench(), [ctx.attacker],
        prompt="Choose an Energy to move to this Pokémon (or stop).")


async def zero_vanish_gx(ctx):
    await ctx.deal_damage()
    energies = [e for p in ctx.opponent_pokemon_in_play() for e in ctx.attached_energies(p)]
    if energies:
        await ctx.shuffle_into_deck(energies, ctx.opponent_id)


card = PokemonCardDef(
    guid="200ec94f-7db9-5302-941a-42f3638aa18b",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.PalkiaGX.Name",
    display_name="Palkia-GX",
    searchable_by=["Palkia-GX", "Basic", "GX", "PalkiaGX"],
    subtypes=["Basic", "GX"],
    collector_number=20,
    set_code="SM5",
    rarity=Rarities.RareUltra,
    hp=180,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    family_id=484,
    abilities=[
        Attack(
            title="Spatial Control",
            game_text="Move any number of Energy from your Benched Pokémon to this Pokémon.",
            cost={PokemonTypes.WATER: 1},
            effect=spatial_control,
        ),
        Attack(
            title="Hydro Pressure",
            game_text="This attack does 20 more damage for each [W] Energy attached to this Pokémon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
            damage_operator="+",
            effect=damage_per(count_energy("self", PokemonTypes.WATER), 20, base=60),
        ),
        Attack(
            title="Zero Vanish-GX",
            game_text="Shuffle all Energy from each of your opponent's Pokémon into their deck. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.WATER: 3, PokemonTypes.COLORLESS: 2},
            damage=150,
            gx=True,
            effect=zero_vanish_gx,
        ),
    ],
)
