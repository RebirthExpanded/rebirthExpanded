from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import AttrID
from spirit.game.session.effects import is_pokemon_card


def _evolution_card(card) -> bool:
    return is_pokemon_card(card) and card.get_attribute(AttrID.STAGE) != PokemonStage.BASIC.value


async def evolution_jammer(ctx):
    """30; the opponent can't evolve from hand during their next turn."""
    await ctx.deal_damage()
    ctx.lock_plays(ctx.opponent_id, _evolution_card)

card = PokemonCardDef(
    guid="89db4cda-7561-5328-8cb9-4dd2e8ada80a",
    key="SV05",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bronzong.Name",
    display_name="Bronzong",
    searchable_by=["Bronzong", "Stage 1", "Bronzong"],
    subtypes=["Stage 1"],
    collector_number=69,
    set_code="SV05",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Bronzor.Name",
    family_id=436,
    abilities=[
        Attack(
            title="Evolution Jammer",
            game_text="During your opponent's next turn, they can't play any Pok\u00e9mon from their hand to evolve their Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=30,
            effect=evolution_jammer,
        ),
        Attack(
            title="Super Psy Bolt",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
        ),
    ],
)
