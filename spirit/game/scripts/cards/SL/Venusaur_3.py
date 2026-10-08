"""Venusaur (SM - Shining Legends 3/73 -- JP SM3+ 003/072, the art here).

Stage 2 Grass Pokemon, evolves from Ivysaur. HP 160, weakness Fire x2,
retreat 4.

  Ability: Jungle Totem  Each basic [G] Energy attached to your Pokemon
                         provides [G][G] Energy. You can't apply more than
                         1 Jungle Totem Ability at a time.
  Solar Beam [GGCC] 90

Meganium's Wild Growth gives the same doubling: with both in play a basic
[G] Energy still provides only [G][G] (ruling) -- each passive leaves an
Energy alone once something has already doubled it, so neither stacks on
the other or on a second copy of itself.
"""

from spirit.game.attributes import AttrID, PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.pokemon import energy_provides_type
from spirit.game.data_utils import Ability, Attack, PokemonCardDef
from spirit.game.session.passives import Passive, active_passives


class JungleTotemPassive(Passive):
    def modify_energy_provided(self, options, energy, holder, board):
        if holder is None or energy.get_attribute(AttrID.IS_SPECIAL_ENERGY):
            return options
        if not energy_provides_type(energy, PokemonTypes.GRASS.value):
            return options
        # Already doubled (another Jungle Totem, Wild Growth): no stacking.
        if any(len(option) >= 2 for option in options):
            return options
        if not any(isinstance(p, JungleTotemPassive)
                   and c.owning_player_id == holder.owning_player_id
                   for p, c in active_passives(board)):
            return options
        return [list(option) * 2 for option in options]


card = PokemonCardDef(
    guid="c552e020-ed6f-5539-b6b6-e54af28eedc5",
    key="SL",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Venusaur.Name",
    display_name="Venusaur",
    searchable_by=["Venusaur", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=3,
    set_code="SL",
    rarity=Rarities.Uncommon,
    hp=160,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Ivysaur.Name",
    family_id=1,
    abilities=[
        Ability(
            title="Jungle Totem",
            game_text="Each basic [G] Energy attached to your Pokémon provides [G][G] Energy. You can't apply more than 1 Jungle Totem Ability at a time.",
            passive=JungleTotemPassive(),
        ),
        Attack(
            title="Solar Beam",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 2},
            damage=90,
        ),
    ],
)
