from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.data_utils import def_for
from spirit.game.card_effects.attacks_common import condition_attack


async def horrifying_revenge(ctx):
    """30, +100 if one of your Hop's Pokemon was KO'd by attack damage last turn."""
    bonus = 0
    for ko in ctx.session.turn_state.kos_by_attack_last_turn.get(ctx.player_id, []):
        name = getattr(def_for(ko.get("archetype_id") or ""), "display_name", "") or ""
        if name.startswith("Hop's "):
            bonus = 100
            break
    await ctx.deal_damage(30 + bonus)

card = PokemonCardDef(
    guid="b7bb026a-c143-567f-8452-547867c73cd0",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HopsTrevenant.Name",
    display_name="Hop's Trevenant",
    searchable_by=["Hop's Trevenant", "Stage 1", "HopsTrevenant"],
    subtypes=["Stage 1"],
    collector_number=96,
    set_code="ME2PT5",
    regulation_mark="I",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.HopsPhantump.Name",
    family_id=708,
    abilities=[
        Attack(
            title="Horrifying Revenge",
            game_text="If any of your Hop's Pok\u00e9mon were Knocked Out by damage from an attack during your opponent's last turn, this attack does 100 more damage.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="+",
            effect=horrifying_revenge,
        ),
        Attack(
            title="Corner",
            game_text="During your opponent's next turn, the Defending Pok\u00e9mon can't retreat.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
            effect=condition_attack(no_retreat=True),
        ),
    ],
)
