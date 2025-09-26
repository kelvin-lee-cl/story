# Story AI - Deployment Guide

## ⚠️ IMPORTANT: Cohere API Update
This app uses the NEW Cohere Chat API (not the deprecated Generate API). 
Ensure your deployment uses the latest code from this repository.

## Quick Deploy Options

### 1. 🚀 Heroku (Recommended)
```bash
# Install Heroku CLI first: https://devcenter.heroku.com/articles/heroku-cli

# Login to Heroku
heroku login

# Create new Heroku app
heroku create your-story-ai-app

# Set environment variable
heroku config:set COHERE_API_KEY=CKaP1q2LMynVtB6FJxACsz7Wdg57r8hKKmEwBIEL

# Deploy
git push heroku master

# Open your app
heroku open
```

### 2. ⚡ Vercel
```bash
# Install Vercel CLI: npm i -g vercel

# Deploy
vercel

# Set environment variable in Vercel dashboard
# COHERE_API_KEY = CKaP1q2LMynVtB6FJxACsz7Wdg57r8hKKmEwBIEL
```

### 3. 🐙 GitHub Pages + Netlify Functions
1. Push to GitHub (already done)
2. Connect Netlify to your GitHub repo
3. Set build command: `pip install -r requirements.txt`
4. Set environment variables in Netlify

### 4. 🌊 Railway
```bash
# Connect Railway to your GitHub repo
# Set environment variable: COHERE_API_KEY
# Deploy automatically on push
```

### 5. 🎨 Render
```bash
# Connect Render to your GitHub repo
# Set environment variable: COHERE_API_KEY
# Use: gunicorn app:app (or python app.py)
# Auto-deploy on push
```

## 🔄 Redeploying After Cohere API Fix

If you're getting "Generate API was removed" errors:

1. **Pull latest code**: `git pull origin master`
2. **Redeploy** on your platform
3. **Clear any cached deployments**
4. **Verify environment variables** are set

## Environment Variables Required

For all platforms, set:
```
COHERE_API_KEY=CKaP1q2LMynVtB6FJxACsz7Wdg57r8hKKmEwBIEL
```

## Files Added for Deployment

- `Procfile` - Heroku process definition
- `runtime.txt` - Python version specification
- `vercel.json` - Vercel configuration
- `requirements.txt` - Python dependencies (already exists)

## Repository URL
```
git@github.com:kelvin-lee-cl/story.git
```

Your app is ready for deployment! 🎉
