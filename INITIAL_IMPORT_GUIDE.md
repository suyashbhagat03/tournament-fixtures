# Initial Contact Import - Quick Start

## 🚀 One-Time Setup Required

Since we removed all hardcoded contact data from HTML files for security, you need to do a **one-time import** from CSV files to Firebase.

---

## 📋 Steps to Import

### 1. **Open Import Tool**
```bash
open import_contacts_initial.html
```

### 2. **Login as Admin**
- You must be logged in with admin credentials
- If not logged in, you'll be redirected to `setup_admin.html`

### 3. **Click "Start Import"**
- The tool will read all 8 CSV files
- Extract email and phone for each player
- Upload to Firebase under `contacts/{SPORT_KEY}`

### 4. **Wait for Completion**
- Progress bar shows import status
- Log shows details for each sport
- Success message confirms completion

---

## 📊 What Gets Imported

From each CSV file:
- **Player Name** → Used as key
- **Email Address** → Contact info
- **Phone Number** → Contact info
- **Partner Info** (for doubles sports) → Team contact

Uploaded to Firebase:
```
firebase-database/
└── contacts/
    ├── TableTennis_Singles/
    │   ├── "Player 1": {email: "...", phone: "..."}
    │   └── ...
    ├── TableTennis_Doubles/
    │   ├── "Team Name": {player1, email1, phone1, player2, email2, phone2}
    │   └── ...
    └── ... (all 8 sports)
```

---

## ✅ After Import

1. **Contacts are in Firebase** - Secure, not in HTML
2. **Brackets can load contacts** - Via async Firebase call
3. **Admin can manage** - Via `contact_management.html`
4. **Tooltips work** - Showing data from Firebase

---

## 🔄 Re-run if Needed

You can re-run the import anytime to:
- Refresh contacts from updated CSV files
- Overwrite existing Firebase data
- Add missing sports

**Note:** This will overwrite any manual edits made via `contact_management.html`

---

## 🎯 Quick Command

```bash
# Open import tool
open import_contacts_initial.html

# After import, verify:
open contact_management.html
# Select a sport and check contacts are loaded
```

---

**Status:** Ready to run
**Required:** Admin login
**Duration:** ~30 seconds for all 8 sports

