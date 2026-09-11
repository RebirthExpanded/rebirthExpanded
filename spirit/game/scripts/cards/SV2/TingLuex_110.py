"""Ting-Lu ex (SV - Paldea Evolved 110/193 -- JP SV2D 049/071, the art here).

Basic Fighting Pokemon ex. HP 240, weakness Grass x2, no resistance,
retreat 4.

  Ability  Cursed Land  As long as this Pokemon is in the Active Spot,
                        Abilities of your opponent's Pokemon that have any
                        damage counters on them (except Pokemon ex) have
                        no effect.
  Land Scoop [FFF] 150  Put 2 damage counters on 1 of your opponent's
                        Benched Pokemon.

Cursed Land is an Ability lock (blocks_abilities) keyed on the target
carrying damage: Stealthy Hood on the target shields it, and the lock
itself goes quiet when Ting-Lu's own Abilities are off (Path to the Peak
-- it is a Rule Box Pokemon -- or a Garbotoxin on the other side).
"""

from spirit.game.attributes import AttrID, PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.passives_common import is_in_active_spot
from spirit.game.data_utils import Ability, Attack, PokemonCardDef, is_pokemon_ex
from spirit.game.session.passives import Passive


class CursedLandPassive(Passive):
    def blocks_abilities(self, pokemon, carrier):
        if not is_in_active_spot(carrier):
            return False
        if pokemon.owning_player_id == carrier.owning_player_id:
            return False
        if is_pokemon_ex(pokemon.archetype_id):
            return False
        # Printed max HP, read off the entity: effective_max_hp walks the
        # passives, and this hook is called while they are being collected.
        printed = pokemon.attribute_originals.get(
            AttrID.HP.value, pokemon.get_attribute(AttrID.HP, 0))
        return printed - pokemon.get_attribute(AttrID.HP, 0) >= 10


async def land_scoop(ctx):
    """150, then 2 damage counters on 1 of the opponent's Benched Pokemon."""
    await ctx.deal_damage()
    bench = ctx.opponent_bench()
    if not bench:
        return
    target = await ctx.choose_pokemon(bench, "Choose 1 of your opponent's Benched Pokémon")
    if target is None:
        return
    await ctx.deal_damage(20, target=target, apply_modifiers=False, as_counters=True)


card = PokemonCardDef(
    guid="4f02aa21-0dee-5316-b3af-838378cdd06e",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TingLuex.Name",
    display_name="Ting-Lu ex",
    searchable_by=["Ting-Lu ex", "Basic", "ex", "TingLuex"],
    subtypes=["Basic", "ex"],
    collector_number=110,
    set_code="SV2",
    regulation_mark="G",
    rarity=Rarities.RareHoloEX,
    hp=240,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    family_id=1003,
    abilities=[
        Ability(title="Cursed Land",
                game_text="As long as this Pokémon is in the Active Spot, Abilities of your opponent's Pokémon that have any damage counters on them (except Pokémon ex) have no effect.",
                passive=CursedLandPassive()),
        Attack(title="Land Scoop",
               game_text="Put 2 damage counters on 1 of your opponent's Benched Pokémon.",
               cost={PokemonTypes.FIGHTING: 3},
               damage=150, effect=land_scoop),
    ],
)
