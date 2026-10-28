"""Raichu (SV045 19 -- JP SV2a 026; English MEW/26, PAF/132, PAF/19). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card


def _grounding_applies(ctx) -> bool:
    ko = getattr(ctx, "ko_pokemon", None)
    attacker = getattr(ctx, "ko_attacker", None)
    return (ko is not None and ko is not ctx.source and bool(getattr(ctx, "ko_from_attack", False))
            and attacker is not None and attacker.owning_player_id != ctx.source.owning_player_id)


async def electrical_grounding(ctx):
    ko = getattr(ctx, "ko_pokemon", None)
    if ko is None:
        return
    pool = [e for e in ctx.attached_energies(ko) if is_energy_of_type(e, PokemonTypes.LIGHTNING)]
    if not pool or not await ctx.ask_yes_no("Move a Lightning Energy from the Knocked Out Pokémon to this Pokémon?"):
        return
    picks = await ctx.choose_cards(pool, 1, minimum=1, prompt="Choose a Lightning Energy to move")
    if picks:
        await ctx.move_energy(picks[0], ctx.source)


card = PokemonCardDef(
    guid="e0ac0776-2eb1-5e89-ba52-c83afc591d56",
    key="SV045",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Raichu.Name",
    display_name="Raichu",
    searchable_by=["Raichu", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=19,
    set_code="SV045",
    regulation_mark="G",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pikachu.Name",
    family_id=172,
    abilities=[
        Ability(
            title="Electrical Grounding",
            game_text="When 1 of your Pokémon is Knocked Out by damage from an attack from your opponent's Pokémon, you may move a Lightning Energy from that Pokémon to this Pokémon.",
            trigger=Triggers.ON_ALLY_KNOCKED_OUT,
            trigger_applies=_grounding_applies,
            effect=electrical_grounding,
        ),
        Attack(
            title="Thunder",
            game_text="This Pokémon also does 50 damage to itself.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=180,
            effect=ac.recoil_attack(50),
        ),
    ],
)
