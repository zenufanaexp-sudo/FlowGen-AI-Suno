#!/usr/bin/env python3
"""FlowGen AI - Generador de Rap & Musica para Colombia"""
import os
import json
import requests
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

# Configurar APIs
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
SUNO_API_KEY = os.getenv('SUNO_API_KEY')
SUNO_API_URL = os.getenv('SUNO_API_URL', 'https://api.suno.ai')

genai.configure(api_key=GEMINI_API_KEY)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/generate-lyrics', methods=['POST'])
def generate_lyrics():
    """Genera letras de rap usando Google Gemini"""
    try:
        data = request.json
        tema = data.get('tema', '')
        estilo = data.get('estilo', 'Trap')
        bpm = data.get('bpm', 100)
        
        model = genai.GenerativeModel('gemini-pro')
        prompt = f"""Genera una letra de rap en español colombiano sobre: {tema}
        Estilo: {estilo}
        BPM: {bpm}
        La letra debe ser:
        - Autentica y con argot colombiano
        - Rimáda y con flow
        - Entre 16 y 24 líneas
        - Con ritmo acorde al BPM indicado
        
        Formato: Solo la letra, sin introducción
        """
        
        response = model.generate_content(prompt)
        lyrics = response.text
        
        return jsonify({
            'success': True,
            'lyrics': lyrics,
            'tema': tema,
            'estilo': estilo,
            'bpm': bpm
        })
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 400

@app.route('/api/generate-music', methods=['POST'])
def generate_music():
    """Genera música usando Suno API"""
    try:
        data = request.json
        lyrics = data.get('lyrics', '')
        estilo = data.get('estilo', 'Trap')
        bpm = data.get('bpm', 100)
        titulo = data.get('titulo', 'Mi Cancion')
        
        headers = {
            'Authorization': f'Bearer {SUNO_API_KEY}',
            'Content-Type': 'application/json'
        }
        
        payload = {
            'lyrics': lyrics,
            'style': estilo.lower(),
            'title': titulo,
            'bpm': bpm,
            'language': 'es'
        }
        
        response = requests.post(
            f'{SUNO_API_URL}/generate',
            json=payload,
            headers=headers,
            timeout=30
        )
        
        if response.status_code == 200:
            result = response.json()
            return jsonify({
                'success': True,
                'trackId': result.get('id'),
                'audioUrl': result.get('audio_url'),
                'status': 'generating'
            })
        else:
            return jsonify({
                'success': False,
                'error': 'Error en Suno API',
                'details': response.text
            }), 400
            
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 400

@app.route('/api/check-music/<track_id>', methods=['GET'])
def check_music(track_id):
    """Verifica el estado de una canción en generación"""
    try:
        headers = {
            'Authorization': f'Bearer {SUNO_API_KEY}'
        }
        
        response = requests.get(
            f'{SUNO_API_URL}/track/{track_id}',
            headers=headers,
            timeout=10
        )
        
        if response.status_code == 200:
            result = response.json()
            return jsonify({
                'success': True,
                'status': result.get('status'),
                'audioUrl': result.get('audio_url'),
                'completed': result.get('status') == 'completed'
            })
        else:
            return jsonify({'success': False, 'error': 'Track not found'}), 404
            
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 400

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
