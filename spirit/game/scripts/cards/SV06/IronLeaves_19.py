"""Iron Leaves (SV06 19 -- JP SV5a 007; English TWM/19). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac

from spirit.game.session.effects import is_pokemon_card


async def recovery_net(ctx):
    pool = [c for c in ctx.discard_pile() if is_pokemon_card(c)]
    if pool:
        picks = await ctx.choose_cards(pool, min(2, len(pool)), minimum=0, prompt="Choose up to 2 Pokémon")
        if picks:
            await ctx.put_in_hand(picks)


def _lost_one(ctx) -> bool:
    return ctx.kos_by_attack_last_turn() > 0


card = PokemonCardDef(
    guid="401ff997-dbca-52da-af85-f7f87e4b2511",
    key="SV06",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.IronLeaves.Name",
    display_name="Iron Leaves",
    searchable_by=["Iron Leaves", "Basic", "Future"],
    subtypes=["Basic", "Future"],
    collector_number=19,
    set_code="SV06",
    regulation_mark="H",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=1010,
    abilities=[
        Attack(
            title="Recovery Net",
            game_text="Put up to 2 Pokémon from your discard pile into your hand.",
            cost={PokemonTypes.GRASS: 1},
            effect=recovery_net,
        ),
        Attack(
            title="Avenging Edge",
            game_text="If any of your Pokémon were Knocked Out by damage from an attack during your opponent's last turn, this attack does 60 more damage.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
            damage_operator="+",
            effect=ac.bonus_if(_lost_one, 60),
        ),
    ],
)
