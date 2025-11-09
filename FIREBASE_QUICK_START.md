# 🔥 Firebase Setup - Quick Action Checklist

## ⚡ 15-Minute Setup

### ✅ STEP 1: Create Firebase Project (5 mins)
1. Go to [console.firebase.google.com](https://console.firebase.google.com/)
2. Click "Add project"
3. Name: `Insportsathon`
4. Disable Google Analytics
5. Click "Create project"

### ✅ STEP 2: Enable Realtime Database (3 mins)
1. Left sidebar → "Realtime Database"
2. Click "Create Database"
3. Location: Asia Southeast (Singapore)
4. **Choose: "Start in test mode"** ⚠️
5. Click "Enable"

### ✅ STEP 3: Get Your Config (2 mins)
1. Click gear icon ⚙️ → "Project settings"
2. Scroll to "Your apps"
3. Click web icon `</>`
4. App name: `Insportsathon Brackets`
5. **Copy the `firebaseConfig` object** 📋

### ✅ STEP 4: Update HTML Files (5 mins)

**Replace the config in ALL 8 files:**

```javascript
// FIND THIS (around line 110):
const firebaseConfig = {
    apiKey: "YOUR_API_KEY_HERE",
    // ... other placeholder values
};

// REPLACE WITH YOUR CONFIG:
const firebaseConfig = {
    apiKey: "AIzaSyA...",  // Your actual values
    authDomain: "insportsathon-xxxxx.firebaseapp.com",
    databaseURL: "https://insportsathon-xxxxx-default-rtdb.firebaseio.com",
    projectId: "insportsathon-xxxxx",
    storageBucket: "insportsathon-xxxxx.appspot.com",
    messagingSenderId: "123456789012",
    appId: "1:123456789012:web:abc123..."
};
```

**Files to update:**
- [ ] `Bracket_TableTennis_Singles.html`
- [ ] `Bracket_TableTennis_Doubles.html`
- [ ] `Bracket_Carrom_Singles.html`
- [ ] `Bracket_Carrom_Doubles.html`
- [ ] `Bracket_Foosball.html`
- [ ] `Bracket_Snooker.html`
- [ ] `Bracket_FIFA25.html`
- [ ] `Bracket_Chess.html`

---

## 🧪 Test (2 mins)

1. Open any bracket file in browser
2. Check status at top: Should say **"🔥 Connected"** (green)
3. Select a winner → Should see **"🔥 Syncing..."** → **"🔥 Synced ✓"**
4. Open same bracket in 2nd tab → Changes should sync automatically! 🎉

---

## ✨ Done!

Your brackets now have:
- ✅ Real-time sync across all devices
- ✅ Auto-save on every change
- ✅ Works from local files (no server needed)
- ✅ No CORS/403 errors

---

## 🆘 Troubleshooting

| Status | Issue | Fix |
|--------|-------|-----|
| 🟡 "Not Configured" | Config not updated | Paste your Firebase config, save file |
| 🔴 "Connection Error" | Invalid config | Double-check you copied entire config |
| 🔴 "Save Failed" | Database rules | Firebase Console → Rules → Set to `"write": true` |

Full guide: `FIREBASE_SETUP_GUIDE.md`

---

## 📍 Your Firebase Console

Bookmark this: [console.firebase.google.com](https://console.firebase.google.com/)

Monitor data in real-time during the event! 📊

