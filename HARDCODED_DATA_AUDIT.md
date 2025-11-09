# 📊 Hardcoded Data Remaining in HTML Files

## ✅ **Removed (Secured)**
- ~~Contact Information (Email & Phone)~~ → Now in Firebase `/contacts/{SPORT_KEY}`

---

## 🔥 **Still Hardcoded in Bracket HTML Files**

### 1. **Firebase Configuration** (Lines ~192-199)
```javascript
const firebaseConfig = {
    apiKey: "AIzaSyC2-o5Oo1y0Qkv8JRKa9eM9T4DKzg_fNEQ",
    authDomain: "insportsathon.firebaseapp.com",
    databaseURL: "https://insportsathon-default-rtdb.asia-southeast1.firebasedatabase.app",
    projectId: "insportsathon",
    storageBucket: "insportsathon.firebasestorage.app",
    messagingSenderId: "197165877753",
    appId: "1:197165877753:web:caa11db729bb62932f5528"
};
```
**Where:** All 8 bracket HTML files  
**Security:** ✅ Safe - Firebase config is public, security comes from database rules  
**Recommendation:** Keep as-is

---

### 2. **Sport Key** (Line ~383)
```javascript
const SPORT_KEY = 'Chess';  // or TableTennis_Singles, FIFA25, etc.
```
**Where:** All 8 bracket HTML files  
**Security:** ✅ Safe - Just identifies the sport  
**Recommendation:** Keep as-is

---

### 3. **Initial Tournament Data** (Line ~384)
```javascript
const initialRoundsData = [
    [
        {"player1": "Hari Prasad", "player2": "Sayantan Banerjee", ...},
        {"player1": "Chinmay Parab", "player2": "ANANT GIRIA", ...}
    ],
    [
        {"player1": "TBD", "player2": "TBD", ...},
        ...
    ],
    ...
];
```
**Where:** All 8 bracket HTML files  
**Contains:**
- Player/Team names
- Initial matchups
- Match structure (rounds, matchIds)
- TBD placeholders

**Security:** ⚠️ **MIXED**
- ✅ **Player names alone** → Safe to show (they're on brackets anyway)
- ❌ **But:** This is initial state only. Live bracket state is in Firebase.

**Recommendation:** Keep as-is (needed for fresh tournament setup)

---

### 4. **Bye Players List** (Line ~385)
```javascript
const byePlayers = new Set([
    "Avneesh Dwivedi", "Vikram ghadge", "Piyush Jhanwar", ...
]);
```
**Where:** All 8 bracket HTML files  
**Contains:** Names of players who skip Round 1  
**Security:** ✅ Safe - Just player names  
**Recommendation:** Keep as-is

---

### 5. **Hardcoded Player Names in HTML** (Line ~177)
```html
<div class="byes-section">
    <h3>🎫 62 Players Automatically in Round 2 (Skip Round 1)</h3>
    <div class="bye-list">
        <div class="bye-item">Avneesh Dwivedi</div>
        <div class="bye-item">Vikram ghadge</div>
        ...
    </div>
</div>
```
**Where:** All 8 bracket HTML files (in HTML body)  
**Security:** ✅ Safe - Display-only  
**Recommendation:** Keep as-is

---

## 🌐 **Other HTML Files**

### **`index.html`** - Main Dashboard
- ✅ **Firebase config** (same as brackets)
- ✅ **Static HTML** (sport links, UI)

### **`contact_management.html`** - Contact Editor
- ✅ **Firebase config** (same)
- ✅ **No hardcoded contacts** (loads from Firebase)

### **`user_management.html`** - User Admin Panel
- ✅ **Firebase config** (same)
- ✅ **No hardcoded users** (loads from Firebase)

### **`import_contacts_initial.html`** - Import Tool
- ✅ **Firebase config** (same)
- ✅ **CSV file paths** (public folder references)

---

## 🔒 **Security Summary**

| Data Type | Location | Security Status |
|-----------|----------|-----------------|
| **Contact Info (Email/Phone)** | ❌ Removed from HTML → Firebase | ✅ **SECURE** |
| **Firebase Config** | Hardcoded in HTML | ✅ Safe (public, protected by rules) |
| **Player Names** | Hardcoded in HTML | ✅ Safe (public tournament data) |
| **Initial Bracket Structure** | Hardcoded in HTML | ✅ Safe (needed for setup) |
| **Live Bracket State** | Firebase Real-time DB | ✅ Secure (access controlled) |
| **User Credentials** | Firebase Auth | ✅ Secure (hashed, backend) |
| **User Roles** | Firebase DB `/users/` | ✅ Secure (access controlled) |

---

## 🎯 **What's Secure Now**

### ✅ **Private Information Moved to Firebase:**
1. **Contact Info** → `/contacts/{SPORT_KEY}`
2. **User Emails** → Firebase Auth
3. **User Roles** → `/users/{uid}/role`
4. **Live Bracket State** → `/tournaments/{SPORT_KEY}/rounds`

### ✅ **Public Information (OK in HTML):**
1. **Player Names** → Public anyway (they're tournament participants)
2. **Initial Match Structure** → Just setup template
3. **Firebase Config** → Public by design (security = database rules)

---

## 🚀 **What You Can Do**

### **Option 1: Keep As-Is** (Recommended)
- ✅ Contact info secured
- ✅ Private data in Firebase
- ✅ Public data in HTML (no security risk)

### **Option 2: Move Initial Data to Firebase**
If you want to make bracket structure dynamic:
1. Upload `initialRoundsData` to Firebase
2. Load it on page load
3. Allows changing matchups without editing HTML

**Pros:** More flexible  
**Cons:** More complex, slower initial load  
**Recommendation:** Only if you need to frequently change brackets

---

## 📝 **Conclusion**

**Current Status:** ✅ **SECURE**

The critical private information (contact details) has been moved to Firebase. Everything remaining in HTML is either:
- Public tournament info (player names, brackets)
- Configuration data (Firebase config - safe)
- Initial setup templates (needed for fresh state)

**No further security concerns! 🔒**

