"""Maushold ex (SV4 155 -- JP SV4M 057; English PAR/155, PAR/233). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import passives_common as pc
from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES


async def solidarity(ctx):
    attacker = ctx.damaged_by
    me = ctx.source
    n = sum(1 for p in ctx.board.pokemon_in_play(me.owning_player_id)
            if p.get_attribute(AttrID.EVOLUTION_LOGIC_NAME) in ("Tandemaus", "Maushold"))
    if attacker is not None and n:
        await ctx.deal_damage(30 * n, target=attacker, apply_modifiers=False, as_counters=True, is_attack=False)


async def nom_nom_nom_incisors(ctx):
    await ctx.deal_damage()
    await ctx.draw_cards(2)


card = PokemonCardDef(
    guid="ce159f04-20ed-5f23-8ca6-5c380b04b53c",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mausholdex.Name",
    display_name="Maushold ex",
    searchable_by=["Maushold ex", "Stage 1", "ex"],
    subtypes=["Stage 1", "ex"],
    collector_number=155,
    set_code="SV4",
    regulation_mark="G",
    rarity=Rarities.RareHoloEX,
    hp=230,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Tandemaus.Name",
    family_id=924,
    abilities=[
        Ability(
            title="Solidarity",
            game_text="If this Pokémon is in the Active Spot and is damaged by an attack from your opponent's Pokémon (even if this Pokémon is Knocked Out), put 3 damage counters on the Attacking Pokémon for each of your Tandemaus, Maushold, and Maushold ex in play.",
            trigger=Triggers.ON_DAMAGED_BY_ATTACK,
            trigger_applies=pc.hit_in_active_by_opponent,
            effect=solidarity,
        ),
        Attack(
            title="Nom-Nom-Nom Incisors",
            game_text="Draw 2 cards.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=120,
            effect=nom_nom_nom_incisors,
        ),
    ],
)
