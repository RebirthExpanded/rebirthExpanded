from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import AttrID
from spirit.game.card_effects.attacks_common import bonus_if


def _defender_evolved(ctx) -> bool:
    d = ctx.defender
    return d is not None and d.get_attribute(AttrID.STAGE) != PokemonStage.BASIC.value


async def axe_blast(ctx):
    """If the opponent's Active Pokemon is a Basic Pokemon, it is Knocked Out."""
    d = ctx.defender
    if d is None or d.get_attribute(AttrID.STAGE) != PokemonStage.BASIC.value:
        return
    if not ctx.effects_blocked(d):
        await ctx.knock_out(d)

card = PokemonCardDef(
    guid="afd88f20-dccf-5bb7-8b7b-f38940f90e08",
    key="ZSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Haxorus.Name",
    display_name="Haxorus",
    searchable_by=["Haxorus", "Stage 2", "Haxorus"],
    subtypes=["Stage 2"],
    collector_number=70,
    set_code="ZSV10PT5",
    regulation_mark="I",
    rarity=Rarities.Rare,
    hp=170,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Fraxure.Name",
    family_id=610,
    abilities=[
        Attack(
            title="Cross-Cut",
            game_text="If your opponent's Active Pok\u00e9mon is an Evolution Pok\u00e9mon, this attack does 80 more damage.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=80,
            damage_operator="+",
            effect=bonus_if(_defender_evolved, 80),
        ),
        Attack(
            title="Axe Blast",
            game_text="If your opponent's Active Pok\u00e9mon is a Basic Pok\u00e9mon, it is Knocked Out.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=0,
            effect=axe_blast,
        ),
    ],
)
