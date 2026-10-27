"""N's Vanilluxe (ME2PT5 51 -- JP M2a 039; English ASC/51). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES

from spirit.game.session.passives import effective_max_hp


def _counters(board, pokemon) -> int:
    return max(0, effective_max_hp(board, pokemon) - pokemon.get_attribute(AttrID.HP, 0)) // 10


async def snow_coating(ctx):
    for p in list(ctx.opponent_pokemon_in_play()):
        n = _counters(ctx.board, p)
        if n and not ctx.effects_blocked(p):
            await ctx.deal_damage(10 * n, target=p, apply_modifiers=False, as_counters=True)


card = PokemonCardDef(
    guid="7092506d-52ef-5ef4-887f-0c62fb133324",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.NsVanilluxe.Name",
    display_name="N's Vanilluxe",
    searchable_by=["N's Vanilluxe", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=51,
    set_code="ME2PT5",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=150,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.NsVanillish.Name",
    family_id=582,
    abilities=[
        Attack(
            title="Snow Coating",
            game_text="Double the number of damage counters on each of your opponent's Pokémon.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=snow_coating,
        ),
        Attack(
            title="Blizzard",
            game_text="This attack also does 10 damage to each of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=120,
            effect=ac.spread_damage(10, also_base=True),
        ),
    ],
)
