"""Bond Sash (M7 74 -- JP M7 074/078 きずなのタスキ). Japanese art.

Provisional English name and text (no English release yet).
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import Ability, Activations, PokemonToolCardDef, Triggers
from spirit.game.card_effects import m7


card = PokemonToolCardDef(
    guid="90cd201d-a12f-5f21-9de5-0c5338edc352",
    key="M7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BondSash.Name",
    display_name='Bond Sash',
    searchable_by=['Bond Sash', 'Item', 'Pokémon Tool', 'BondSash'],
    subtypes=['Item', 'Pokémon Tool'],
    collector_number=74,
    set_code="M7",
    regulation_mark="J",
    rarity=Rarities.Uncommon,
    granted_abilities=[
        Ability(
            title="Bond Sash",
            game_text="If the Mega Evolution Pokémon ex this card is attached to is Knocked Out by damage from an attack from your opponent's Pokémon, search your deck for a card and put it into your hand. Then, shuffle your deck.",
            trigger=Triggers.ON_KNOCKED_OUT_IN_PLAY,
            effect=m7.bond_sash,
            trigger_applies=lambda c: bool(c.ko_from_attack and m7.is_mega_ex(c.source)),
        ),
    ],
)
