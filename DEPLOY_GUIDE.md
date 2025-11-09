# 🚀 Deploy to Firebase Hosting

## ⚡ Quick Deploy (5 Minutes)

### **Step 1: Install Firebase CLI**

```bash
npm install -g firebase-tools
```

If you don't have npm, install Node.js first: https://nodejs.org/

---

### **Step 2: Login to Firebase**

```bash
firebase login
```

This will open a browser window. Sign in with your Google account.

---

### **Step 3: Initialize Project**

```bash
cd /Users/sbhagat/Insports
firebase init hosting
```

**Answer the prompts:**

1. **"Select a default Firebase project"**
   - Choose: `insportsathon` (your existing project)

2. **"What do you want to use as your public directory?"**
   - Enter: `.` (just a dot - means current directory)

3. **"Configure as a single-page app?"**
   - Enter: `N` (No)

4. **"Set up automatic builds and deploys with GitHub?"**
   - Enter: `N` (No)

5. **"File ./index.html already exists. Overwrite?"**
   - Enter: `N` (No - keep your file!)

---

### **Step 4: Create .firebaserc**

This file is created automatically by `firebase init`, but if you need to create it manually:

```json
{
  "projects": {
    "default": "insportsathon"
  }
}
```

---

### **Step 5: Update firebase.json**

After `firebase init`, a `firebase.json` file is created. Make sure it looks like this:

```json
{
  "hosting": {
    "public": ".",
    "ignore": [
      "firebase.json",
      "**/.*",
      "**/node_modules/**",
      "**/*.md"
    ]
  }
}
```

---

### **Step 6: Deploy!**

```bash
firebase deploy --only hosting
```

**Output will show:**
```
✔  Deploy complete!

Project Console: https://console.firebase.google.com/project/insportsathon/overview
Hosting URL: https://insportsathon.web.app
```

---

## 🎉 Your Site is Live!

**Access URLs:**
- Main: `https://insportsathon.web.app`
- Alternate: `https://insportsathon.firebaseapp.com`

**Share with organizers:**
- Dashboard: `https://insportsathon.web.app/index.html`
- Table Tennis Singles: `https://insportsathon.web.app/Bracket_TableTennis_Singles.html`
- Chess: `https://insportsathon.web.app/Bracket_Chess.html`
- Etc.

---

## 🔄 How to Update After Changes

**Anytime you make changes to the brackets:**

```bash
cd /Users/sbhagat/Insports
firebase deploy --only hosting
```

Takes ~30 seconds to deploy!

---

## 🌐 Optional: Custom Domain

Want to use your own domain (e.g., `brackets.yourdomain.com`)?

1. **Go to Firebase Console:**
   ```
   https://console.firebase.google.com/project/insportsathon/hosting
   ```

2. **Click "Add custom domain"**

3. **Follow the DNS setup instructions**

4. **Done!** SSL is automatic.

---

## 📊 Monitor Usage

**View analytics:**
```
https://console.firebase.google.com/project/insportsathon/hosting
```

**See:**
- Page views
- Bandwidth usage
- Deploy history

---

## 🆘 Troubleshooting

### **Error: "Permission denied"**
```bash
sudo npm install -g firebase-tools
```

### **Error: "No project active"**
```bash
firebase use insportsathon
```

### **Error: "Command not found: firebase"**
Restart your terminal after installing.

### **Wrong files deployed?**
Check `firebase.json` - make sure `"public": "."` 

---

## 📝 Files to Keep

**DO deploy:**
- ✅ All `.html` files
- ✅ All `.css` files (if any)
- ✅ `index.html` (dashboard)

**DO NOT deploy:**
- ❌ `.git/` folder
- ❌ `node_modules/` (if any)
- ❌ `.md` files (documentation)
- ❌ Source `.csv` files (optional - security)

Update `firebase.json` ignore section as needed.

---

## 🎯 Quick Reference

| Command | Purpose |
|---------|---------|
| `firebase login` | Authenticate |
| `firebase init hosting` | Setup project |
| `firebase deploy --only hosting` | Deploy site |
| `firebase serve` | Test locally (localhost:5000) |
| `firebase hosting:channel:deploy preview` | Deploy preview |

---

## 🔒 Security Note

**Your Firebase config in HTML files is PUBLIC.** This is fine because:
- Firebase database rules protect your data
- Config only allows connecting to YOUR database
- Rules determine what users can read/write

**But if you want extra security:**

1. Make sure Firebase rules are set correctly
2. Don't deploy source `.csv` files (delete before deploy)
3. Consider adding authentication for editing

---

## 🎊 You're Done!

Your tournament brackets are now:
- ✅ Live on the internet
- ✅ Accessible from any device
- ✅ Fast (Firebase CDN)
- ✅ Secure (HTTPS)
- ✅ Synced in real-time (Firebase DB)

**Share the URL with your team!** 🚀

---

## 📱 Access from Mobile

Your brackets work perfectly on mobile devices!

Just share: `https://insportsathon.web.app`

---

**Last Updated:** November 7, 2025  
**Deployment Time:** ~5 minutes  
**Cost:** FREE (Firebase free tier)

