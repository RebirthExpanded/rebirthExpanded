"""Core Memory (ME - Perfect Order 70 -- JP M3 072).

Pokemon Tool.

  "The Mega Zygarde ex this card is attached to can use the attack on this
   card. (You still need the necessary Energy to use this attack.)"
  Geobuster [FFFF] 350  Discard all Energy from this Pokemon.

The Technical Machine shape -- a granted Attack -- whose condition keeps it
to a Mega Zygarde ex holder.
"""

from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import self_energy_discard_attack
from spirit.game.data_utils import Attack, PokemonToolCardDef, def_for


def _held_by_mega_zygarde(board, player_id, pokemon=None) -> bool:
    return pokemon is not None and \
        getattr(def_for(pokemon.archetype_id), "display_name", None) == "Mega Zygarde ex"


card = PokemonToolCardDef(
    guid="62d9e74b-dcd9-5698-b4b0-bbf2bfccae45",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CoreMemory.Name",
    display_name="Core Memory",
    searchable_by=["Core Memory", "Pokémon Tool", "Tool", "CoreMemory"],
    subtypes=["Pokémon Tool", "Tool"],
    collector_number=70,
    set_code="ME3",
    regulation_mark="J",
    rarity=Rarities.Uncommon,
    granted_abilities=[
        Attack(
            title="Geobuster",
            game_text="Discard all Energy from this Pokémon.",
            cost={PokemonTypes.FIGHTING: 4},
            damage=350,
            condition=_held_by_mega_zygarde,
            effect=self_energy_discard_attack(all_energy=True),
        ),
    ],
)
