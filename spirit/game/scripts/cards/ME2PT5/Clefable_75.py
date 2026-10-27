"""Clefable (ME2PT5 75 -- JP SV6 046; English ASC/75, TWM/79). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES

from spirit.game.data_utils import def_for as _def_for


async def foul_play(ctx):
    defender = ctx.opponent_active()
    if defender is None:
        return
    candidates = [(defender, a) for a in getattr(_def_for(defender.archetype_id), "abilities", []) if isinstance(a, Attack)]
    if not candidates:
        return
    picked = await ctx.choose_attack_to_copy(candidates, "Choose an attack to copy")
    if picked is not None:
        await ctx.use_attack(picked[1])


card = PokemonCardDef(
    guid="2fe47d99-d15a-547a-9c11-51847a1fafe6",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Clefable.Name",
    display_name="Clefable",
    searchable_by=["Clefable", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=75,
    set_code="ME2PT5",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Clefairy.Name",
    family_id=173,
    abilities=[
        Attack(
            title="Metronome",
            game_text="Choose 1 of your opponent's Active Pokémon's attacks and use it as this attack.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=foul_play,
        ),
        Attack(
            title="Magical Shot",
            game_text="",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
        ),
    ],
)
