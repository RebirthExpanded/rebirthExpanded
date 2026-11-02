"""Pretend Magma Boss Pikachu (SMPJ 193 -- JP SMP 193; English Japan only). Japanese art.
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
    guid="f8ef430e-2320-554c-8c18-045c986a62b8",
    key="SMPJ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.PretendMagmaBossPikachu.Name",
    display_name="Pretend Magma Boss Pikachu",
    searchable_by=["Pretend Magma Boss Pikachu", "Basic"],
    subtypes=["Basic"],
    collector_number=193,
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
            title="Land Ambition?",
            game_text="Discard a [W] Energy from your opponent's Active Pokémon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            effect=_discard_typed_energy(PokemonTypes.WATER),
        ),
        Attack(
            title="Pika Punch",
            game_text="",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
    ],
)
