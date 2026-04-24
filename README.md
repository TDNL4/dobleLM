# Proyecto 8: LLM
Escribe aquí una breve descripción de tu proyecto

## Requisitos previos

- Python 3.8 o superior.
- Una cuenta en OpenAI y una API Key válida.

## Instalación y Configuración

1. **Clonar el repositorio y acceder a la carpeta del proyecto:**
   \`\`\`bash
   git clone <URL_DE_TU_FORK>
   cd llm
   \`\`\`

2. **Crear y activar un entorno virtual:**
   * En Windows:
     \`\`\`bash
     python -m venv venv
     venv\Scripts\activate
     \`\`\`
   * En macOS/Linux:
     \`\`\`bash
     python3 -m venv venv
     source venv/bin/activate
     \`\`\`

3. **Instalar las dependencias:**
   \`\`\`bash
   pip install -r requirements.txt
   \`\`\`

4. **Configurar las variables de entorno:**
   Crea un archivo llamado `.env` en la raíz del proyecto y agrega tu API Key de OpenAI de la siguiente manera:
   \`\`\`env
   OPENAI_API_KEY=tu_clave_api_aqui
   \`\`\`
