# 📦 Firebase Hosting - Files Deployment Checklist

## ✅ **REQUIRED for Firebase Hosting** (Deploy These)

### **🌐 Core Application Files (HTML)**
```
✅ index.html                          # Main dashboard
✅ Bracket_Chess.html                  # Chess tournament bracket
✅ Bracket_TableTennis_Singles.html    # Table Tennis Singles
✅ Bracket_TableTennis_Doubles.html    # Table Tennis Doubles
✅ Bracket_Carrom_Singles.html         # Carrom Singles
✅ Bracket_Carrom_Doubles.html         # Carrom Doubles
✅ Bracket_Foosball.html               # Foosball
✅ Bracket_Snooker.html                # Snooker
✅ Bracket_FIFA25.html                 # FIFA 25
✅ contact_management.html             # Contact management (admin)
✅ user_management.html                # User management (admin)
✅ import_contacts_initial.html        # One-time contact import tool
```
**Total: 12 HTML files**

---

### **📊 Data Files (CSV)**
```
✅ Chess.csv                           # Chess registrations
✅ TableTennis_Singles.csv             # TT Singles registrations
✅ TableTennis_Doubles.csv             # TT Doubles registrations
✅ Carrom_Singles.csv                  # Carrom Singles registrations
✅ Carrom_Doubles.csv                  # Carrom Doubles registrations
✅ Foosball.csv                        # Foosball registrations
✅ Snooker.csv                         # Snooker registrations
✅ FIFA25.csv                          # FIFA registrations
```
**Total: 8 CSV files**

**Why needed:** The `import_contacts_initial.html` reads these to populate Firebase contacts.

---

### **⚙️ Firebase Configuration**
```
✅ firebase.json                       # Firebase hosting config
```
**Note:** This is auto-generated and already exists. Keep it!

---

## ❌ **NOT REQUIRED for Firebase Hosting** (Don't Deploy)

### **📝 Documentation Files**
```
❌ All *.md files (30+ files)
   - README_FIREBASE.md
   - FIREBASE_SETUP_GUIDE.md
   - UPDATE_RULES_NOW.md
   - DATABASE_BLOAT_PROTECTION.md
   - RULES_COMPARISON.md
   - HARDCODED_DATA_AUDIT.md
   - CHECK_FIREBASE_RULES_GUIDE.md
   - INITIAL_IMPORT_GUIDE.md
   - SECURE_CONTACT_LOADING.md
   - ... (all others)
```
**Why:** Documentation for developers, not needed by end users.

---

### **🐍 Python Scripts**
```
❌ add_apply_controls_call.py
❌ add_auth_to_brackets.py
❌ add_auth.py
❌ add_firebase_contact_loading.py
❌ fix_auth_apply_controls.py
❌ fix_auth_permissions.py
❌ fix_back_button.py
❌ fix_edit_permissions_final.py
❌ fix_match_time_all.py
❌ fix_reset_admin_only.py
❌ fix_user_role_scope.py
❌ fix_view_only_strict.py
❌ fix_viewer_mode.py
❌ move_apply_edit_controls.py
❌ remove_permission_checks.py
❌ restore_permission_checks.py
❌ update_async_contacts.py
❌ update_contacts_firebase.py
```
**Why:** Build/maintenance scripts, not part of the web app.

---

### **🔧 Shell Scripts**
```
❌ check_firebase_rules.sh
❌ deploy_security_rules.sh
❌ deploy-now.sh
❌ deploy.sh
❌ start_server.sh
```
**Why:** Local development/deployment tools, not for hosting.

---

### **🔐 Database Rules Files**
```
❌ database.rules.json
❌ database.rules.enhanced.json
❌ database.rules.whitelist.json
```
**Why:** These are deployed separately using `firebase deploy --only database`, NOT via hosting.

---

### **📄 Text Fixtures Files**
```
❌ Fixtures_Chess.txt
❌ Fixtures_TableTennis_Singles.txt
❌ Fixtures_TableTennis_Doubles.txt
❌ Fixtures_Carrom_Singles.txt
❌ Fixtures_Carrom_Doubles.txt
❌ Fixtures_Foosball.txt
❌ Fixtures_Snooker.txt
❌ Fixtures_FIFA25.txt
```
**Why:** Were used for initial bracket generation. Tournament data is now in Firebase.

---

### **📦 Source Data**
```
❌ Insportsathon Responses - Sheet2.csv
```
**Why:** Original master data, already split into sport-specific CSVs.

---

### **📁 Empty Folders**
```
❌ tournament_data/
```
**Why:** Was for local file persistence (removed). Only contains a README.

---

### **🗃️ Google Apps Script**
```
❌ Apps_Script_Code.js
```
**Why:** Was for Google Sheets integration (removed in favor of Firebase).

