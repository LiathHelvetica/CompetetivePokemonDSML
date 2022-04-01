import { Kafka } from "kafkajs"

export const kafka = new Kafka({
    brokers: ['localhost:20300']
})
