# Guía Paso a Paso: Cómo Publicar tu Compendio en Render Gratis

Esta guía te explica cómo subir tu compendio académico a **Render** para que tengas un enlace público en internet (ej: `https://sistemas-bancarios.onrender.com`) y puedas abrirlo y consultarlo desde tu teléfono celular, tablet o cualquier computadora en cualquier momento.

---

## 🚀 Opción 1: Publicar como "Static Site" en Render (Recomendada)

> [!TIP]
> **¿Por qué es la mejor opción?**
> Los sitios estáticos en Render son **100% gratuitos para siempre**, cargan instantáneamente desde una red global (CDN), tienen certificado de seguridad HTTPS automático y **nunca se apagan ni entran en reposo**.

### Paso 1: Subir tus archivos a GitHub
1. Entra a [github.com](https://github.com) e inicia sesión (o créate una cuenta si no tienes).
2. Haz clic en el botón verde **New** para crear un nuevo repositorio.
3. Asígnale un nombre, por ejemplo: `sistemas-bancarios` (puedes dejarlo público o privado) y presiona **Create repository**.
4. Abre una terminal (PowerShell o CMD) en esta carpeta (`c:\Users\Andrea\OneDrive\Escritorio\sistemas bancarios`) y ejecuta:

```powershell
git init
git add .
git commit -m "Compendio académico de sistemas bancarios y teoría monetaria"
git branch -M main
git remote add origin https://github.com/TU_USUARIO_GITHUB/sistemas-bancarios.git
git push -u origin main
```
*(Reemplaza `TU_USUARIO_GITHUB` por tu nombre de usuario en GitHub).*

---

### Paso 2: Conectar Render con tu GitHub
1. Entra a [render.com](https://render.com) y presiona **Get Started for Free** o **Sign In** (puedes iniciar sesión directamente con tu cuenta de GitHub con 1 solo clic).
2. En el panel principal de Render (Dashboard), haz clic en el botón superior **New +** y selecciona **Static Site**.
3. Elige tu repositorio `sistemas-bancarios` y presiona **Connect**.
4. Configura los siguientes campos:
   - **Name**: `sistemas-bancarios` (o el nombre que prefieras).
   - **Branch**: `main`.
   - **Build Command**: Déjalo vacío.
   - **Publish directory**: Escribe `static` (o déjalo en `.` ya que los archivos están en ambas partes).
5. Haz clic abajo en el botón verde **Create Static Site**.

🎉 **¡Listo!** En unos 30 segundos Render compilará tu sitio y te dará una URL pública como:
👉 `https://sistemas-bancarios.onrender.com`

Ya puedes enviarte ese link a WhatsApp o guardarlo en los marcadores de tu celular para estudiar desde cualquier lugar.

---

## 🐍 Opción 2: Publicar como "Web Service" en Python / Flask

Si prefieres tener activo el servidor de Python con el endpoint `/api/data`:

1. En el panel de Render, haz clic en **New +** &rarr; **Web Service**.
2. Conecta tu repositorio de GitHub `sistemas-bancarios`.
3. Configuración:
   - **Name**: `sistemas-bancarios`
   - **Environment**: `Python 3`
   - **Region**: La más cercana (ej: Ohio o Frankfurt)
   - **Branch**: `main`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
   - **Instance Type**: Selecciona **Free** ($0 / mes)
4. Presiona **Create Web Service**.

*(Nota: En el plan gratuito de Web Service, si pasas 15 minutos sin usar la página, el servidor se suspende temporalmente y tarda unos 40 segundos en reactivarse la próxima vez que ingreses. Por eso la Opción 1 de Static Site suele ser más cómoda).*

---

## 💻 Cómo probarlo localmente en tu computadora hoy mismo

No necesitas conexión a internet para ver la página ahora mismo:

### Método A: Servidor Flask local
Abre PowerShell en esta carpeta y corre:
```powershell
python app.py
```
Abre en tu navegador: [http://localhost:5000](http://localhost:5000)

### Método B: Doble clic directo
Simplemente ve a la carpeta y haz **doble clic en `index.html`**. Se abrirá en Chrome o Edge con todas sus funciones activas.
