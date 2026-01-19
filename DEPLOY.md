# 🚀 Deploy to Render

## Quick Deployment Steps:

### 1. **Push to GitHub:**
```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin YOUR_GITHUB_REPO_URL
git push -u origin main
```

### 2. **Deploy on Render:**
1. Go to [render.com](https://render.com)
2. Sign up/Login with GitHub
3. Click "New +" → "Web Service"
4. Connect your GitHub repository
5. Use these settings:
   - **Name:** canteen-management
   - **Environment:** Python 3
   - **Build Command:** `./build.sh`
   - **Start Command:** `gunicorn canteen.wsgi:application`

### 3. **Environment Variables:**
Render will auto-generate:
- `SECRET_KEY` (auto-generated)
- `DEBUG=False`

### 4. **Access Your App:**
- **Live URL:** `https://your-app-name.onrender.com`
- **Admin:** `https://your-app-name.onrender.com/admin`
- **Credentials:** admin / admin123

## 📁 Files Added for Deployment:
- ✅ `build.sh` - Build script
- ✅ `render.yaml` - Render configuration
- ✅ `runtime.txt` - Python version
- ✅ Updated `requirements.txt` - Production dependencies
- ✅ Updated `settings.py` - Production settings

## 🔧 Production Features:
- ✅ **Gunicorn** - Production WSGI server
- ✅ **WhiteNoise** - Static file serving
- ✅ **Environment Variables** - Secure configuration
- ✅ **Auto Migration** - Database setup
- ✅ **Auto Admin Creation** - Ready to use
- ✅ **Sample Data** - Pre-populated menu

Your canteen management system is ready for production! 🎉