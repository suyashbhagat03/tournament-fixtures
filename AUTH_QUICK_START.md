# 🔐 Authentication Quick Start

## ✅ What's Done

All 8 tournament brackets now have:
- ✅ **Login/Logout** buttons
- ✅ **Role-based access control** (Viewer/Editor/Admin)
- ✅ **Read-only mode by default** (anyone can view, only authorized users can edit)
- ✅ **Firebase Authentication** integration
- ✅ **User management** capabilities for admins

---

## 🚀 Setup in 3 Steps (5 Minutes)

### **Step 1: Enable Firebase Authentication**

1. Open: https://console.firebase.google.com/project/insportsathon/authentication
2. Click **"Get Started"**
3. Select **"Email/Password"** provider
4. Toggle **"Enable"** → Save
5. Done! ✅

---

### **Step 2: Create Admin User**

1. Open `setup_admin.html` in your browser:
   ```
   file:///Users/sbhagat/Insports/setup_admin.html
   ```

2. Fill in the form:
   - **Email:** Your admin email
   - **Password:** Strong password (min 6 chars)
   - **Name:** Your full name
   - **Role:** Admin (pre-selected)

3. Click **"Create Admin User"**

4. Success! ✅ You now have an admin account

---

### **Step 3: Test It!**

1. Open any bracket (e.g., `Bracket_Chess.html`)

2. Without login:
   - ❌ Cannot click players to select winner
   - ❌ Cannot edit scores
   - ❌ Cannot edit names
   - ✅ Can view everything
   - 🔒 See "READ-ONLY mode" banner

3. Click **"Login"** button (top-right)

4. Enter your admin credentials

5. After login:
   - ✅ Can select winners
   - ✅ Can edit scores and names
   - ✅ Can reset brackets
   - 🔴 See "ADMIN" badge
   - No more read-only banner!

---

## 👥 User Roles Explained

### **Viewer** (Default)
- Anyone without login
- Can view brackets, print, export
- **Cannot** edit anything
- Perfect for: Public viewing

### **Editor**
- Can do everything Viewers can
- **Plus:** Edit brackets, select winners, change scores
- Perfect for: Tournament organizers

### **Admin**
- Can do everything Editors can
- **Plus:** Manage users (add/remove/change roles)
- Perfect for: Main admin/coordinator

---

## 📱 How It Works

### **Public Access (No Login)**
```
User opens bracket → Sees read-only banner → Can view but not edit
```

### **Editor Access**
```
User clicks Login → Enters credentials → Green "EDITOR" badge → Can edit
```

### **Admin Access**
```
User clicks Login → Enters credentials → Red "ADMIN" badge → Full control
```

---

## 🎯 Common Scenarios

### **Scenario A: Only organizers can edit**
1. Create 2-3 admin/editor accounts for organizers
2. Share bracket URLs publicly (no login needed to view)
3. Only organizers login to make edits
4. **Perfect for:** Public tournament viewing

### **Scenario B: Completely private**
1. Create viewer accounts for specific people
2. Share URLs + login credentials privately
3. Adjust Firebase rules to require login for viewing
4. **Perfect for:** Internal/private tournaments

### **Scenario C: Multiple organizers**
1. Create 1 admin account (you)
2. Create editor accounts for other organizers
3. They can edit, you can manage users
4. **Perfect for:** Team management

---

## 🔑 Adding More Users

### **Method 1: Firebase Console (Quick)**

1. Go to: https://console.firebase.google.com/project/insportsathon/authentication/users
2. Click **"Add User"**
3. Enter email + password
4. Click **"Add User"**
5. **Important:** Now assign role in database (see below)

### **Method 2: Assign User Role**

After creating user in console:

1. Go to: https://console.firebase.google.com/project/insportsathon/database
2. Navigate to `users` node
3. Add entry:
   ```
   users/
     └─ {USER_UID}/          ← Copy from Authentication → Users
          ├─ email: "user@example.com"
          ├─ name: "User Name"
          └─ role: "editor"  ← or "viewer" or "admin"
   ```
4. Save ✅

---

## 🆘 Troubleshooting

### **Problem: "Login failed"**
**Solution:** 
- Check Firebase Authentication is enabled
- Verify email/password in Firebase Console → Authentication → Users

### **Problem: "Still read-only after login"**
**Solution:**
- Check user role in Firebase Database → `users/{uid}/role`
- Should be `"editor"` or `"admin"` (not `"viewer"`)

### **Problem: "Login button not showing"**
**Solution:**
- Already logged in
- Open browser DevTools → Console → Type: `window.location.reload(true)`

---

## 📊 Firebase Console Quick Links

| Task | Link |
|------|------|
| View Users | https://console.firebase.google.com/project/insportsathon/authentication/users |
| Add User | https://console.firebase.google.com/project/insportsathon/authentication/users |
| Database | https://console.firebase.google.com/project/insportsathon/database |
| Project Home | https://console.firebase.google.com/project/insportsathon/overview |

---

## 📄 Full Documentation

- **`AUTH_SETUP_GUIDE.md`** - Complete setup guide with all details
- **`setup_admin.html`** - Create admin user (open in browser)
- **`DEPLOY_NOW.md`** - Deploy brackets to Firebase Hosting

---

## ✅ Checklist

- [ ] Enable Firebase Authentication (Step 1)
- [ ] Create admin user via `setup_admin.html` (Step 2)
- [ ] Test login on a bracket (Step 3)
- [ ] Add more users as needed
- [ ] Deploy to Firebase Hosting (optional, see `DEPLOY_NOW.md`)
- [ ] Share bracket URLs with team!

---

## 🎊 You're Ready!

Your tournament brackets now have:
- ✅ Secure authentication
- ✅ Role-based access control
- ✅ Read-only mode for viewers
- ✅ Edit mode for authorized users
- ✅ Real-time Firebase sync

**Total setup time:** 5 minutes  
**Security level:** 🔒🔒🔒🔒⭐

---

## 🔥 Next Step: Deploy!

Once you've tested locally, deploy to make it accessible from anywhere:

```bash
cd /Users/sbhagat/Insports
firebase login
./deploy-now.sh
```

See `DEPLOY_NOW.md` for full deployment instructions.

---

**Questions? Check `AUTH_SETUP_GUIDE.md` for comprehensive documentation!**

Good luck with Insportsathon! 🏆🔐

