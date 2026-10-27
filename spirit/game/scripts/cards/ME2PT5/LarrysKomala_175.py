"""Larry's Komala (ME2PT5 175 -- JP MC 619; English ASC/175). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.data_utils import def_for

from spirit.game.session.effects import is_energy_card


def _larrys(pokemon) -> bool:
    return pokemon is not None and (getattr(def_for(pokemon.archetype_id), "display_name", "") or "").startswith("Larry's ")


def _lethargic_ok(board, player_id, pokemon) -> bool:
    bench = board.find_player_area(player_id, "bench")
    hand = board.find_player_area(player_id, "hand")
    return (bench is not None and pokemon.parent is bench and _larrys(board.active_pokemon(player_id))
            and any(is_energy_card(c) for c in (hand.children if hand else [])))


async def lethargic_charge(ctx):
    active = ctx.my_active()
    pool = [c for c in ctx.hand() if is_energy_card(c)]
    if not pool or not _larrys(active):
        return
    picks = await ctx.choose_cards(pool, 1, minimum=0, prompt="Choose an Energy card to attach to your Active Larry's Pokémon")
    if picks:
        await ctx.attach_energy(picks[0], active)


async def dozing_draw(ctx):
    await ctx.apply_special_condition(ctx.attacker, SpecialConditions.ASLEEP)
    await ctx.draw_cards(2)


card = PokemonCardDef(
    guid="fee5bb72-5dfb-5c97-9957-fd302bc3db2f",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LarrysKomala.Name",
    display_name="Larry's Komala",
    searchable_by=["Larry's Komala", "Basic"],
    subtypes=["Basic"],
    collector_number=175,
    set_code="ME2PT5",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=775,
    abilities=[
        Ability(
            title="Lethargic Charge",
            game_text="Once during your turn, if this Pokémon is on your Bench, you may use this Ability. Attach an Energy card from your hand to your Active Larry's Pokémon.",
            activation=Activations.ONCE_PER_TURN,
            condition=_lethargic_ok,
            effect=lethargic_charge,
        ),
        Attack(
            title="Dozing Draw",
            game_text="This Pokémon is now Asleep. Draw 2 cards.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=dozing_draw,
        ),
    ],
)
