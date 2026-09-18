"""Electrode (XY - Evolutions 40/108 -- JP CP6 040/087).

Stage 1 Lightning Pokemon, evolves from Voltorb. HP 80, weakness Fighting
x2, resistance Metal -20, retreat 1.

  Ability  Buzzap Thunder  Once during your turn (before your attack), you
                           may Knock Out this Pokemon and attach it to one
                           of your [L] Pokemon as a Special Energy card.
                           This card provides 2 [L] Energy only while this
                           card is attached to a Pokemon.
  Head Bolt  [LLC] 70

The pool's first card that becomes an Energy card. Nothing is spawned or
swapped: the Electrode card ITSELF is Knocked Out (the opponent takes a
Prize for it), and once that knockout has resolved it is lifted out of the
discard pile onto the chosen Pokemon wearing an Energy's attributes --
ENERGY_INFO providing [L][L], the Special Energy flag, and acts_as_energy,
which is what attached_energies and the retreat payment read. The moment
it leaves play again (discarded, scooped, its holder Knocked Out),
clear_pokemon_effects strips all of that and it is an Electrode card in
whatever pile it lands in, as the rules have it.

The holder is chosen BEFORE the knockout, since a Prize taken for this
Pokemon can change the board; the attach itself waits for the knockout to
resolve, in the ability's deferred actions.
"""

from spirit.game.attributes import (AttrID, PokemonStage, PokemonTypes,
                                    Rarities)
from spirit.game.data_utils import (Ability, Activations, Attack,
                                    PokemonCardDef)
from spirit.game.session.effects import is_pokemon_of_type


def _lightning_pokemon_besides_self(board, player_id, pokemon) -> bool:
    return any(p is not pokemon and is_pokemon_of_type(p, PokemonTypes.LIGHTNING)
               for p in board.pokemon_in_play(player_id))


async def buzzap_thunder(ctx):
    """Knock this Pokemon Out, then wear it as [L][L] on a Lightning Pokemon."""
    electrode = ctx.source
    candidates = [p for p in ctx.my_pokemon_in_play()
                  if p is not electrode
                  and is_pokemon_of_type(p, PokemonTypes.LIGHTNING)]
    if not candidates:
        return
    if not await ctx.ask_yes_no(
            "Knock Out this Pokémon and attach it to one of your Lightning "
            "Pokémon as a Special Energy card?"):
        return
    holder = await ctx.choose_pokemon(
        candidates, "Choose a Lightning Pokémon to attach Electrode to")
    if holder is None:
        return
    await ctx.knock_out(electrode)

    async def _attach():
        # The knockout has resolved: the card is in the discard, the Prize
        # taken. Only a holder still in play can wear it.
        if holder not in ctx.board.pokemon_in_play(ctx.player_id):
            return
        electrode.acts_as_energy = True
        electrode.set_attribute(AttrID.ENERGY_INFO, {
            "options": [[PokemonTypes.LIGHTNING.value, PokemonTypes.LIGHTNING.value]]})
        electrode.set_attribute(AttrID.IS_SPECIAL_ENERGY, True)
        if not await ctx.attach_energy(electrode, holder):
            electrode.acts_as_energy = False
            electrode.set_attribute(AttrID.ENERGY_INFO, None)
            electrode.set_attribute(AttrID.IS_SPECIAL_ENERGY, False)
            return
        await ctx.flush_choreography()
    ctx.deferred_actions.append(_attach)


card = PokemonCardDef(
    guid="6d00dd22-605d-5d2b-8e2d-b6af2cc8ba04",
    key="XY12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Electrode.Name",
    display_name="Electrode",
    searchable_by=["Electrode", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=40,
    set_code="XY12",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Voltorb.Name",
    family_id=100,
    abilities=[
        Ability(
            title="Buzzap Thunder",
            game_text="Once during your turn (before your attack), you may Knock Out this Pokémon and attach it to one of your Lightning Pokémon as a Special Energy card. This card provides 2 Lightning Energy only while this card is attached to a Pokémon.",
            activation=Activations.ONCE_PER_TURN,
            condition=_lightning_pokemon_besides_self,
            effect=buzzap_thunder,
            self_knockout=True,
        ),
        Attack(
            title="Head Bolt",
            game_text="",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=70,
        ),
    ],
)