---

## 📊 **Deployment Summary**

### **Files to Deploy:**
```
20 files total:
- 12 HTML files
- 8 CSV files
```

### **Files to Ignore:**
```
70+ files:
- 30+ .md documentation files
- 18 .py Python scripts
- 5 .sh shell scripts
- 3 database.rules.*.json files
- 8 Fixtures_*.txt files
- 1 Apps_Script_Code.js
- 1 Insportsathon Responses - Sheet2.csv
- 1 tournament_data/ folder
```

---

## 🚀 **How to Deploy Only Required Files**

### **Option 1: Use .firebaserc Ignore Patterns (Recommended)**

Edit your `firebase.json`:

```json
{
  "hosting": {
    "public": ".",
    "ignore": [
      "firebase.json",
      "**/.*",
      "**/node_modules/**",
      "**/*.md",
      "**/*.py",
      "**/*.sh",
      "**/*.txt",
      "**/*.js",
      "database.rules*.json",
      "Insportsathon Responses - Sheet2.csv",
      "tournament_data/**"
    ]
  }
}
```

Then deploy:
```bash
firebase deploy --only hosting
```

---

### **Option 2: Create a Public Folder (Cleanest)**

Move only required files to a `public/` folder:

```bash
mkdir public

# Copy HTML files
cp *.html public/

# Copy CSV files
cp Chess.csv TableTennis_*.csv Carrom_*.csv Foosball.csv Snooker.csv FIFA25.csv public/

# Update firebase.json
# Change "public": "." to "public": "public"

# Deploy
firebase deploy --only hosting
```

---

### **Option 3: Manual Selection**

Use `firebase deploy --only hosting` with the ignore patterns above.

---

## 📋 **Verification Checklist**

After deployment, verify these URLs work:

```bash
# Main pages
✅ https://your-app.web.app/index.html
✅ https://your-app.web.app/Bracket_Chess.html
✅ https://your-app.web.app/contact_management.html
✅ https://your-app.web.app/user_management.html
✅ https://your-app.web.app/import_contacts_initial.html

# CSV files (for import tool)
✅ https://your-app.web.app/Chess.csv
✅ https://your-app.web.app/TableTennis_Singles.csv
... (all 8 CSVs)

# Should NOT be accessible
❌ https://your-app.web.app/database.rules.json (404)
❌ https://your-app.web.app/README_FIREBASE.md (404)
❌ https://your-app.web.app/deploy.sh (404)
```

---

## 🎯 **Recommended Deployment Structure**

```
Firebase Hosting (public folder)
├── index.html                          ✅ Main dashboard
├── Bracket_*.html (8 files)            ✅ Tournament brackets
├── contact_management.html             ✅ Admin contact tool
├── user_management.html                ✅ Admin user tool
├── import_contacts_initial.html        ✅ One-time import
└── *.csv (8 files)                     ✅ Registration data

Local Workspace (not deployed)
├── *.md (30+ files)                    📝 Documentation
├── *.py (18 files)                     🐍 Build scripts
├── *.sh (5 files)                      🔧 Dev tools
├── database.rules*.json (3 files)      🔐 DB rules (separate)
├── Fixtures_*.txt (8 files)            📄 Old fixtures
└── Apps_Script_Code.js                 🗃️ Old Google Sheets
```

---

## ✅ **Quick Deploy Command**

```bash
# Update firebase.json with ignore patterns
cat > firebase.json << 'EOF'
{
  "hosting": {
    "public": ".",
    "ignore": [
      "firebase.json",
      "**/.*",
      "**/node_modules/**",
      "**/*.md",
      "**/*.py",
      "**/*.sh",
      "Fixtures_*.txt",
      "Apps_Script_Code.js",
      "database.rules*.json",
      "Insportsathon Responses - Sheet2.csv",
      "tournament_data/**"
    ]
  }
}
EOF

# Deploy
firebase deploy --only hosting
```

---

## 📝 **Summary**

| Category | Deploy? | Count | Size Estimate |
|----------|---------|-------|---------------|
| **HTML Files** | ✅ YES | 12 | ~8 MB |
| **CSV Files** | ✅ YES | 8 | ~500 KB |
| **Documentation** | ❌ NO | 30+ | ~1 MB |
| **Python Scripts** | ❌ NO | 18 | ~200 KB |
| **Shell Scripts** | ❌ NO | 5 | ~20 KB |
| **DB Rules** | ❌ NO (separate deploy) | 3 | ~10 KB |
| **Old Fixtures** | ❌ NO | 8 | ~100 KB |
| **Total Deploy Size** | - | 20 files | **~8.5 MB** |

---

**🚀 Ready to deploy with clean, minimal file set!**

