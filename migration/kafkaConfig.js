import { Kafka } from "kafkajs"

export const kafka = new Kafka({
    brokers: ['localhost:20300']
})

export async function createProducerAndSend(topic, messages) {
    const producer = kafka.producer()

    await producer.connect()
    await producer.send({
        topic,
        messages
    })

    await producer.disconnect()
}
