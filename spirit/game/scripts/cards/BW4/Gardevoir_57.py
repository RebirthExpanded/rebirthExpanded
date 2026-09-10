"""Gardevoir (BW - Next Destinies 57/99 -- JP BW3 028/052).

Stage 2 Psychic. HP 110, weakness Psychic x2, retreat 2. Evolves from
Kirlia.

  Ability  Psychic Mirage  Each basic Psychic Energy attached to your
                           Psychic Pokemon provides [P][P] Energy. You can't
                           apply more than 1 Psychic Mirage Ability at a
                           time.

  Mind Shock  [PPCC] 60  This attack's damage isn't affected by Weakness or
                         Resistance.

Meganium's Wild Growth in Psychic, and it borrows that card's two answers.
The hook is handed the Energy and its holder but not the carrier, so
"YOUR Psychic Pokemon" is settled by scanning the board for a Psychic
Mirage whose carrier shares the holder's owner. And "can't apply more than
1 at a time" falls out of refusing to touch an option that is already
doubled, so a second Gardevoir changes nothing.

Three conditions, all re-read on every cost check: a BASIC Psychic Energy,
on a Psychic Pokemon, on this Gardevoir's side. A basic Psychic Energy on a
Colorless Pokemon is untouched, and so is a Rainbow or a Double Colorless
anywhere.
"""

from spirit.game.attributes import AttrID, PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import ignore_effects_attack
from spirit.game.card_effects.pokemon import energy_provides_type
from spirit.game.data_utils import Ability, Attack, PokemonCardDef
from spirit.game.session.effects import is_pokemon_of_type
from spirit.game.session.passives import Passive, active_passives


class PsychicMiragePassive(Passive):
    """Basic [P] on your Psychic Pokemon counts double -- once, however many
    Gardevoir are in play."""

    def modify_energy_provided(self, options, energy, holder, board):
        if holder is None or energy.get_attribute(AttrID.IS_SPECIAL_ENERGY):
            return options
        if not energy_provides_type(energy, PokemonTypes.PSYCHIC.value):
            return options
        if not is_pokemon_of_type(holder, PokemonTypes.PSYCHIC):
            return options
        if any(len(option) >= 2 for option in options):
            return options   # already doubled: one Psychic Mirage at a time
        mine = any(
            isinstance(p, PsychicMiragePassive)
            and c.owning_player_id == holder.owning_player_id
            for p, c in active_passives(board)
        )
        if not mine:
            return options
        return [list(option) * 2 for option in options]


card = PokemonCardDef(
    guid="91eea7a2-c771-5ffd-af1d-cf6412e6ac85",
    key="BW4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gardevoir.Name",
    display_name="Gardevoir",
    searchable_by=["Gardevoir", "Stage 2", "Gardevoir"],
    subtypes=["Stage 2"],
    collector_number=57,
    set_code="BW4",
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Kirlia.Name",
    family_id=280,
    abilities=[
        Ability(
            title="Psychic Mirage",
            game_text="Each basic Psychic Energy attached to your Psychic Pokémon provides Psychic Psychic Energy. You can't apply more than 1 Psychic Mirage Ability at a time.",
            passive=PsychicMiragePassive(),
        ),
        Attack(
            title="Mind Shock",
            game_text="This attack's damage isn't affected by Weakness or Resistance.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=ignore_effects_attack(ignore_weakness=True,
                                         ignore_resistance=True),
        ),
    ],
)
