# Streamlit Cloud Deployment Fix

## Issue: ChromaDB SQLite Version Error

If you're seeing this error in Streamlit Cloud:
```
RuntimeError: Your system has an unsupported version of sqlite3. Chroma requires sqlite3 >= 3.35.0.
```

## Quick Solution:

### Option 1: Use Basic Requirements (Recommended)
1. **Rename files** in your repository:
   - Rename `requirements.txt` to `requirements-ai.txt` 
   - Rename `requirements-basic.txt` to `requirements.txt`
2. **Redeploy** - The app will work without AI features but with all core functionality

### Option 2: Full AI Features (Advanced)
If you need AI features, the fixes are already in place:

✅ **Fixed in this repository:**
1. **Updated `ai_agents.py`** - Added SQLite compatibility fix
2. **Updated `requirements.txt`** - Added `pysqlite3-binary` package
3. **Added `packages.txt`** - Includes `libsqlite3-dev` system dependency  
4. **Enhanced error handling** - App won't crash if AI features fail

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
7. **Deploy** - The app should now work!

## Get Your Groq API Key:
1. Visit [console.groq.com](https://console.groq.com/)
2. Sign up/Login
3. Generate a new API key
4. Add it to your Streamlit Cloud secrets

Your app will be available at: `https://your-app-name.streamlit.app`

## App Features Available:
- ✅ **Dashboard**: Real-time emissions visualization
- ✅ **Data Entry**: Manual and CSV data input
- ✅ **Settings**: Company configuration
- 🤖 **AI Insights**: Available with full requirements, manual guidance otherwise
