import { createProducerAndSend } from "../kafkaConfig.js"
import { pokedex } from "../data/pokedex.js"

const POKEMON_TOPIC_NAME = "pokemon-export"

async function producePokemon() {
    const messages = []

    for (const [key, pokemon] of Object.entries(pokedex)) {
        if (pokemon.num <= 0) {
            continue
        }

        messages.push({
            key,
            value: JSON.stringify(
                createJsonMessage(pokemon)
            )
        })
    }

    await createProducerAndSend(POKEMON_TOPIC_NAME, messages)
}

function createJsonMessage(pokemon) {
    return {
        pokedexId: pokemon.num,
        name: pokemon.name,
        types: pokemon.types,
        hp: pokemon.baseStats.hp,
        attack: pokemon.baseStats.atk,
        defense: pokemon.baseStats.def,
        specialAttack: pokemon.baseStats.spa,
        specialDefense: pokemon.baseStats.spd,
        speed: pokemon.baseStats.spe,
        abilities: Object.values(pokemon.abilities),
        weight: pokemon.weightkg
    }
}

await producePokemon()
