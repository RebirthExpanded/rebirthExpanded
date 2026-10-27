"""Munkidori ex (SV065 37 -- JP SV6a 037; English SFA/37, SFA/83, SFA/91). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.session.passives import Passive, carrier_pokemon
from spirit.game.data_utils import def_for, subtypes_for



class OhNoYouDontPassive(Passive):
    """KO'd by an opposing attack's damage with Pecharunt ex in play: one
    fewer Prize card."""

    def modify_prizes_for_knockout(self, pokemon, ctx, count, carrier):
        if pokemon is not carrier_pokemon(carrier):
            return count
        attacker = getattr(ctx, "ko_attacker", None)
        if not (getattr(ctx, "ko_from_attack", False) and attacker is not None
                and attacker.owning_player_id != pokemon.owning_player_id):
            return count
        board = ctx.board
        if any(getattr(def_for(p.archetype_id), "display_name", "") == "Pecharunt ex"
               for p in board.pokemon_in_play(pokemon.owning_player_id)):
            return max(0, count - 1)
        return count


card = PokemonCardDef(
    guid="b24d83ff-3a06-5eae-95df-8932356e7b15",
    key="SV065",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Munkidoriex.Name",
    display_name="Munkidori ex",
    searchable_by=["Munkidori ex", "Basic", "ex"],
    subtypes=["Basic", "ex"],
    collector_number=37,
    set_code="SV065",
    regulation_mark="H",
    rarity=Rarities.RareHoloEX,
    hp=210,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=1015,
    abilities=[
        Ability(
            title="Oh No You Don't",
            game_text="If this Pokémon is Knocked Out by damage from an attack from your opponent's Pokémon, and if you have any Pecharunt ex in play, your opponent takes 1 fewer Prize card.",
            passive=OhNoYouDontPassive(),
        ),
        Attack(
            title="Dirty Headbutt",
            game_text="During your next turn, this Pokémon can't use Dirty Headbutt.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=190,
            locks_next_turn=True,
        ),
    ],
)
