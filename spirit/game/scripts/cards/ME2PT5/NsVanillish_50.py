from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import lock_defender_attacks


async def sheer_cold(ctx):
    """60; the Defending Pokemon can't attack during the opponent's next turn."""
    await ctx.deal_damage()
    lock_defender_attacks(ctx)

card = PokemonCardDef(
    guid="8fbf5650-1eb6-50c8-beab-683647f0a1af",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.NsVanillish.Name",
    display_name="N's Vanillish",
    searchable_by=["N's Vanillish", "Stage 1", "NsVanillish"],
    subtypes=["Stage 1"],
    collector_number=50,
    set_code="ME2PT5",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.NsVanillite.Name",
    family_id=582,
    abilities=[
        Attack(
            title="Flop",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
        Attack(
            title="Sheer Cold",
            game_text="During your opponent's next turn, the Defending Pok\u00e9mon can't use attacks.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=sheer_cold,
        ),
    ],
)
