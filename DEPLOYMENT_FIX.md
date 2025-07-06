# Streamlit Cloud Deployment Fix

## Issue: ChromaDB SQLite Version Error

If you're seeing this error in Streamlit Cloud:
```
RuntimeError: Your system has an unsupported version of sqlite3. Chroma requires sqlite3 >= 3.35.0.
```

## Solution Applied:

✅ **Fixed in this repository:**

1. **Updated `requirements.txt`** - Added `pysqlite3-binary` package
2. **Added `packages.txt`** - Includes `libsqlite3-dev` system dependency  
3. **Updated `app.py`** - Added SQLite compatibility fix at startup
4. **Added deployment examples** - `.env.example` and `secrets.toml.example`

## Deploy to Streamlit Cloud:

1. **Fork this repository** to your GitHub account
2. **Go to [share.streamlit.io](https://share.streamlit.io)**
3. **Connect your GitHub account**
4. **Select your forked repository**
5. **Set main file path**: `app.py`
6. **Add secrets in app settings**:
   ```toml
   GROQ_API_KEY = "your_actual_groq_api_key_here"
   ```
7. **Deploy** - The app should now work without SQLite errors!

## Get Your Groq API Key:
1. Visit [console.groq.com](https://console.groq.com/)
2. Sign up/Login
3. Generate a new API key
4. Add it to your Streamlit Cloud secrets

Your app will be available at: `https://your-app-name.streamlit.app`
