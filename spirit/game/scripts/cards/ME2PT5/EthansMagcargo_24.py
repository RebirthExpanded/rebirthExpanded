"""Ethan's Magcargo (ME2PT5 24 -- JP SV9a 019; English ASC/222, ASC/24, DRI/36). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.session.passives import Passive, carrier_pokemon
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card

from spirit.game.models.board import EnergyEntity


class MeltAwayPassive(Passive):
    """No Energy attached: no Retreat Cost (an Ability)."""

    def modify_retreat_cost(self, cost, pokemon, carrier, board):
        if pokemon is carrier and not any(isinstance(c, EnergyEntity) for c in pokemon.children):
            return 0
        return cost


async def lava_burst(ctx):
    pool = [e for e in ctx.attached_energies(ctx.attacker) if is_energy_of_type(e, PokemonTypes.FIRE)]
    if not pool:
        return
    picks = await ctx.choose_cards(pool, min(5, len(pool)), minimum=0, prompt="Discard up to 5 Fire Energy from this Pokémon")
    if picks:
        await ctx.discard_cards(picks)
        await ctx.deal_damage(70 * len(picks))


card = PokemonCardDef(
    guid="ccab9442-cc49-5469-91dd-c8b45294b345",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.EthansMagcargo.Name",
    display_name="Ethan's Magcargo",
    searchable_by=["Ethan's Magcargo", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=24,
    set_code="ME2PT5",
    regulation_mark="I",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.EthansSlugma.Name",
    family_id=218,
    abilities=[
        Ability(
            title="Melt Away",
            game_text="If this Pokémon has no Energy attached, it has no Retreat Cost.",
            passive=MeltAwayPassive(),
        ),
        Attack(
            title="Lava Burst",
            game_text="Discard up to 5 Fire Energy from this Pokémon. This attack does 70 damage for each card you discarded in this way.",
            cost={PokemonTypes.FIRE: 3},
            damage=70,
            damage_operator="x",
            effect=lava_burst,
        ),
    ],
)
