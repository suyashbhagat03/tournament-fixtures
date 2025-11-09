# 🔍 Firebase Connection Debugging

## Step 1: Check Browser Console

1. **Open the bracket in browser** (e.g., `Bracket_TableTennis_Singles.html`)
2. **Open Developer Console:**
   - Chrome/Edge: Press `F12` or `Cmd+Option+J` (Mac) / `Ctrl+Shift+J` (Windows)
   - Firefox: Press `F12` or `Cmd+Shift+K` (Mac) / `Ctrl+Shift+K` (Windows)
3. **Look for errors** (red text)

---

## Common Issues & Solutions

### ❌ Issue 1: "Firebase: No Firebase App '[DEFAULT]' has been created"
**Cause:** Firebase SDK failed to initialize

**Fix:**
- Check if you have internet connection (Firebase SDK loads from CDN)
- Try hard refresh: `Cmd+Shift+R` (Mac) or `Ctrl+Shift+F5` (Windows)

---

### ❌ Issue 2: "PERMISSION_DENIED: Permission denied"
**Cause:** Firebase database rules are blocking access

**Fix:**
1. Go to Firebase Console: https://console.firebase.google.com/
2. Select project: `insportsathon`
3. Click "Realtime Database" in left sidebar
4. Click "Rules" tab
5. Make sure rules are:
   ```json
   {
     "rules": {
       ".read": true,
       ".write": true
     }
   }
   ```
6. Click "Publish"

---

### ❌ Issue 3: "Failed to load resource: net::ERR_BLOCKED_BY_CLIENT"
**Cause:** Ad blocker or browser extension blocking Firebase

**Fix:**
- Disable ad blockers/extensions temporarily
- Add Firebase to whitelist

---

### ❌ Issue 4: Module import errors
**Cause:** Browser doesn't support ES6 modules or CORS issue

**Fix:**
- Use a modern browser (Chrome, Firefox, Edge, Safari)
- Don't use Internet Explorer

---

### ❌ Issue 5: "Database not found"
**Cause:** Realtime Database not created in Firebase

**Fix:**
1. Go to Firebase Console
2. Click "Realtime Database"
3. If you see "Get Started", click it to create database
4. Choose location: Asia Southeast (Singapore)
5. Start in test mode
6. Click "Enable"

---

## Quick Diagnostic Test

**Open Browser Console and run this:**

```javascript
// Check if Firebase config is loaded
console.log('Firebase Config:', firebaseConfig);

// Check if Firebase is configured
console.log('Is Configured:', isFirebaseConfigured);

// Check if database reference exists
console.log('Database Ref:', dataRef);
```

**Expected Output:**
```
Firebase Config: {apiKey: "AIzaSy...", authDomain: "insportsathon...", ...}
Is Configured: true
Database Ref: DatabaseReference {...}
```

---

## Step 2: Verify Firebase Setup

**Check these in Firebase Console:**

### ✅ Checklist:
- [ ] Project exists: `insportsathon`
- [ ] Realtime Database is enabled
- [ ] Database URL matches: `https://insportsathon-default-rtdb.asia-southeast1.firebasedatabase.app`
- [ ] Database rules allow read/write (test mode)
- [ ] Web app is registered

---

## Step 3: Test Connection Manually

**In Browser Console, try:**

```javascript
// Test Firebase import
import('https://www.gstatic.com/firebasejs/10.7.1/firebase-app.js')
  .then(() => console.log('✅ Firebase SDK loaded'))
  .catch(err => console.error('❌ Firebase SDK failed:', err));
```

---

## What to Report Back

Please share:
1. **Any error messages** from browser console (red text)
2. **Which browser** you're using (Chrome, Firefox, Safari, Edge)
3. **Database URL** shown in Firebase Console
4. **Screenshot** of Firebase Console showing Realtime Database

---

## Quick Fix Checklist

Try these in order:

1. ✅ **Hard refresh browser** (`Cmd+Shift+R` / `Ctrl+Shift+F5`)
2. ✅ **Check internet connection**
3. ✅ **Disable ad blockers**
4. ✅ **Try different browser** (Chrome recommended)
5. ✅ **Check Firebase Console** (database enabled?)
6. ✅ **Verify database rules** (allow read/write?)
7. ✅ **Clear browser cache**

---

## Most Likely Issue

**If you're seeing "⚠️ FIREBASE SETUP REQUIRED"**, it means:

The JavaScript check `firebaseConfig.apiKey !== "YOUR_API_KEY_HERE"` is returning `false`.

This could happen if:
1. The file wasn't saved after editing
2. Browser is showing cached version
3. Wrong file is open in browser

**Try this:**
1. Close all browser tabs with the bracket
2. Open your code editor
3. Verify line 115 shows: `apiKey: "AIzaSyC2-o5Oo1y0Qkv8JRKa9eM9T4DKzg_fNEQ",`
4. Save the file again (Cmd+S / Ctrl+S)
5. Open the file fresh in browser

---

Need more help? Share the console errors and I'll help you fix it! 🔥

