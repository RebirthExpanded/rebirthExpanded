"""Sandy Shocks (SV05 98 -- JP SVHK 011; English TEF/98). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

async def magnetic_burst(ctx):
    n = sum(len(ctx.attached_energies(p)) for p in ctx.my_pokemon_in_play())
    await ctx.deal_damage(20 + (70 if n >= 3 else 0), ignore_weakness=True)


card = PokemonCardDef(
    guid="b86e1f29-9162-5c8a-ad12-78e5648f8f65",
    key="SV05",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.SandyShocks.Name",
    display_name="Sandy Shocks",
    searchable_by=["Sandy Shocks", "Basic", "Ancient"],
    subtypes=["Basic", "Ancient"],
    collector_number=98,
    set_code="SV05",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=989,
    abilities=[
        Attack(
            title="Magnetic Burst",
            game_text="If you have 3 or more Energy in play, this attack does 70 more damage. This attack's damage isn't affected by Weakness.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=20,
            damage_operator="+",
            effect=magnetic_burst,
        ),
        Attack(
            title="Power Gem",
            game_text="",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
        ),
    ],
)
