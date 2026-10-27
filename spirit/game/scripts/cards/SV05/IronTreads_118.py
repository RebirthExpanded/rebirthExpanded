"""Iron Treads (SV05 118 -- JP SV5M 051; English TEF/118). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.session.passives import Passive, carrier_pokemon
from spirit.game.data_utils import def_for, subtypes_for


async def _move_one_energy_to_bench(ctx, pred=None):
    pool = [e for e in ctx.attached_energies(ctx.attacker) if pred is None or pred(e)]
    bench = ctx.my_bench()
    if not pool or not bench or ctx.attacker in ctx.knockouts:
        return
    picks = await ctx.choose_cards(pool, 1, minimum=1, prompt="Choose an Energy to move")
    dest = await ctx.choose_pokemon(bench, "Choose a Benched Pokémon to move it to") if picks else None
    if dest is not None:
        await ctx.move_energy(picks[0], dest)



class DualCorePassive(Passive):
    """Future Booster Energy Capsule attached: Fighting and Metal type."""

    def modify_pokemon_types(self, types, pokemon, carrier):
        if pokemon is not carrier_pokemon(carrier):
            return types
        if not any(getattr(def_for(c.archetype_id), "display_name", "") == "Future Booster Energy Capsule"
                   for c in pokemon.children):
            return types
        return [PokemonTypes.FIGHTING.value, PokemonTypes.METAL.value]


async def wheel_pass(ctx):
    await ctx.deal_damage()
    await _move_one_energy_to_bench(ctx)


card = PokemonCardDef(
    guid="7751b567-2d77-5393-9e90-cef4c46f10ea",
    key="SV05",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.IronTreads.Name",
    display_name="Iron Treads",
    searchable_by=["Iron Treads", "Basic", "Future"],
    subtypes=["Basic", "Future"],
    collector_number=118,
    set_code="SV05",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    family_id=990,
    abilities=[
        Ability(
            title="Dual Core",
            game_text="As long as this Pokémon has a Future Booster Energy Capsule attached, it is Fighting and Metal type.",
            passive=DualCorePassive(),
        ),
        Attack(
            title="Wheel Pass",
            game_text="Move an Energy from this Pokémon to 1 of your Benched Pokémon.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
            effect=wheel_pass,
        ),
    ],
)
