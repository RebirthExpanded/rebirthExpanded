"""Espathra (SV4 81 -- JP SV4M 033; English PAR/197, PAR/81). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.card_effects import passives_common as pc
from spirit.game.data_utils import def_for, subtypes_for


async def stance(ctx):
    if not getattr(ctx, "evolved_from_hand", True):
        return
    if await ctx.ask_yes_no("Use Stance?"):
        await pc.apply_protection(ctx, target=ctx.source, prevent=True, effects_too=True)


def _tulip(ctx) -> bool:
    return any(getattr(def_for(c.archetype_id), "display_name", "") == "Tulip" for c in ctx.discard_pile())


card = PokemonCardDef(
    guid="ac1a02f3-4bb1-5797-8349-bd5234f6b3a7",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Espathra.Name",
    display_name="Espathra",
    searchable_by=["Espathra", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=81,
    set_code="SV4",
    regulation_mark="G",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Flittle.Name",
    family_id=955,
    abilities=[
        Ability(
            title="Stance",
            game_text="When you play this Pokémon from your hand to evolve 1 of your Pokémon during your turn, you may prevent all damage from and effects of attacks from your opponent's Pokémon done to this Pokémon until the end of your opponent's next turn.",
            trigger=Triggers.ON_EVOLVE,
            effect=stance,
        ),
        Attack(
            title="Glittering Eyes",
            game_text="If Tulip is in your discard pile, this attack does 70 more damage.",
            cost={PokemonTypes.PSYCHIC: 2},
            damage=70,
            damage_operator="+",
            effect=ac.bonus_if(_tulip, 70),
        ),
    ],
)
