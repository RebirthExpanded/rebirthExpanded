from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.data_utils import subtypes_for
from spirit.game.card_effects.attacks_common import count_in_play, damage_per


def _ancient(pokemon) -> bool:
    return "Ancient" in subtypes_for(pokemon.archetype_id)


async def shred(ctx):
    """130, not affected by any effects on the opponent's Active Pokemon."""
    await ctx.deal_damage(ignore_target_effects=True)

card = PokemonCardDef(
    guid="3c6257ca-9ee0-5770-9cb3-3a1abf02a2ec",
    key="SV05",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Koraidon.Name",
    display_name="Koraidon",
    searchable_by=["Koraidon", "Basic", "Ancient", "Koraidon"],
    subtypes=["Basic", "Ancient"],
    collector_number=119,
    set_code="SV05",
    regulation_mark="H",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    family_id=1007,
    abilities=[
        Attack(
            title="Primordial Beatdown",
            game_text="This attack does 30 damage for each of your Ancient Pok\u00e9mon in play.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="x",
            effect=damage_per(count_in_play("mine", _ancient), 30),
        ),
        Attack(
            title="Shred",
            game_text="This attack's damage isn't affected by any effects on your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=130,
            effect=shred,
        ),
    ],
)
