from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.data_utils import is_pokemon_ex
from spirit.game.session.effects import live_pokemon_types
from spirit.game.session.passives import Passive


class ShadowyConcealmentPassive(Passive):
    """Your [D] Pokemon KO'd by attack damage from an opposing Pokemon ex give
    up 1 fewer Prize card. Doesn't stack: the knockout's ctx remembers which
    Pokemon already had its count lowered (Legendary Summit's shape)."""

    def modify_prizes_for_knockout(self, pokemon, ctx, count, carrier):
        if pokemon.owning_player_id != carrier.owning_player_id:
            return count
        if PokemonTypes.DARKNESS.value not in live_pokemon_types(pokemon):
            return count
        attacker = getattr(ctx, "attacker", None)
        if not ctx.is_attack_effect() or attacker is None:
            return count
        if attacker.owning_player_id == pokemon.owning_player_id:
            return count
        if not is_pokemon_ex(attacker.archetype_id) or pokemon.entity_id not in ctx.attack_damage:
            return count
        applied = ctx.__dict__.setdefault("_shadowy_concealment", set())
        if pokemon.entity_id in applied:
            return count
        applied.add(pokemon.entity_id)
        return max(0, count - 1)


async def _move_energy(ctx):
    """Printed damage, then move an Energy from this Pokemon to a Benched one."""
    await ctx.deal_damage()
    bench = ctx.my_bench()
    energies = ctx.attached_energies(ctx.attacker)
    if not bench or not energies:
        return
    picks = await ctx.choose_cards(energies, 1, prompt="Choose an Energy to move to 1 of your Benched Pokémon")
    if not picks:
        return
    target = await ctx.choose_pokemon(bench, "Choose a Benched Pokémon")
    if target is not None:
        await ctx.move_energy(picks[0], target)

card = PokemonCardDef(
    guid="f03693ee-632f-51de-8bd1-4118e4541d14",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MegaGengarex.Name",
    display_name="Mega Gengar ex",
    searchable_by=["Mega Gengar ex", "Stage 2", "ex", "SV_Mega", "MegaGengarex"],
    subtypes=["Stage 2", "ex", "SV_Mega"],
    collector_number=125,
    set_code="ME2PT5",
    regulation_mark="I",
    rarity=Rarities.RareHoloEX,
    hp=350,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Haunter.Name",
    family_id=92,
    abilities=[
        Ability(
            title="Shadowy Concealment",
            game_text="If 1 of your [D] Pok\u00e9mon is Knocked Out by damage from an attack from your opponent's Pok\u00e9mon ex, that player takes 1 fewer Prize card. The effect of Shadowy Concealment doesn't stack.",
            passive=ShadowyConcealmentPassive(),
        ),
        Attack(
            title="Void Gale",
            game_text="Move an Energy from this Pok\u00e9mon to 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.DARKNESS: 2},
            damage=230,
            effect=_move_energy,
        ),
    ],
)
