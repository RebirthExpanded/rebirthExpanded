from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import AttrID
from spirit.game.card_effects.attacks_common import snipe_attack


async def painful_sword(ctx):
    """Double the number of damage counters on each opposing Pokemon."""
    for pokemon in list(ctx.opponent_pokemon_in_play()):
        current = (ctx.max_hp(pokemon) - pokemon.get_attribute(AttrID.HP, 0)) // 10
        if current > 0:
            await ctx.deal_damage(current * 10, target=pokemon, apply_modifiers=False, as_counters=True)

card = PokemonCardDef(
    guid="c354d755-5297-5e8f-a455-3b203232cff9",
    key="XY9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Aegislash.Name",
    display_name="Aegislash",
    searchable_by=["Aegislash", "Stage 2", "Aegislash"],
    subtypes=["Stage 2"],
    collector_number=62,
    set_code="XY9",
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Doublade.Name",
    family_id=679,
    abilities=[
        Attack(
            title="Painful Sword",
            game_text="Double the number of damage counters on each of your opponent's Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=0,
            effect=painful_sword,
        ),
        Attack(
            title="Megaton Slash",
            game_text="This attack does 10 damage to 2 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 2},
            damage=100,
            effect=snipe_attack(10, count=2, also_base=True),
        ),
    ],
)
