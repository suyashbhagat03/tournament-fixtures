# Google Sheets Error - Quick Fix Options

## ❌ The Error You're Seeing

"Sorry, unable to open the file at present" means:
- The Google Sheet doesn't exist yet
- Or permissions aren't set correctly
- Or the Apps Script URL is wrong

---

## ✅ OPTION 1: Use Browser Storage (FASTEST - No Setup!)

I can create a version that uses your browser's storage instead of Google Sheets.

**Pros:**
- ✅ Works immediately, no setup
- ✅ Data persists in browser
- ✅ Each browser/computer has its own data
- ✅ No Google account needed
- ✅ Zero configuration

**Cons:**
- ⚠️ Data is per-browser (not synced across machines)
- ⚠️ Clearing browser data = losing tournament data

**Best for:** Single machine, quick setup, testing

---

## ✅ OPTION 2: Fix Google Sheets (Synced Across Machines)

**Pros:**
- ✅ Syncs across all machines
- ✅ Multiple people can update
- ✅ Data backed up in Google
- ✅ Can view data in spreadsheet

**Cons:**
- ⚠️ Requires setup (10-15 minutes)
- ⚠️ Needs Google account
- ⚠️ More complex

**Setup Steps:**

### Step 1: Create Google Sheet
1. Go to https://sheets.google.com
2. Create new spreadsheet
3. Name it: "Insportsathon Tournaments"

### Step 2: Create Sheets for Each Sport
Create 8 sheets (tabs) with these EXACT names:
- `TableTennis_Singles`
- `TableTennis_Doubles`
- `Foosball`
- `Carrom_Singles`
- `Carrom_Doubles`
- `Snooker`
- `FIFA25`
- `Chess`

### Step 3: Add Headers to EACH Sheet
In row 1 of each sheet, add these columns:
```
RoundID | MatchID | Player1 | Player2 | Score1 | Score2 | Winner | Time
```

### Step 4: Add Apps Script
1. In the Google Sheet, click **Extensions** → **Apps Script**
2. Delete any existing code
3. Copy the code from `Apps_Script_Code.js`
4. Click **Save** (disk icon)

### Step 5: Deploy
1. Click **Deploy** → **New deployment**
2. Click gear icon ⚙️ → **Web app**
3. Description: "Tournament API"
4. **Execute as:** Me
5. **Who has access:** **Anyone** ← VERY IMPORTANT!
6. Click **Deploy**
7. **Copy the Web App URL** (looks like: `https://script.google.com/macros/s/...`)

### Step 6: Update Bracket Files
Replace the URL in all bracket HTML files with your new URL.

---

## 🤔 Which Should You Choose?

### Choose Browser Storage if:
- ✅ Using only 1 computer
- ✅ Want it working NOW
- ✅ Don't need cloud sync
- ✅ Just testing/trying it out

### Choose Google Sheets if:
- ✅ Multiple computers/people
- ✅ Need cloud backup
- ✅ Want to see data in spreadsheet
- ✅ Don't mind 15min setup

---

## 🚀 Tell me which option you want and I'll implement it!

