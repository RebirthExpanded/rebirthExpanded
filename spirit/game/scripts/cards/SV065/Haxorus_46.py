"""Haxorus (SV065 46 -- JP SV6a 046; English SFA/46). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.session.effects import is_special_energy


async def bring_down_the_axe(ctx):
    d = ctx.opponent_active()
    if d is not None and not ctx.effects_blocked(d) and any(is_special_energy(e) for e in ctx.attached_energies(d)):
        await ctx.knock_out(d)


async def dragon_pulse(ctx):
    await ctx.deal_damage()
    top = list(ctx.deck_top(3))
    if top:
        await ctx.discard_cards(top)


card = PokemonCardDef(
    guid="edff2627-7af9-576d-8fd1-b8b964fa038e",
    key="SV065",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Haxorus.Name",
    display_name="Haxorus",
    searchable_by=["Haxorus", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=46,
    set_code="SV065",
    regulation_mark="H",
    rarity=Rarities.Rare,
    hp=170,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Fraxure.Name",
    family_id=610,
    abilities=[
        Attack(
            title="Bring Down the Axe",
            game_text="If your opponent's Active Pokémon has any Special Energy attached, it is Knocked Out.",
            cost={PokemonTypes.FIGHTING: 1},
            effect=bring_down_the_axe,
        ),
        Attack(
            title="Dragon Pulse",
            game_text="Discard the top 3 cards of your deck.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.METAL: 1},
            damage=230,
            effect=dragon_pulse,
        ),
    ],
)
