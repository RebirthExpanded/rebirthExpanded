from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.data_utils import def_for
from spirit.game.card_effects.passives_common import is_in_active_spot
from spirit.game.card_effects.pokemon import has_printed_ability
from spirit.game.session.passives import Passive


def _is_team_rockets(pokemon) -> bool:
    name = getattr(def_for(pokemon.archetype_id), "display_name", "") or ""
    return name.startswith("Team Rocket's ")


class PotentGlarePassive(Passive):
    """While Active: the opponent can't play Pokemon with a printed Ability
    from hand (Bench or evolve), Team Rocket's Pokemon excepted."""

    def blocks_pokemon_play(self, card, player_id, carrier):
        if player_id == carrier.owning_player_id or not is_in_active_spot(carrier):
            return False
        return has_printed_ability(card) and not _is_team_rockets(card)


async def spinning_tail(ctx):
    """30 to each of the opponent's Pokemon."""
    for pokemon in list(ctx.opponent_pokemon_in_play()):
        await ctx.deal_damage(30, target=pokemon)

card = PokemonCardDef(
    guid="9cc0b8ad-a2b5-5b2f-842d-1202c9e587b7",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsArbok.Name",
    display_name="Team Rocket's Arbok",
    searchable_by=["Team Rocket's Arbok", "Stage 1", "TeamRocketsArbok"],
    subtypes=["Stage 1"],
    collector_number=113,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsEkans.Name",
    family_id=23,
    abilities=[
        Ability(
            title="Potent Glare",
            game_text="As long as this Pok\u00e9mon is in the Active Spot, your opponent can't play any Pok\u00e9mon that has an Ability from their hand, except for Team Rocket's Pok\u00e9mon.",
            passive=PotentGlarePassive(),
        ),
        Attack(
            title="Spinning Tail",
            game_text="This attack does 30 damage to each of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.DARKNESS: 3},
            damage=0,
            effect=spinning_tail,
        ),
    ],
)
