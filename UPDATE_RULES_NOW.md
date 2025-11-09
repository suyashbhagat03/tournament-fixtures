# 🚨 URGENT: Update Your Firebase Rules NOW

## ⚠️ Current Status: TEST MODE (INSECURE)

Your current rules expire **December 7, 2025** and allow ANYONE to read/write everything!

---

## ✅ **COPY THESE SECURE RULES** (30 seconds to fix!)

### **Step 1: SELECT ALL AND COPY THIS:**

```json
{
  "rules": {
    "tournaments": {
      "$sportKey": {
        ".read": true,
        ".write": "auth != null && (root.child('users').child(auth.uid).child('role').val() == 'editor' || root.child('users').child(auth.uid).child('role').val() == 'admin')"
      }
    },
    "users": {
      "$uid": {
        ".read": "auth != null && (auth.uid == $uid || root.child('users').child(auth.uid).child('role').val() == 'admin')",
        ".write": "auth != null && root.child('users').child(auth.uid).child('role').val() == 'admin'"
      }
    },
    "contacts": {
      "$sportKey": {
        ".read": "auth != null",
        ".write": "auth != null && root.child('users').child(auth.uid).child('role').val() == 'admin'"
      }
    }
  }
}
```

---

### **Step 2: In the Firebase Console (already open in your browser):**

1. **Select all** the old test mode rules (Cmd+A or Ctrl+A)
2. **Delete** them
3. **Paste** the secure rules from above
4. **Click** the blue **"Publish"** button (top right corner)
5. **Confirm** in the dialog

---

### **Step 3: Verify**

After publishing, you should see:
- ✅ **No yellow warning banner**
- ✅ **No expiry date**
- ✅ **Nested structure** with `tournaments`, `users`, `contacts`

---

## 🔒 **What These Secure Rules Do:**

| Path | Who Can Read | Who Can Write |
|------|--------------|---------------|
| `/tournaments/{sport}/` | **Everyone** (public brackets) | **Editor & Admin ONLY** ✅ |
| `/contacts/{sport}/` | **Logged-in users ONLY** | **Admin ONLY** ✅ |
| `/users/{uid}/` | **Owner & Admin ONLY** | **Admin ONLY** ✅ |

---

## ✅ **After Publishing:**

Your database will be **secure**:
- ❌ Anonymous users **cannot** see contact info
- ❌ Viewers **cannot** modify brackets
- ❌ Editors **cannot** access user management
- ✅ Only authorized users can edit
- ✅ Only admins can manage contacts and users

---

## 🚀 **DO THIS NOW!**

**Time required:** 30 seconds  
**Difficulty:** Copy + Paste  
**Urgency:** HIGH (currently anyone can access your data)

---

**Questions?** Let me know after you've published the rules!

