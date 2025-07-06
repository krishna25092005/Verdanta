# Streamlit Cloud Deployment Guide

## Quick Deployment Steps

### 1. Streamlit Cloud Setup
1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Connect your GitHub account
3. Select repository: `krishna25092005/Verdanta`
4. Main file path: `app.py`
5. Python version: 3.11

### 2. Environment Variables (Optional)
If you want AI features, add these secrets in Streamlit Cloud:
```
GROQ_API_KEY = "your_groq_api_key_here"
```

### 3. App Access
- **Basic Mode**: App runs without AI features, provides manual carbon accounting
- **Full Mode**: With GROQ_API_KEY, enables all AI insights and assistance

### 4. Known Issues & Solutions

#### SQLite Compatibility
- Fixed: Uses pysqlite3-binary for Streamlit Cloud compatibility
- The app handles SQLite version issues automatically

#### Missing Dependencies
- The app gracefully handles missing AI dependencies
- Falls back to manual guidance when AI features are unavailable

### 5. Testing
The app should start immediately and show:
- ✅ Dashboard with carbon tracking
- ✅ Data Entry forms
- ✅ Settings page
- ✅ AI Insights (with fallback if AI unavailable)

### 6. Troubleshooting
If issues persist:
1. Check Python version is 3.11
2. Verify requirements.txt is being used
3. Check logs for specific error messages

The app is designed to be resilient and will work even if some features are unavailable.
