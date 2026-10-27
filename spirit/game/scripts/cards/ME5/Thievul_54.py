"""Thievul (ME5 54 -- JP M5 052; English PBL/54, PBL/92). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES

from spirit.game.data_utils import def_for


async def skill_thief(ctx):
    if ctx.hand():
        return
    candidates = [(p, a) for p in ctx.opponent_pokemon_in_play()
                  for a in getattr(def_for(p.archetype_id), "abilities", []) or []
                  if isinstance(a, Attack)]
    if not candidates:
        return
    picked = await ctx.choose_attack_to_copy(candidates, "Choose an attack to use")
    if picked is None:
        return
    _, chosen = picked
    await ctx.use_attack(chosen)


card = PokemonCardDef(
    guid="626d4b6a-a365-564c-a08d-e28d3f4be201",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Thievul.Name",
    display_name="Thievul",
    searchable_by=["Thievul", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=54,
    set_code="ME5",
    regulation_mark="J",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Nickit.Name",
    family_id=827,
    abilities=[
        Attack(
            title="Skill Thief",
            game_text="If you have no cards in your hand, choose an attack from 1 of your opponent's Pokémon in play and use it as this attack.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=skill_thief,
        ),
        Attack(
            title="Sharp Fang",
            game_text="",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
        ),
    ],
)
