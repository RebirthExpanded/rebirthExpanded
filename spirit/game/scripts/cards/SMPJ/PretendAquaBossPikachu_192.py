"""Pretend Aqua Boss Pikachu (SMPJ 192 -- JP SMP 192; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import PokemonTypes
from spirit.game.card_effects.pokemon import energy_provides_type


def _discard_typed_energy(ptype):
    """Printed damage, then discard a [ptype] Energy from the opponent's Active."""
    async def effect(ctx):
        await ctx.deal_damage()
        defender = ctx.opponent_active()
        if defender is None or ctx.effects_blocked(defender):
            return
        typed = [e for e in ctx.attached_energies(defender) if energy_provides_type(e, ptype.value)]
        if not typed:
            return
        picks = await ctx.choose_cards(typed, 1, minimum=1, prompt="Choose an Energy to discard")
        if picks:
            await ctx.discard_cards(picks)
    return effect


card = PokemonCardDef(
    guid="084e12ab-7999-56f5-849a-3ae62a0b172d",
    key="SMPJ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.PretendAquaBossPikachu.Name",
    display_name="Pretend Aqua Boss Pikachu",
    searchable_by=["Pretend Aqua Boss Pikachu", "Basic"],
    subtypes=["Basic"],
    collector_number=192,
    set_code="SMPJ",
    regulation_mark="B",
    rarity=Rarities.RarePromo,
    hp=60,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=172,
    abilities=[
        Attack(
            title="Ocean Ambition?",
            game_text="Discard a [F] Energy from your opponent's Active Pokémon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            effect=_discard_typed_energy(PokemonTypes.FIGHTING),
        ),
        Attack(
            title="Pika Punch",
            game_text="",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
    ],
)
