"""Anthea & Concordia (ME2PT5 182 -- JP M2a 173; English ASC/182, ASC/254). Japanese art.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import SupporterCardDef

from spirit.game.data_utils import def_for, subtypes_for


_SIX = ("N's Darmanitan", "N's Zoroark ex", "N's Vanilluxe", "N's Klinklang", "N's Reshiram", "N's Zekrom")


def _all_six(board, player_id, card=None) -> bool:
    names = {getattr(def_for(p.archetype_id), "display_name", "") for p in board.pokemon_in_play(player_id)}
    return all(n in names for n in _SIX)


def _ns(pokemon) -> bool:
    return (getattr(def_for(pokemon.archetype_id), "display_name", "") or "").startswith("N's ")


async def anthea_and_concordia(ctx):
    ctx.add_extra_prize_watcher(attacker_predicate=_ns,
                                target_predicate=lambda p: p.owning_player_id != ctx.player_id
                                and ctx.board.active_pokemon(p.owning_player_id) is p,
                                prizes=3)


card = SupporterCardDef(
    guid="c3411fa9-870e-5b28-b4ee-3bd7a4fc41ed",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AntheaConcordia.Name",
    display_name="Anthea & Concordia",
    searchable_by=["Anthea & Concordia", "Supporter"],
    subtypes=["Supporter"],
    collector_number=182,
    set_code="ME2PT5",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    condition=_all_six,
    effect=anthea_and_concordia,
)
