"""Seadra (SV035 117 -- JP SV2a 117; English MEW/117). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

async def blinding_ink(ctx):
    await ctx.deal_damage()
    d = ctx.defender
    if d is not None and not ctx.effects_blocked(d):
        ctx.require_attack_flip(d, coins=2)


card = PokemonCardDef(
    guid="34de24d4-6e69-56ba-bc78-00bbadc28547",
    key="SV035",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Seadra.Name",
    display_name="Seadra",
    searchable_by=["Seadra", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=117,
    set_code="SV035",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Horsea.Name",
    family_id=116,
    abilities=[
        Attack(
            title="Blinding Ink",
            game_text="During your opponent's next turn, if the Defending Pokémon tries to use an attack, your opponent flips 2 coins. If either of them is tails, that attack doesn't happen.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=blinding_ink,
        ),
    ],
)
