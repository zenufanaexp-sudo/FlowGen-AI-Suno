# FlowGen AI - Guia Rapida de Inicio (Para ti, parcero)

## OPCION MAS FACIL: Render (Gratis, 5 minutos)

### PASO 1: Obtener claves API

**Google Gemini (para letras):**
- Ve a: https://aistudio.google.com
- Haz clic en "Get API Key"
- Copiar la clave (ejemplo: AIzaSy...)

**Suno AI (para musica):**
- Ve a: https://suno.com
- Registrate/inicia sesion
- Ve a Account > API Keys
- Copiar la clave

### PASO 2: Deploy en Render

1. Ve a https://render.com
2. Haz clic en "Sign up" (usa GitHub)
3. Conecta tu cuenta de GitHub
4. En dashboard, haz clic en "+" y "Web Service"
5. Pega esta URL: `https://github.com/zenufanaexp-sudo/FlowGen-AI-Suno`
6. Configura:
   - Name: `flowgen-ai`
   - Environment: Python 3
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn main:app`
7. Scroll down a "Environment Variables" y agrega:
   ```
   GOOGLE_API_KEY=tu_clave_google_aqui
   SUNO_API_KEY=tu_clave_suno_aqui
   SUNO_API_URL=https://api.suno.ai
   ```
8. Haz clic en "Create Web Service"
9. Espera 3-5 minutos a que termine el deploy
10. URL en vivo aparecera en la parte superior (ej: https://flowgen-ai-xxx.onrender.com)

## OPCION 2: Ejecutar Localmente

```bash
# Clona el proyecto
git clone https://github.com/zenufanaexp-sudo/FlowGen-AI-Suno.git
cd FlowGen-AI-Suno

# Copia variables
cp .env.example .env

# Abre .env en un editor y rellena:
# GOOGLE_API_KEY=tu_clave
# SUNO_API_KEY=tu_clave
# SUNO_API_URL=https://api.suno.ai

# Instala dependencias
pip install -r requirements.txt

# Ejecuta
python main.py

# Abre http://localhost:5000
```

## Que Hacer Cuando Este Corriendo

1. **Generar letras:**
   - Escribe el tema (ej: "Mi vida en la ciudad")
   - Elige estilo (Trap, Reggaeton, Boom Bap)
   - BPM (80-140)
   - Haz clic en "Generar Letra"

2. **Generar musica:**
   - Copia la letra generada
   - Haz clic en "Crear Audio"
   - Espera 30-60 segundos (Suno genera la musica)
   - Descarga el MP3

3. **Karaoke:**
   - Reproduce la cancion
   - Las letras sincronizadas apareceran
   - Toggle para quitar la voz

## Errores Comunes

**"API Key invalid"**
- Revisa que copiaste correctamente la clave
- No hay espacios al inicio o final

**"Service timeout"** (en Render)
- Es normal, toma 30-60s
- Espera sin recargar

**Port already in use**
```bash
python main.py --port 3000
```

## Siguientes Pasos

- Personaliza colores y logos
- Agrega mas estilos de rap
- Integra con Instagram/TikTok
- Crea comunidad de usuarios

## Soporte

Si algo falla:
1. Revisa los logs en Render
2. Verifica que las claves API esten activas
3. Intenta en otro navegador
4. Contacta: zenufanaexp.sudo@gmail.com

**La app esta lista. Solo necesitas agregar tus claves y hacer clic en Deploy.**
