"""Blissey (SV1 145 -- JP SV1V 060; English SVI/145). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES
from spirit.game.attributes import SpecialConditions

from spirit.game.attributes import CLIENT_SPECIAL_CONDITION_NAMES

_BY_NAME = {name: cond for cond, name in CLIENT_SPECIAL_CONDITION_NAMES.items()}


def _nurse_condition(board, player_id, pokemon) -> bool:
    a = board.active_pokemon(player_id)
    return a is not None and bool(a.get_attribute(AttrID.SPECIAL_CONDITIONS) or [])


async def busybody_nurse(ctx):
    a = ctx.board.active_pokemon(ctx.player_id)
    if a is None:
        return
    for name in list(a.get_attribute(AttrID.SPECIAL_CONDITIONS) or []):
        if name in _BY_NAME:
            await ctx.cure_condition(a, _BY_NAME[name])


async def happy_cyclone(ctx):
    await ctx.deal_damage()
    pool = list(ctx.attached_energies(ctx.attacker))
    bench = ctx.my_bench()
    if pool and bench and ctx.attacker not in ctx.knockouts:
        target = await ctx.choose_pokemon(bench, "Choose a Benched Pokémon to move all Energy to")
        if target is not None:
            for e in pool:
                await ctx.move_energy(e, target)


card = PokemonCardDef(
    guid="719ba8aa-ac90-52f0-a361-ef45ec33d51a",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Blissey.Name",
    display_name="Blissey",
    searchable_by=["Blissey", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=145,
    set_code="SV1",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=150,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Chansey.Name",
    family_id=440,
    abilities=[
        Ability(
            title="Busybody Nurse",
            game_text="Once during your turn, you may use this Ability. Your Active Pokémon recovers from all Special Conditions.",
            activation=Activations.ONCE_PER_TURN,
            condition=_nurse_condition,
            effect=busybody_nurse,
        ),
        Attack(
            title="Happy Cyclone",
            game_text="Move all Energy from this Pokémon to 1 of your Benched Pokémon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=150,
            effect=happy_cyclone,
        ),
    ],
)
