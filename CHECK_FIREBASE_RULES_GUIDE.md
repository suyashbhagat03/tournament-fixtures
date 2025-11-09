# 🔍 How to Check Firebase Database Rules

## 📋 **Step-by-Step Guide**

### **Method 1: Firebase Console (Easiest)**

#### **Step 1: Open Firebase Console**
Go to: https://console.firebase.google.com/

Or run:
```bash
chmod +x check_firebase_rules.sh
./check_firebase_rules.sh
```

---

#### **Step 2: Navigate to Database Rules**

1. **Select your project:** Click on **"insportsathon"**

2. **Open Realtime Database:**
   - Left sidebar → Click **"Realtime Database"**
   - OR click **"Build"** → **"Realtime Database"**

3. **Go to Rules tab:**
   - Top menu → Click **"Rules"** (next to "Data", "Usage", "Backups")

---

#### **Step 3: View Current Rules**

You'll see a JSON editor with your current rules.

---

## ⚠️ **What You Might See**

### **Scenario A: TEST MODE (INSECURE)**

```json
{
  "rules": {
    ".read": true,
    ".write": true
  }
}
```

**Status:** 🚨 **INSECURE - Anyone can read/write everything!**

**Warning shown:**
```
⚠️ Your security rules are defined as public, so anyone can steal,
modify, or delete data in your database. You should configure more
restrictive rules before going into production.
```

**Expiry date shown:** (e.g., "Rules expire on Dec 8, 2025")

**Action:** ❌ **UPDATE IMMEDIATELY**

---

### **Scenario B: SECURE MODE (GOOD)**

```json
{
  "rules": {
    "tournaments": {
      "$sportKey": {
        ".read": true,
        ".write": "auth != null && (root.child('users')..."
      }
    },
    "users": {
      "$uid": {
        ".read": "auth != null && ...",
        ".write": "auth != null && ..."
      }
    },
    "contacts": {
      "$sportKey": {
        ".read": "auth != null",
        ".write": "auth != null && ..."
      }
    }
  }
}
```

**Status:** ✅ **SECURE - Role-based access control**

**No warnings shown**

---

## 🔧 **How to Update Rules (If in Test Mode)**

### **In the Firebase Console:**

1. **Delete** the existing test mode rules

2. **Copy** the contents from your local `database.rules.json` file

3. **Paste** into the Firebase Console editor

4. **Click** the blue **"Publish"** button (top right corner)

5. **Confirm** in the dialog that appears

6. ✅ **Done!** Your database is now secure

---

## 📍 **Direct Links**

### **Quick Access:**
- **Console Home:** https://console.firebase.google.com/
- **Your Project:** https://console.firebase.google.com/project/insportsathon
- **Database Rules:** https://console.firebase.google.com/project/insportsathon/database/insportsathon-default-rtdb/rules
- **Database Data:** https://console.firebase.google.com/project/insportsathon/database/insportsathon-default-rtdb/data

---

## 🔍 **Method 2: Firebase CLI (Terminal)**

### **Check if logged in:**
```bash
firebase projects:list
```

**Expected output:**
```
✔ Preparing the list of your Firebase projects
┌───────────────┬──────────────┬────────────────┬──────────────┐
│ Project ID    │ Display Name │ Resource       │ Project      │
│               │              │ Location       │ Number       │
├───────────────┼──────────────┼────────────────┼──────────────┤
│ insportsathon │ Insportsathon│ asia-southeast1│ 197165877753 │
└───────────────┴──────────────┴────────────────┴──────────────┘
```

---

### **Get current rules:**
```bash
firebase database:get / --project insportsathon
```

**Note:** This gets the **data**, not the rules.

---

### **Deploy new rules:**
```bash
firebase deploy --only database --project insportsathon
```

This uploads your local `database.rules.json` to Firebase.

---

## 📊 **Visual Guide**

### **What the Firebase Console Looks Like:**

```
┌─────────────────────────────────────────────────────┐
│  Firebase Console                                   │
├─────────────────────────────────────────────────────┤
│                                                     │
│  [Build ▼]  Realtime Database                      │
│                                                     │
│  [Data] [Rules] [Usage] [Backups]  ← Click "Rules" │
│  ──────────────────────────────────────────────    │
│                                                     │
│  Rules Editor:                    [Publish] ← Click│
│  ┌──────────────────────────────────────────┐     │
│  │ {                                        │     │
│  │   "rules": {                             │     │
│  │     ".read": true,   ← This is test mode │     │
│  │     ".write": true   ← INSECURE!         │     │
│  │   }                                      │     │
│  │ }                                        │     │
│  └──────────────────────────────────────────┘     │
│                                                     │
│  ⚠️ Your security rules are defined as public...   │
│     Rules expire on: Dec 8, 2025                   │
│                                                     │
└─────────────────────────────────────────────────────┘
```

---

## ✅ **Quick Check Script**

Run this to open Firebase Console directly to rules:

```bash
chmod +x check_firebase_rules.sh
./check_firebase_rules.sh
```

This will:
1. Open your browser
2. Navigate directly to Database Rules
3. Show current rules
4. You can see if you're in test mode or secure mode

---

## 🎯 **What to Look For**

| Indicator | Test Mode (Bad) | Secure Mode (Good) |
|-----------|-----------------|-------------------|
| **Rules structure** | Just `.read` and `.write` at root | Nested paths: `tournaments`, `users`, `contacts` |
| **Warnings** | ⚠️ Yellow warning banner | ✅ No warnings |
| **Expiry date** | Shows expiration date | No expiration |
| **Status** | 🚨 INSECURE | ✅ SECURE |

---

## 🚀 **Action Plan**

1. ✅ Run `./check_firebase_rules.sh` to open console
2. 👀 Check if you see test mode rules
3. ⚠️ If test mode → Copy `database.rules.json` and publish
4. ✅ If secure mode → You're all set!

---

## 📞 **Need Help?**

If you see test mode rules:
1. Open local file: `database.rules.json`
2. Copy entire contents
3. Paste in Firebase Console
4. Click "Publish"
5. Done! 🎉

**Time required:** ~2 minutes

