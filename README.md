# FlowGen AI (Colombia) 🎵🎤

**Generador de Rap & Musica Profesional con Integracion Suno AI**

FlowGen AI es una aplicacion web para crear letras de rap profesionales y generar musica tipo Suno/Tunee. Interfaz 100% en espanol colombiano, karaoke sincronizado, vocal remover, y compartir en redes sociales.

## 🎯 Caracteristicas Principales

- **Generacion de Letras AI** - Genera letras profesionales usando Google Gemini
- **Musica Real Profesional** - Integracion con Suno AI para musica tipo Suno/Tunee
- **Modo Karaoke** - Letras sincronizadas con colores (pasadas/actual/futuras)
- **Vocal Remover** - Toggle para quitar voz y cantar sobre instrumental
- **YouTube Inspiration** - Pega link de artista favorito para inspirar letras
- **BPM Selector** - Elige tempo 60-160 BPM
- **10+ Estilos Rap** - Trap, Boom Bap, Cloud Rap, Mumble Rap, Old School, Conscious, etc
- **Biblioteca & Historial** - Guarda todas tus canciones con metadatos
- **Compartir Redes** - Botones directos Instagram, TikTok, Facebook, WhatsApp
- **Exportar Karaoke** - Descarga instrumental.wav + lyrics.json
- **100% Espanol** - Interfaz completa en espanol colombiano

## 🚀 Instalacion & Deploy

### Requisitos
- Node.js 16+
- npm o yarn
- API Key de Suno AI (gratuita en https://suno.ai)
- API Key de Google Gemini (gratuita en https://makersuite.google.com)

### Pasos Instalacion

```bash
# 1. Clonar repositorio
git clone https://github.com/zenufanaexp-sudo/FlowGen-AI-Suno.git
cd FlowGen-AI-Suno

# 2. Instalar dependencias
npm install

# 3. Crear archivo .env
cp .env.example .env

# 4. Agregar tus API Keys en .env
SUNO_API_KEY=tu_clave_suno
GEMINI_API_KEY=tu_clave_gemini
NEXT_PUBLIC_SUNO_WEBHOOK=tu_webhook_url

# 5. Iniciar desarrollo
npm run dev

# 6. Deploy en Vercel
vercel deploy
```

## 📋 Estructura del Proyecto

```
FlowGen-AI-Suno/
├── frontend/              # React + TypeScript
│   ├── components/
│   │   ├── ControlPanel.tsx      # Formulario inputs
│   │   ├── LyricsPanel.tsx       # Editor letras + karaoke
│   │   ├── Visualizer.tsx        # Visualizador audio
│   │   └── SocialShare.tsx       # Botones compartir
│   ├── services/
│   │   ├── geminiService.ts      # Generacion letras
│   │   ├── sunoService.ts        # Integracion Suno API
│   │   └── audioService.ts       # Procesamiento audio
│   ├── styles/                   # CSS/Tailwind
│   └── pages/                    # Next.js pages
├── backend/               # Node.js/Express
│   ├── api/
│   │   ├── generateLyrics.js     # Endpoint letras
│   │   ├── generateMusic.js      # Endpoint musica Suno
│   │   └── vocalRemover.js       # Vocal remover API
│   ├── middleware/
│   └── webhooks/                 # Suno webhooks
├── .env.example           # Variables ambiente
├── package.json
├── tsconfig.json
└── README.md
```

## 💻 Stack Tecnologico

- **Frontend**: React 18, Next.js, TypeScript, Tailwind CSS
- **Backend**: Node.js, Express, Python (audio processing)
- **APIs**: Suno AI, Google Gemini, ElevenLabs TTS
- **Audio**: Web Audio API, tone.js, librosa
- **Database**: MongoDB (para guardar canciones)
- **Deploy**: Vercel (frontend), Heroku (backend)

## 🎨 Como Usar

1. **Ingresa Titulo** de tu cancion
2. **Escribe el Tema** (ej: Paragliding, Viajes, Crypto)
3. **Selecciona Mood & Estilo** (Energetico/Trap, Chill/Cloud Rap, etc)
4. **Pega URL YouTube** de tu artista favorito (opcional)
5. **Click "Generar Letras"** - Genera letras profesionales
6. **Click "Crear Musica"** - Integra con Suno para generar track
7. **Escucha en Karaoke** - Letras sincronizadas con colores
8. **Comparte en Redes** - Instagram, TikTok, Facebook, WhatsApp
9. **Guarda en Biblioteca** - Acceso ilimitado a tus canciones

## 🔌 Integraciones API

### Suno AI Integration
Conecta tu API de Suno para generar musica PROFESIONAL tipo Suno:

```javascript
const song = await generateMusicSuno({
  prompt: "Rap about paragliding in Colombian mountains",
  style: "Trap",
  bpm: 120,
  lyrics: generatedLyrics
});
```

### Google Gemini
Genera letras creativas con analisis de artista:

```javascript
const lyrics = await generateLyricsGemini({
  topic: "Paragliding",
  mood: "Energetic",
  style: "Trap",
  inspirationArtist: "J Balvin",
  language: "es" // Espanol
});
```

## 📱 Variables de Ambiente (.env)

```
NEXT_PUBLIC_APP_NAME=FlowGen AI
NEXT_PUBLIC_API_URL=http://localhost:3001

# Suno AI
SUNO_API_KEY=tu_clave_aqui
SUNO_API_URL=https://api.suno.ai
SUNO_WEBHOOK_SECRET=tu_secret

# Google Gemini
GEMINI_API_KEY=tu_clave_aqui
GEMINI_MODEL=gemini-2.0-flash

# ElevenLabs (opcional)
ELEVENLABS_API_KEY=tu_clave
ELEVENLABS_VOICE_ID=default

# MongoDB
MONGODB_URI=mongodb+srv://user:pass@cluster.mongodb.net/flowgen

# JWT
JWT_SECRET=tu_secret_largo_aqui

# Ambiente
NODE_ENV=production
```

## 🎯 Roadmap Futuro

- [ ] Integracion directa Suno AI webhook
- [ ] Colaboracion en tiempo real
- [ ] Chat IA para mejorar letras
- [ ] Video lyric generation (estilo YouTube)
- [ ] Analytics de views/streams
- [ ] Sistema de monetizacion (afiliado Hotmart)
- [ ] Mobile app iOS/Android
- [ ] Integracion Spotify/Apple Music
- [ ] Comunidad de usuarios
- [ ] Descargas HD MP3/WAV

## 🤝 Contribuir

Las contribuciones son bienvenidas. Por favor:

1. Fork el proyecto
2. Crea rama feature (`git checkout -b feature/AmazingFeature`)
3. Commit cambios (`git commit -m 'Add AmazingFeature'`)
4. Push a rama (`git push origin feature/AmazingFeature`)
5. Abre Pull Request

## 📝 Licencia

MIT License - Ver `LICENSE` para detalles.

## 📧 Contacto

**Creador**: Zenufana Expeditions  
**Email**: info@zenufana.com  
**Website**: https://zenufana.com  
**GitHub**: https://github.com/zenufanaexp-sudo  

## ⭐ Apoya el Proyecto

Si te gusta FlowGen AI, dale una ⭐ en GitHub.

---

**Hecho con ❤️ para la comunidad colombiana de creadores de contenido**

🎵 Genera musica. 🎤 Canta. 📱 Comparte. 🌟 ¡Exito!
