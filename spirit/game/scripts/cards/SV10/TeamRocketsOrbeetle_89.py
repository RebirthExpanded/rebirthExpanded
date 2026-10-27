"""Team Rocket's Orbeetle (SV10 89 -- JP SV10 044; English DRI/198, DRI/89). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.data_utils import def_for, subtypes_for


def _named(prefix):
    def pred(card) -> bool:
        return card is not None and (getattr(def_for(card.archetype_id), "display_name", "") or "").startswith(prefix)
    return pred


def _name_has(*parts):
    def pred(card) -> bool:
        name = (getattr(def_for(card.archetype_id), "display_name", "") or "") if card is not None else ""
        return any(p in name for p in parts)
    return pred
from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES

from spirit.game.session.passives import effective_max_hp


def _damaged_rockets(board, player_id):
    return [p for p in board.pokemon_in_play(player_id)
            if _named("Team Rocket's ")(p) and p.get_attribute(AttrID.HP, 0) < effective_max_hp(board, p)]


def _rocket_brain_condition(board, player_id, pokemon) -> bool:
    return len(board.pokemon_in_play(player_id)) >= 2 and bool(_damaged_rockets(board, player_id))


async def rocket_brain(ctx):
    sources = _damaged_rockets(ctx.board, ctx.player_id)
    if not sources:
        return
    source = await ctx.choose_pokemon(sources, "Choose a Team Rocket's Pokémon to move a damage counter from")
    if source is None:
        return
    dests = [p for p in ctx.my_pokemon_in_play() if p is not source]
    dest = await ctx.choose_pokemon(dests, "Choose a Pokémon to move the damage counter to") if dests else None
    if dest is not None:
        await ctx.move_damage_counters(source, dest, max_count=1)


card = PokemonCardDef(
    guid="25866ba1-92f8-50a8-8e6a-f554b7cd401f",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsOrbeetle.Name",
    display_name="Team Rocket's Orbeetle",
    searchable_by=["Team Rocket's Orbeetle", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=89,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsDottler.Name",
    family_id=824,
    abilities=[
        Ability(
            title="Rocket Brain",
            game_text="As often as you like during your turn, you may move 1 damage counter from 1 of your Team Rocket's Pokémon to another of your Pokémon.",
            activation=Activations.UNLIMITED,
            condition=_rocket_brain_condition,
            effect=rocket_brain,
        ),
        Attack(
            title="Psychic",
            game_text="This attack does 40 more damage for each Energy attached to your opponent's Active Pokémon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            damage_operator="+",
            effect=ac.damage_per(ac.count_energy("defender"), 40, base=40),
        ),
    ],
)
