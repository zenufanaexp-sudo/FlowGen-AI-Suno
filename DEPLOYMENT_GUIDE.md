# Guia de Despliegue - FlowGen AI (Colombia)

## Opcion 1: Despliegue Rapido en Vercel (RECOMENDADO)

### Paso 1: Preparar Repositorio
1. Asegúrate de que tienes una cuenta en GitHub
2. El repositorio ya está listo en: https://github.com/zenufanaexp-sudo/FlowGen-AI-Suno

### Paso 2: Conectar con Vercel
1. Visita https://vercel.com
2. Haz clic en "Sign Up" o inicia sesión
3. Conecta tu cuenta de GitHub
4. Selecciona el repositorio FlowGen-AI-Suno
5. Vercel detectará automaticamente package.json y vercel.json
6. Haz clic en "Deploy"

### Paso 3: Agregar Variables de Entorno
En el panel de Vercel, ve a Settings > Environment Variables y agrega:

```
GOOGLE_API_KEY=tu_api_key_aqui
SUNO_API_KEY=tu_suno_api_key_aqui
SUNO_API_URL=https://api.suno.ai
SUNO_WEBHOOK_SECRET=tu_webhook_secret
ELEVENLABS_API_KEY=tu_elevenlabs_key
ELEVENLABS_VOICE_ID=tu_voice_id
MONGODB_URI=mongodb+srv://usuario:password@cluster.mongodb.net/flowgen
JWT_SECRET=tu_jwt_secret_aleatorio
VERCEL_ENV=production
```

## Opcion 2: Ejecutar Localmente (Para Desarrollo)

### Requisitos Previos
- Node.js 18.0.0 o superior
- npm o yarn
- Git

### Instalacion
1. Clona el repositorio:
```bash
git clone https://github.com/zenufanaexp-sudo/FlowGen-AI-Suno.git
cd FlowGen-AI-Suno
```

2. Copia .env.example a .env:
```bash
cp .env.example .env
```

3. Edita .env con tus claves API reales

4. Instala dependencias:
```bash
npm install
```

5. Inicia el servidor de desarrollo:
```bash
npm run dev
```

6. Abre http://localhost:5173 en tu navegador

## Obtener Claves API

### Google Generative AI (Letras de Rap)
1. Ve a https://aistudio.google.com
2. Haz clic en "Get API Key"
3. Crea una nueva clave y cópiala
4. Agrégala como GOOGLE_API_KEY en .env o Vercel

### Suno AI (Generacion de Musica)
1. Registrate en https://suno.com
2. Ve a Account > API Keys
3. Copia tu API Key y URL
4. Agrégalas como SUNO_API_KEY y SUNO_API_URL

### ElevenLabs (Voces de Calidad)
1. Ve a https://elevenlabs.io
2. Crea una cuenta
3. En Voices, selecciona tu voz preferida y obtén su ID
4. En Account, copia tu API Key

### MongoDB (Guardar Canciones)
1. Ve a https://www.mongodb.com/cloud/atlas
2. Crea un cluster gratuito
3. Obtén la cadena de conexión (MongoDB URI)
4. Reemplaza usuario y password con tus credenciales

## Estructura del Proyecto

```
FlowGen-AI-Suno/
├── .env.example              # Variables de ejemplo
├── .gitignore               # Archivos ignorados por git
├── package.json             # Dependencias y scripts
├── vercel.json              # Config para Vercel
├── README.md                # Documentacion principal
├── DEPLOYMENT_GUIDE.md      # Esta guia
├── src/
│   ├── App.jsx             # Componente principal
│   ├── index.css           # Estilos globales
│   └── components/         # Componentes React
├── api/
│   └── index.js            # Servidor backend (Express)
└── public/                  # Archivos estaticos
```

## Troubleshooting

### Error: "Cannot find module"
Solucion: Ejecuta `npm install` nuevamente

### Error: "API Key invalid"
Solucion: Verifica que copiaste correctamente la API Key en .env o Vercel

### La app no genera musica
Solucion: Asegúrate de que Suno API key está activa y tienes creditos disponibles

### Puerto 5173 ya en uso
Solucion: Ejecuta `npm run dev -- --port 3000`

## Soporte para Colombianos

- La interfaz está 100% en español colombiano
- Soporta los estilos de rap de moda: reggaeton, trap latino, boom bap
- Función karaoke para cantar sobre las pistas generadas
- Removedor de voz para practicar (modo instrumental)
- Exporta en formato MP3 de alta calidad

## Proximo Pasos

1. Personaliza el logo en src/components/
2. Agrega mas estilos de rap en la configuracion
3. Integra con redes sociales para compartir
4. Agrega base de datos para guardar canciones favoritas
5. Implementa sistema de usuarios con autenticacion

## Licencia

MIT - Libre para uso personal y comercial
