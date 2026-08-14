from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.passives_common import TakesLessPassive, protect_next_turn
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.card_effects.trainers import is_basic_energy_card

async def protect_charge(ctx):
    """150. During your opponent's next turn, this Pokémon takes 30 less
    damage from attacks (after applying Weakness and Resistance)."""
    await ctx.deal_damage()
    ctx.add_passive_through_opponents_turn(ctx.attacker, TakesLessPassive(30))

card = PokemonCardDef(
    guid="0a18cf29-cd0c-5a33-bc05-719b698cef61",
    key="ZSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Genesectex.Name",
    display_name="Genesect ex",
    searchable_by=["Genesect ex","Basic","ex","Genesectex"],
    subtypes=["Basic","ex"],
    collector_number=67,
    set_code="ZSV10PT5",
    regulation_mark="I",
    rarity=Rarities.RareHoloEX,
    hp=220,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    abilities=[
        Ability(
            title="Metallic Signal",
            game_text="Once during your turn, you may search your deck for up to 2 Evolution Metal Pokémon, reveal them, and put them into your hand. Then, shuffle your deck.",
            activation=Activations.ONCE_PER_TURN,
            effect=search_to_hand(,
        ),
        Attack(
            title="Protect Charge",
            game_text="During your opponent's next turn, this Pokémon takes 30 less damage from attacks (after applying Weakness and Resistance).",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=150,
            effect=protect_charge,
        ),
    ],
)
