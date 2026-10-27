"""Archaludon ex (SV08 130 -- JP SV7a 037; English SSP/130, SSP/224, SSP/241). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.session.passives import Passive, carrier_pokemon
from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES


def _of_type(pokemon, t) -> bool:
    return t.value in (pokemon.get_attribute(AttrID.POKEMON_TYPES) or [])
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card


def _basic_metal(card):
    return is_basic_energy_card(card) and is_energy_of_type(card, PokemonTypes.METAL)



async def assemble_alloy(ctx):
    if not getattr(ctx, "evolved_from_hand", True):
        return
    targets = [p for p in ctx.my_pokemon_in_play() if _of_type(p, PokemonTypes.METAL)]
    pool = [c for c in ctx.discard_pile() if _basic_metal(c)]
    if not targets or not pool or not await ctx.ask_yes_no("Use Assemble Alloy?"):
        return
    picks = await ctx.choose_cards(pool, min(2, len(pool)), minimum=0, prompt="Attach up to 2 Basic Metal Energy cards")
    for card in picks:
        target = await ctx.choose_pokemon(targets, "Choose 1 of your Metal Pokémon")
        if target is not None:
            await ctx.attach_energy(card, target)


class _NoWeakness(Passive):
    def modify_weakness(self, calc, carrier):
        if calc.target is carrier_pokemon(carrier):
            calc.weakness_applies = False


async def metal_defender(ctx):
    await ctx.deal_damage()
    ctx.add_passive_through_opponents_turn(ctx.attacker, _NoWeakness())


card = PokemonCardDef(
    guid="e4413671-7248-527a-b66c-30dea3c848c4",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Archaludonex.Name",
    display_name="Archaludon ex",
    searchable_by=["Archaludon ex", "Stage 1", "ex"],
    subtypes=["Stage 1", "ex"],
    collector_number=130,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.RareHoloEX,
    hp=300,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Duraludon.Name",
    family_id=884,
    abilities=[
        Ability(
            title="Assemble Alloy",
            game_text="When you play this Pokémon from your hand to evolve 1 of your Pokémon during your turn, you may attach up to 2 Basic Metal Energy cards from your discard pile to your Metal Pokémon in any way you like.",
            trigger=Triggers.ON_EVOLVE,
            effect=assemble_alloy,
        ),
        Attack(
            title="Metal Defender",
            game_text="During your opponent's next turn, this Pokémon has no Weakness.",
            cost={PokemonTypes.METAL: 3},
            damage=220,
            effect=metal_defender,
        ),
    ],
)
