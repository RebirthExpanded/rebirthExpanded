"""Toxtricity ex (SV4 100 -- JP SV4M 040; English PAR/100, PAR/227). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers
from spirit.game.card_effects.pokemon import TeraRulePassive

from spirit.game.card_effects import attacks_common as ac
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card


async def gaia_punk(ctx):
    pool = [e for p in ctx.my_pokemon_in_play() for e in ctx.attached_energies(p) if is_energy_of_type(e, PokemonTypes.LIGHTNING)]
    if len(pool) < 3:
        return
    picks = await ctx.choose_cards(pool, 3, minimum=3, prompt="Choose 3 Lightning Energy to discard from your Pokémon")
    await ctx.discard_cards(picks)
    await ctx.deal_damage()


card = PokemonCardDef(
    guid="4f4e8835-ad9a-5a43-bd98-fb1cfd2aad8a",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Toxtricityex.Name",
    display_name="Toxtricity ex",
    searchable_by=["Toxtricity ex", "Stage 1", "ex", "Tera"],
    subtypes=["Stage 1", "ex", "Tera"],
    collector_number=100,
    set_code="SV4",
    regulation_mark="G",
    rarity=Rarities.RareHoloEX,
    hp=260,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Toxel.Name",
    family_id=848,
    passive=TeraRulePassive(),
    abilities=[
        Attack(
            title="Knocking Hammer",
            game_text="Discard the top card of your opponent's deck.",
            cost={PokemonTypes.LIGHTNING: 2},
            damage=70,
            effect=ac.mill_attack(1),
        ),
        Attack(
            title="Gaia Punk",
            game_text="Discard 3 Lightning Energy from your Pokémon.",
            cost={PokemonTypes.LIGHTNING: 3},
            damage=270,
            effect=gaia_punk,
        ),
    ],
)
