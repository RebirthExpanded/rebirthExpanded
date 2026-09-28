from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities


async def soul_destroyer(ctx):
    """Knock Out each opposing Pokemon with 50 HP or less remaining."""
    for pokemon in list(ctx.opponent_pokemon_in_play()):
        if pokemon.get_attribute(AttrID.HP, 0) <= 50 and not ctx.effects_blocked(pokemon):
            await ctx.knock_out(pokemon)

card = PokemonCardDef(
    guid="515e839b-3e9a-5e8b-a911-b4b7c5a92610",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Yveltalex.Name",
    display_name="Yveltal ex",
    searchable_by=["Yveltal ex", "Basic", "ex", "Yveltalex"],
    subtypes=["Basic", "ex"],
    collector_number=53,
    set_code="ME3",
    regulation_mark="J",
    rarity=Rarities.RareHoloEX,
    hp=210,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=717,
    abilities=[
        Attack(
            title="Soul Destroyer",
            game_text="Knock Out each of your opponent's Pok\u00e9mon that has 50 HP or less remaining.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=0,
            effect=soul_destroyer,
        ),
        Attack(
            title="Dark Strike",
            game_text="During your next turn, this Pok\u00e9mon can't use Dark Strike.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=210,
            locks_next_turn=True,
        ),
    ],
)
