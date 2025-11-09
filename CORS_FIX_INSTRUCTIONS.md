# 🔧 CORS Error Fix

## ❌ Error You're Seeing:
```
CORS header missing allow origin header
Access to fetch at '...' from origin 'null' has been blocked by CORS policy
```

## ✅ Solution: Update Apps Script with CORS Headers

### STEP 1: Update Apps Script Code (5 minutes)

1. Open your Google Sheet: **"Insportsathon_Tournament_Data"**
2. Click **Extensions → Apps Script**
3. **DELETE** all existing code
4. **COPY** the updated code from `Apps_Script_Code.js` (with CORS support)
5. **PASTE** into the Apps Script editor
6. Click **Save** (💾)

### STEP 2: Re-Deploy the Web App (IMPORTANT!)

**⚠️ You MUST create a NEW deployment for changes to take effect!**

#### Option A: New Deployment (Recommended)
1. Click **Deploy → New deployment**
2. Click gear icon ⚙️ → Select **"Web app"**
3. Configure:
   - Description: **"Tournament API v2 - CORS Fix"**
   - Execute as: **"Me"**
   - Who has access: **"Anyone"**
4. Click **Deploy**
5. **Copy the NEW Web App URL**
6. ⚠️ **Important:** The URL will be different! Update all HTML files with new URL

#### Option B: Manage Deployments (Keep Same URL)
1. Click **Deploy → Manage deployments**
2. Click the **pencil/edit icon** ✏️ next to your existing deployment
3. Under "Version", click **New version**
4. Add description: **"Added CORS support"**
5. Click **Deploy**
6. Your URL stays the same! ✅

**Option B is EASIER** - no need to update HTML files again!

### STEP 3: Test

1. Open any bracket HTML file in browser
2. Check browser console (F12)
3. CORS error should be gone! ✅
4. Sync status should show: **"✅ Synced with Google Sheets"**

---

## 🔍 What Changed?

### Before (No CORS):
```javascript
return ContentService.createTextOutput(JSON.stringify(result))
  .setMimeType(ContentService.MimeType.JSON);
```

### After (With CORS):
```javascript
return ContentService.createTextOutput(JSON.stringify(result))
  .setMimeType(ContentService.MimeType.JSON)
  .setHeader('Access-Control-Allow-Origin', '*')
  .setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
  .setHeader('Access-Control-Allow-Headers', 'Content-Type');
```

These headers tell the browser:
- ✅ Allow requests from any origin (`*`)
- ✅ Allow GET, POST, and OPTIONS methods
- ✅ Allow Content-Type header

---

## 🚨 Still Getting CORS Error?

### Check 1: Did you re-deploy?
- Changes don't take effect until you create a new deployment
- Use **Manage deployments → Edit → New version**

### Check 2: Using the correct URL?
- If you created a NEW deployment, the URL changed
- Copy the new URL and update all 8 HTML files

### Check 3: Clear browser cache
- Press **Ctrl + Shift + R** (Windows/Linux)
- Press **Cmd + Shift + R** (Mac)
- Or use incognito/private browsing mode

### Check 4: Authorization
- Make sure you authorized the script when deploying
- Check "Who has access" is set to **"Anyone"**

---

## 💡 Alternative: Use a Local Web Server

If CORS issues persist, serve files through a local web server instead of opening them directly:

### Option 1: Python (Easiest)
```bash
cd /Users/sbhagat/Insports
python3 -m http.server 8000
```
Then open: http://localhost:8000/Bracket_Chess.html

### Option 2: Node.js
```bash
npx http-server -p 8000
```
Then open: http://localhost:8000/Bracket_Chess.html

### Option 3: VS Code Extension
Install "Live Server" extension → Right-click HTML file → "Open with Live Server"

---

## ✅ Verification

Your sync is working when you see:

1. **Sync status shows:** "✅ Synced with Google Sheets"
2. **Browser console (F12) shows:** No CORS errors
3. **Google Sheet updates:** When you enter scores
4. **Brackets sync:** Changes appear on other machines within 5 seconds

---

## 📝 Summary

1. ✅ Update Apps Script code (add CORS headers)
2. ✅ Re-deploy (Manage deployments → Edit → New version)
3. ✅ Test in browser
4. ✅ CORS error gone!

---

Need more help? Check browser console (F12) for specific error messages.

