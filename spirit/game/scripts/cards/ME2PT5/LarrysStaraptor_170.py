"""Larry's Staraptor (ME2PT5 170 -- JP MC 592; English ASC/170, ASC/249). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac

from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES


def _burned_or_poisoned(ctx) -> bool:
    have = ctx.attacker.get_attribute(AttrID.SPECIAL_CONDITIONS) or []
    return any(CLIENT_SPECIAL_CONDITION_NAMES[c] in have
               for c in (SpecialConditions.BURNED, SpecialConditions.POISONED))


async def feathery_strike(ctx):
    await ctx.deal_damage()
    await ctx.discard_energy_units_from(ctx.attacker, 2, prompt="Choose 2 Energy to discard from this Pokémon", partial=True)
    await ac.snipe_attack(50, pool="bench")(ctx)


card = PokemonCardDef(
    guid="47cdaa46-279f-58fd-ace4-37b140c186f1",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LarrysStaraptor.Name",
    display_name="Larry's Staraptor",
    searchable_by=["Larry's Staraptor", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=170,
    set_code="ME2PT5",
    regulation_mark="J",
    rarity=Rarities.Rare,
    hp=150,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.LarrysStaravia.Name",
    family_id=396,
    abilities=[
        Attack(
            title="Facade",
            game_text="If this Pokémon is Burned or Poisoned, this attack does 100 more damage.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=60,
            damage_operator="+",
            effect=ac.bonus_if(_burned_or_poisoned, 100),
        ),
        Attack(
            title="Feathery Strike",
            game_text="Discard 2 Energy from this Pokémon, and this attack also does 50 damage to 1 of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.COLORLESS: 3},
            damage=150,
            effect=feathery_strike,
        ),
    ],
)
