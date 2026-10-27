"""Dachsbun ex (SV07 67 -- JP SV7 046; English SCR/160, SCR/169, SCR/67). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac
from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES

from spirit.game.session.passives import effective_max_hp


def _counters(board, pokemon) -> int:
    return max(0, effective_max_hp(board, pokemon) - pokemon.get_attribute(AttrID.HP, 0)) // 10

from spirit.game.session.effects import is_evolution_pokemon


async def time_to_chow_down(ctx):
    if not getattr(ctx, "evolved_from_hand", True):
        return
    pool = [p for p in ctx.my_pokemon_in_play() if is_evolution_pokemon(p) and _counters(ctx.board, p) > 0]
    if not pool or not await ctx.ask_yes_no("Use Time to Chow Down?"):
        return
    for p in pool:
        await ctx.heal(_counters(ctx.board, p) * 10, p)
        energy = list(ctx.attached_energies(p))
        if energy:
            await ctx.discard_cards(energy)


card = PokemonCardDef(
    guid="19c8d203-ec77-5235-9ecb-586b2c4579d1",
    key="SV07",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dachsbunex.Name",
    display_name="Dachsbun ex",
    searchable_by=["Dachsbun ex", "Stage 1", "ex"],
    subtypes=["Stage 1", "ex"],
    collector_number=67,
    set_code="SV07",
    regulation_mark="H",
    rarity=Rarities.RareHoloEX,
    hp=250,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Fidough.Name",
    family_id=926,
    abilities=[
        Ability(
            title="Time to Chow Down",
            game_text="When you play this Pokémon from your hand to evolve 1 of your Pokémon during your turn, you may heal all damage from each of your Evolution Pokémon. If you healed any damage in this way, discard all Energy from those Pokémon.",
            trigger=Triggers.ON_EVOLVE,
            effect=time_to_chow_down,
        ),
        Attack(
            title="Wonder Shine",
            game_text="Your opponent's Active Pokémon is now Confused.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=130,
            effect=ac.condition_attack(SpecialConditions.CONFUSED),
        ),
    ],
)
