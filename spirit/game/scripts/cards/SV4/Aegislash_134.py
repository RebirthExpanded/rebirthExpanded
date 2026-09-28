from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.data_utils import is_pokemon_ex, is_pokemon_v
from spirit.game.session.passives import Passive, carrier_pokemon


class MysteriousShieldPassive(Passive):
    """No damage from attacks by the opponent's Pokemon ex and Pokemon V."""

    def prevents_damage(self, calc, carrier):
        if not (calc.is_attack and calc.is_opposing) or calc.attacker is None:
            return False
        if carrier_pokemon(carrier) is not calc.target:
            return False
        aid = calc.attacker.archetype_id
        return is_pokemon_ex(aid) or is_pokemon_v(aid)


async def hard_bashing(ctx):
    """120, not affected by any effects on the opponent's Active Pokemon."""
    await ctx.deal_damage(ignore_target_effects=True)

card = PokemonCardDef(
    guid="4cad3ff3-dbcf-5791-b782-24ba593fa341",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Aegislash.Name",
    display_name="Aegislash",
    searchable_by=["Aegislash", "Stage 2", "Aegislash"],
    subtypes=["Stage 2"],
    collector_number=134,
    set_code="SV4",
    regulation_mark="G",
    rarity=Rarities.Rare,
    hp=150,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Doublade.Name",
    family_id=679,
    abilities=[
        Ability(
            title="Mysterious Shield",
            game_text="Prevent all damage done to this Pok\u00e9mon by attacks from your opponent's Pok\u00e9mon ex and Pok\u00e9mon V.",
            passive=MysteriousShieldPassive(),
        ),
        Attack(
            title="Hard Bashing",
            game_text="This attack's damage isn't affected by any effects on your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=hard_bashing,
        ),
    ],
)
