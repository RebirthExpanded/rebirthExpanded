"""Flygon (BWPJ 168 -- JP BWP 168; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac

from spirit.game.session.passives import Passive, carrier_pokemon


class SandGuardPassive(Passive):
    """Flip a coin whenever an opposing attack would damage this Pokemon;
    heads takes 40 off that damage."""

    async def damage_interceptor(self, ctx, calc, target, carrier):
        me = carrier_pokemon(carrier)
        if not (calc.is_attack and calc.is_opposing and calc.amount > 0) or target is not me:
            return None
        heads = await ctx.flip_coins(1, "Sand Guard", source=me)
        if heads and heads[0]:
            return max(0, calc.amount - 40)
        return None


card = PokemonCardDef(
    guid="834ba7ae-e3a4-5a92-8682-e6d0ce2232db",
    key="BWPJ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Flygon.Name",
    display_name="Flygon",
    searchable_by=["Flygon", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=168,
    set_code="BWPJ",
    rarity=Rarities.RarePromo,
    hp=140,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.DRAGON,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Vibrava.Name",
    family_id=328,
    abilities=[
        Ability(
            title="Sand Guard",
            game_text="Whenever this Pokémon would be damaged by an attack, flip a coin. If heads, it takes 40 less damage.",
            passive=SandGuardPassive(),
        ),
        Attack(
            title="Power Blast",
            game_text="Discard an Energy from this Pokémon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=ac.self_energy_discard_attack(1),
        ),
    ],
)
