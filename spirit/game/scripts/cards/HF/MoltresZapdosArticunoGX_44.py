"""Moltres & Zapdos & Articuno-GX (SM - Hidden Fates 44/68 -- JP SM12a 102/173, the art here).

Basic Colorless TAG TEAM Pokemon-GX. HP 300, weakness Lightning x2,
resistance Fighting -20, retreat 3.

  Trinity Burn    [RWLC] 210
  Sky Legend-GX   [C]+   Shuffle this Pokemon and all cards attached to it
                         into your deck. If this Pokemon has at least 1
                         extra [R], [W], and [L] Energy attached (in
                         addition to this attack's cost), this attack does
                         110 damage to 3 of your opponent's Pokemon. (Don't
                         apply Weakness and Resistance for Benched Pokemon.)

The extras are read before the shuffle (the Energy leaves with the
birds), asked as one question through attack_cost_satisfied: cost plus
one each of [R] [W] [L]. The shuffle is Aqua Return's; the executor
promotes a new Active afterwards. The 3 hits go through deal_damage's
default, so the Active takes Weakness/Resistance and the Bench does not.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Attack, PokemonCardDef
from spirit.game.session.effects import full_stack
from spirit.game.session.legal_actions import attack_cost_satisfied

SKY_LEGEND_DAMAGE = 110
SKY_LEGEND_TARGETS = 3
# The [C] cost plus one extra of each of [R], [W] and [L], asked at once.
_COST_PLUS_EXTRAS = {"Colorless": 1, "Fire": 1, "Water": 1, "Lightning": 1}


async def sky_legend_gx(ctx):
    attacker = ctx.attacker
    energies = ctx.attached_energies(attacker)
    extras = attack_cost_satisfied(_COST_PLUS_EXTRAS, energies, ctx.board)
    await ctx.shuffle_into_deck(full_stack(attacker), ctx.player_id)
    if not extras:
        return
    candidates = ctx.opponent_pokemon_in_play()
    if not candidates:
        return
    count = min(SKY_LEGEND_TARGETS, len(candidates))
    picks = await ctx.choose_cards(
        candidates, count, minimum=count,
        prompt="Choose 3 of your opponent's Pokémon to take 110 damage")
    for target in picks:
        await ctx.deal_damage(SKY_LEGEND_DAMAGE, target=target)


card = PokemonCardDef(
    guid="2b486905-3ab8-5189-886c-6222edb0e08d",
    key="HF",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MoltresZapdosArticunoGX.Name",
    display_name="Moltres & Zapdos & Articuno-GX",
    searchable_by=["Moltres & Zapdos & Articuno-GX", "Basic", "TAG TEAM", "GX",
                   "MoltresZapdosArticunoGX"],
    subtypes=["Basic", "TAG TEAM", "GX"],
    collector_number=44,
    set_code="HF",
    rarity=Rarities.RareHoloGX,
    hp=300,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=146,
    abilities=[
        Attack(
            title="Trinity Burn",
            game_text="",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.WATER: 1, PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=210,
        ),
        Attack(
            title="Sky Legend-GX",
            game_text="Shuffle this Pokémon and all cards attached to it into your deck. If this Pokémon has at least 1 extra [R], [W], and [L] Energy attached (in addition to this attack's cost), this attack does 110 damage to 3 of your opponent's Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.) (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.COLORLESS: 1},
            gx=True,
            effect=sky_legend_gx,
        ),
    ],
)
