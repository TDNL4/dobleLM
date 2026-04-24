import os
from openai import OpenAI
from dotenv import load_dotenv

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Inicializar el cliente de OpenAI
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def sistema_atencion_cliente():
    print("==================================================")
    print("Iniciando Sistema de Atención al Cliente...")
    
    # Simulación requerida por los lineamientos del proyecto
    print("[Simulación] Consultando base de datos de clientes...")
    print("[Simulación] Cargando historial de visualización y preferencias del usuario...")
    print("==================================================\n")

    # Prompt del sistema: Define la personalidad y las reglas del LLM
    system_prompt = """
    Eres un asistente de atención al cliente altamente eficiente para una plataforma global de streaming de contenido.
    Tus objetivos principales son:
    1. Resolver problemas técnicos y de facturación de manera clara y amable.
    2. Ayudar a retener a los suscriptores ofreciendo recomendaciones de contenido altamente personalizadas basadas en el contexto de la conversación.
    3. Mantener un tono conversacional, profesional y empático.
    Nunca inventes información sobre políticas de precios; si no estás seguro, sugiere contactar a un humano.
    """

    # Historial de mensajes para mantener el contexto de la conversación
    mensajes = [{"role": "system", "content": system_prompt}]

    print("Asistente: ¡Hola! Bienvenido al soporte técnico de nuestra plataforma. ¿En qué te puedo ayudar hoy? (Escribe 'salir' para terminar)")

    # Bucle principal del chat
    while True:
        user_input = input("\nTú: ")
        
        # Condición de salida
        if user_input.lower() in ['salir', 'exit', 'quit']:
            print("Asistente: Ha sido un placer ayudarte. ¡Que disfrutes tu contenido!")
            break

        # Agregar el mensaje del usuario al historial
        mensajes.append({"role": "user", "content": user_input})

        try:
            # Llamada a la API de OpenAI
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=mensajes,
                temperature=0.7 # Un balance entre respuestas precisas y creativas
            )

            respuesta_bot = response.choices[0].message.content
            print(f"\nAsistente: {respuesta_bot}")

            # Guardar la respuesta del asistente en el historial
            mensajes.append({"role": "assistant", "content": respuesta_bot})

        except Exception as e:
            print(f"\n[Error de comunicación con la API]: {e}")
            print("Por favor, revisa tu conexión o tu API Key en el archivo .env")

if __name__ == "__main__":
    sistema_atencion_cliente()