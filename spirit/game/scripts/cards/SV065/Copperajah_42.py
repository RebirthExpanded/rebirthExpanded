"""Copperajah (SV065 42 -- JP SV6a 042; English SFA/42). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.session.passives import Passive, carrier_pokemon
from spirit.game.card_effects import passives_common as pc
from spirit.game.card_effects import attacks_common as ac

from spirit.game.session.effects import is_stadium_card


class MassiveBodyPassive(Passive):
    """Active: the opponent can't play Stadium cards from their hand."""

    def blocks_trainer_play(self, card, player_id, carrier):
        return player_id != carrier.owning_player_id and is_stadium_card(card) and pc.is_in_active_spot(carrier)


async def nasal_lariat(ctx):
    if await ctx.ask_yes_no("Do 100 more damage? (This Pokémon can't attack during your next turn.)"):
        await ctx.deal_damage(230)
        ac.lock_all_attacks(ctx, ctx.attacker)
    else:
        await ctx.deal_damage(130)


card = PokemonCardDef(
    guid="c905a241-6529-586c-bc46-8c7ce6a70dae",
    key="SV065",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Copperajah.Name",
    display_name="Copperajah",
    searchable_by=["Copperajah", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=42,
    set_code="SV065",
    regulation_mark="H",
    rarity=Rarities.Rare,
    hp=200,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Cufant.Name",
    family_id=878,
    abilities=[
        Ability(
            title="Massive Body",
            game_text="As long as this Pokémon is in the Active Spot, your opponent can't play any Stadium cards from their hand.",
            passive=MassiveBodyPassive(),
        ),
        Attack(
            title="Nasal Lariat",
            game_text="You may do 100 more damage. If you do, during your next turn, this Pokémon can't attack.",
            cost={PokemonTypes.METAL: 3, PokemonTypes.COLORLESS: 1},
            damage=130,
            damage_operator="+",
            effect=nasal_lariat,
        ),
    ],
)
