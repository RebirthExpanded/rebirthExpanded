"""Lanturn (SM - Celestial Storm 50/168 -- JP SM6b 021/066).

Stage 1 Lightning Pokemon, evolves from Chinchou. HP 110, weakness Fighting
x2, resistance Metal -20, retreat 2.

  Ability  Energy Grounding  When 1 of your Pokemon is Knocked Out by damage
                             from an opponent's attack, you may move a basic
                             Energy card from that Pokemon to this Pokemon.
  Lightning Strike  [LLC] 70+  You may discard all [L] Energy from this
                               Pokemon. If you do, this attack does 70 more
                               damage.

Jirachi V's Wish Connector shape (ON_ALLY_KNOCKED_OUT, before the stack
moves), with this Lanturn as the only destination.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.pokemon import energy_provides_type
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.data_utils import Triggers
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef


async def energy_grounding(ctx):
    ko = ctx.ko_pokemon
    if not ctx.ko_from_attack or ko is None or ko is ctx.source:
        return
    basics = [e for e in ctx.attached_energies(ko) if is_basic_energy_card(e)]
    if not basics:
        return
    if not await ctx.ask_yes_no("Energy Grounding: move a basic Energy card to Lanturn?"):
        return
    picks = await ctx.choose_cards(basics, 1, prompt="Choose a basic Energy card to move")
    if picks:
        await ctx.move_energy(picks[0], ctx.source)


async def lightning_strike(ctx):
    lightning = [e for e in ctx.attached_energies(ctx.source)
                 if energy_provides_type(e, PokemonTypes.LIGHTNING.value)]
    bonus = 0
    if lightning and await ctx.ask_yes_no(
            "Discard all Lightning Energy from Lanturn for 70 more damage?"):
        discarded = await ctx.discard_energy_from(
            ctx.source, 99,
            predicate=lambda e: energy_provides_type(e, PokemonTypes.LIGHTNING.value),
            prompt="Discard all Lightning Energy from this Pokémon")
        bonus = 70 if discarded else 0
    await ctx.deal_damage(70 + bonus)


card = PokemonCardDef(
    guid="03401d8c-dd33-5dcb-93ec-6d2ed55c5348",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lanturn.Name",
    display_name="Lanturn",
    searchable_by=['Lanturn', 'Stage 1', 'Lanturn'],
    subtypes=['Stage 1'],
    collector_number=50,
    set_code="SM7",
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Chinchou.Name",
    family_id=170,
    abilities=[
        Ability(
            title="Energy Grounding",
            game_text="When 1 of your Pokémon is Knocked Out by damage from an opponent's attack, you may move a basic Energy card from that Pokémon to this Pokémon.",
            trigger=Triggers.ON_ALLY_KNOCKED_OUT,
            effect=energy_grounding,
        ),
        Attack(title="Lightning Strike", game_text="You may discard all Lightning Energy from this Pokémon. If you do, this attack does 70 more damage.",
               cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1}, damage=70, damage_operator="+",
               effect=lightning_strike),
    ],
)
