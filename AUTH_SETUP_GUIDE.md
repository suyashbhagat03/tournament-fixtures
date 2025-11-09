# 🔐 Authentication & Access Control Setup Guide

## Overview

Your tournament brackets now have role-based access control:

| Role | Access Level | Can Do |
|------|-------------|---------|
| **Viewer** (Default) | Read-Only | View brackets, see scores, print |
| **Editor** | Edit Access | Everything Viewer can do + edit brackets, select winners, change scores |
| **Admin** | Full Access | Everything Editor can do + manage users |

**By default, everyone is a VIEWER** (read-only). Only logged-in users with Editor or Admin roles can make changes.

---

## 🚀 Quick Setup (5 Minutes)

### **Step 1: Enable Firebase Authentication**

1. Go to [Firebase Console](https://console.firebase.google.com/project/insportsathon/authentication)
2. Click **"Get Started"**
3. Click **"Email/Password"** under Sign-in providers
4. Toggle **"Enable"** → Save
5. Done! ✅

---

### **Step 2: Create Your First Admin User**

1. Open `setup_admin.html` in your browser:
   ```
   file:///Users/sbhagat/Insports/setup_admin.html
   ```
   
2. Fill in:
   - **Email:** Your email (e.g., `admin@insportsathon.com`)
   - **Password:** Strong password (min 6 characters)
   - **Name:** Your full name
   - **Role:** Admin (pre-selected)

3. Click **"Create Admin User"**

4. Done! ✅ You now have an admin account.

---

### **Step 3: Test Login**

1. Open any bracket (e.g., `Bracket_Chess.html`)
2. Click **"Login"** button (top-right corner)
3. Enter your admin email and password
4. You should now see:
   - Your email displayed
   - **ADMIN** badge
   - Edit features enabled

---

## 🎯 How It Works

### **For Viewers (Default)**

When someone opens a bracket without logging in:
- ✅ Can view all brackets
- ✅ Can see scores and winners
- ✅ Can print brackets
- ❌ Cannot select winners
- ❌ Cannot edit scores or names
- ❌ Cannot reset brackets

**Read-only notice** is displayed at the top.

---

### **For Editors**

When someone logs in with Editor role:
- ✅ Everything Viewers can do
- ✅ Can select winners by clicking player names
- ✅ Can edit scores
- ✅ Can edit player/team names
- ✅ Can change match times
- ✅ Can reset brackets
- ❌ Cannot manage users

**Green EDITOR badge** is displayed.

---

### **For Admins**

When someone logs in with Admin role:
- ✅ Everything Editors can do
- ✅ Can manage users (add/remove/change roles)
- ✅ Full system access

**Red ADMIN badge** is displayed.

---

## 👥 Adding More Users

### **Option A: Create Accounts Manually (Recommended)**

1. Go to [Firebase Console → Authentication → Users](https://console.firebase.google.com/project/insportsathon/authentication/users)
2. Click **"Add User"**
3. Enter:
   - Email
   - Password
4. Click **"Add User"**
5. **Important:** Now assign a role (see below)

---

### **Assigning User Roles**

After creating a user in Firebase Console, you need to assign their role in the Realtime Database:

1. Go to [Firebase Console → Realtime Database](https://console.firebase.google.com/project/insportsathon/database/insportsathon-default-rtdb/data)

2. Find or create the `users` node

3. Add a new entry:
   ```
   users/
     └─ {USER_UID}/          ← Get this from Authentication → Users
          ├─ email: "user@example.com"
          ├─ name: "User Name"
          └─ role: "editor"  ← or "viewer" or "admin"
   ```

4. Save

**To find USER_UID:**
- Firebase Console → Authentication → Users
- Copy the **User UID** column value

---

### **Quick Role Assignment Template**

```json
{
  "users": {
    "USER_UID_HERE": {
      "email": "user@example.com",
      "name": "John Doe",
      "role": "editor",
      "createdAt": "2025-11-07T00:00:00Z"
    }
  }
}
```

---

## 🔒 Security Rules

Your Firebase Realtime Database should have these rules:

```json
{
  "rules": {
    ".read": true,
    ".write": "auth != null",
    "users": {
      ".write": "root.child('users').child(auth.uid).child('role').val() === 'admin'"
    }
  }
}
```

**What this means:**
- Everyone can **read** (view) data
- Only logged-in users can **write** (edit) tournament data
- Only **admins** can modify user roles

---

## 🎨 UI Features

### **Login Button**
- Located: Top-right corner
- Shows: When not logged in
- Click to: Open login modal

### **User Info Badge**
- Shows: Email, role badge, logout button
- Color:
  - Gray border: Viewer
  - Green border: Editor
  - Red border: Admin

### **Read-Only Notice**
- Yellow banner at top
- Shows: When viewing as guest or with Viewer role
- Hides: When logged in as Editor/Admin

### **Edit Controls**
- **Disabled** for Viewers:
  - Player name clicking
  - Score inputs
  - Edit buttons
  - Reset button
  - Match time inputs
- **Enabled** for Editors/Admins

---

## 📱 Usage Scenarios

### **Scenario 1: Public Viewing**

**Goal:** Let anyone view brackets, but only organizers can edit

**Setup:**
1. Create 2-3 admin/editor accounts for organizers
2. Share bracket URLs publicly
3. Public can view, only organizers can login and edit

---

### **Scenario 2: Controlled Access**

**Goal:** Only specific people can view brackets

**Setup:**
1. Create viewer accounts for specific people
2. Share bracket URLs + login credentials
3. Non-users cannot access (set Firebase rules to require auth for reading)

---

### **Scenario 3: Multiple Organizers**

**Goal:** 5 people need edit access

**Setup:**
1. Create 1 admin account (you)
2. Create 4 editor accounts for other organizers
3. Admins can manage user roles if needed

---

## 🛠️ Troubleshooting

### **"Login failed" error**

**Causes:**
1. Firebase Authentication not enabled
2. Wrong email/password
3. User not created in Firebase

**Solution:**
- Check Firebase Console → Authentication → Users
- Verify the email exists
- Try resetting password in Firebase Console

---

### **"Logged in but still read-only"**

**Cause:** User role not set in database

**Solution:**
1. Firebase Console → Realtime Database
2. Check `users/{USER_UID}/role`
3. Should be `"editor"` or `"admin"` (not `"viewer"`)

---

### **"Login button not showing"**

**Cause:** Already logged in or browser cache

**Solution:**
1. Open browser DevTools (F12)
2. Console → Type: `firebase.auth().signOut()`
3. Refresh page

---

### **"Cannot click players to select winner"**

**Cause:** Logged in as Viewer, or not logged in

**Solution:**
- Check role badge (should be green EDITOR or red ADMIN)
- If gray VIEWER, ask admin to change your role to "editor"

---

## 🔑 Default Credentials Template

For your team, create a document like this:

```
INSPORTSATHON BRACKET ACCESS

Admin Account:
Email: admin@insportsathon.com
Password: [strong-password]
Role: Admin

Editor Accounts:
1. organizer1@insportsathon.com / [password] - Editor
2. organizer2@insportsathon.com / [password] - Editor

Viewer Accounts (optional):
- Anyone without login = Read-only viewer
```

---

## 📊 User Management Best Practices

1. **Create 1-2 admins** (backup admin in case you lose access)
2. **Create editors for active organizers** (people who update brackets)
3. **Don't create viewer accounts unless needed** (default is open viewing)
4. **Use strong passwords** (Firebase enforces min 6 characters)
5. **Document credentials** (keep them safe!)

---

## 🎯 Quick Reference

| Task | How To |
|------|--------|
| Create first admin | Open `setup_admin.html` |
| Add more users | Firebase Console → Authentication → Add User |
| Change user role | Firebase Console → Database → `users/{uid}/role` |
| Login to bracket | Click "Login" button → Enter credentials |
| Logout | Click "Logout" button (top-right) |
| Reset password | Firebase Console → Authentication → Users → 3 dots → Reset password |

---

## 🚀 Next Steps

1. ✅ Enable Firebase Authentication (Step 1)
2. ✅ Create admin user with `setup_admin.html` (Step 2)
3. ✅ Test login on a bracket page (Step 3)
4. ⏳ Add more users as needed
5. ⏳ Share bracket URLs with your team!
6. ⏳ Deploy to Firebase Hosting (see `DEPLOY_NOW.md`)

---

## 💡 Pro Tips

1. **Test with incognito window** to see what viewers see
2. **Keep admin password secure** - it has full access
3. **Use editor role for most organizers** - they don't need user management
4. **Firebase Console is your friend** - bookmark it for quick access
5. **Viewers can still export/print** - read-only doesn't mean no access

---

## 🆘 Need Help?

1. Check this guide first
2. Check browser console for errors (F12)
3. Verify Firebase Authentication is enabled
4. Verify user exists in Firebase Console
5. Verify user role in Realtime Database

---

**Setup time:** ~5 minutes  
**Difficulty:** ⭐⭐☆☆☆ (Easy)  
**Security:** 🔒🔒🔒🔒⭐ (Very Secure)

Good luck with your tournament! 🏆🔥

