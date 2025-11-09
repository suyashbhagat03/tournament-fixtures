# 🔧 Google Sheets - Final Fix (Step-by-Step)

## ✅ Current Status:
- ✅ Apps Script code is correct (no `.setHeader()` errors)
- ✅ All 8 HTML files have correct URL
- ⏳ Need to deploy Apps Script correctly

---

## 🎯 THE ONLY THING THAT MATTERS:

**"Who has access" MUST be set to "Anyone"**

This is the #1 reason for 403 and CORS errors!

---

## 📋 FOOLPROOF DEPLOYMENT STEPS

### STEP 1: Open Apps Script (1 min)

1. Open Google Sheet: **"Insportsathon_Tournament_Data"**
2. Click **Extensions → Apps Script**
3. You should see the code with `doGet` and `doPost` functions

### STEP 2: Verify Code (1 min)

Make sure your code looks like this (NO `.setHeader()` calls):

```javascript
function doGet(e) {
  const sport = e.parameter.sport;
  const sheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName(sport);
  
  if (!sheet) {
    return ContentService.createTextOutput(JSON.stringify({error: 'Sheet not found'}))
      .setMimeType(ContentService.MimeType.JSON);
  }
  
  // ... rest of code ...
  
  return ContentService.createTextOutput(JSON.stringify(result))
    .setMimeType(ContentService.MimeType.JSON);
}
```

**✅ Good:** Only `.setMimeType()` - NO `.setHeader()`  
**❌ Bad:** Any `.setHeader()` calls

If you see `.setHeader()`, copy the clean code from `Apps_Script_Code.js`

### STEP 3: Save (30 sec)

Click the **Save** icon (💾) or **Ctrl+S** / **Cmd+S**

### STEP 4: Delete Old Deployment (1 min)

1. Click **Deploy → Manage deployments**
2. If you see ANY existing deployments:
   - Click the **trash icon** 🗑️ next to each one
   - Click **Delete** to confirm
3. You should now see "No deployments"

### STEP 5: Create New Deployment (3 min)

1. Click **Deploy → New deployment**

2. Click the **gear icon** ⚙️ next to "Select type"

3. Choose **"Web app"**

4. Fill in these EXACT settings:

   ```
   Description: Tournament Bracket Sync
   
   Web app:
   Execute as: Me (your-email@intuit.com)
   
   Who has access: Anyone    ⚠️⚠️⚠️ CRITICAL - MUST BE "Anyone"
   ```

   **SCREENSHOT THE SETTINGS if unsure!**

5. Click **Deploy**

### STEP 6: Authorize (2 min)

1. A popup will appear asking to **"Authorize access"**

2. Click **"Authorize access"**

3. Choose your Google/Intuit account

4. You'll see a warning: **"This app isn't verified"**
   - Click **"Advanced"**
   - Click **"Go to Tournament Bracket Sync (unsafe)"**
   - This is YOUR script, it's safe!

5. Review permissions:
   - "See, edit, create, and delete your spreadsheets"
   - Click **"Allow"**

6. You'll see: **"Deployment successfully created"**

7. **COPY THE WEB APP URL** - it should be:
   ```
   https://script.google.com/macros/s/AKfycbw2KqLi9-yE8MDvzZ2Eim0OgX1nFnCPhL-kJstt5Q5AUZjIVvbJT80mcTiZ3YOri4Lw/exec
   ```

8. Click **Done**

### STEP 7: VERIFY DEPLOYMENT (1 min) ⚠️ CRITICAL

1. Click **Deploy → Manage deployments**

2. You should see:
   ```
   Active Deployments
   
   Web app
   Description: Tournament Bracket Sync
   Deployment ID: AKfycbw2KqLi9...
   Version: 1
   Execute as: your-email@intuit.com
   Access: Anyone    ✅✅✅ MUST SAY "Anyone"
   ```

3. **If "Access" says anything OTHER than "Anyone", you have the wrong setting!**
   - Click the pencil icon ✏️
   - Change "Who has access" to "Anyone"
   - Click "Deploy"

---

## 🧪 CRITICAL TESTS (Do Not Skip!)

### TEST 1: Direct URL Test (2 min)

Open this EXACT URL in a new browser tab:

```
https://script.google.com/macros/s/AKfycbw2KqLi9-yE8MDvzZ2Eim0OgX1nFnCPhL-kJstt5Q5AUZjIVvbJT80mcTiZ3YOri4Lw/exec?sport=Chess
```

**✅ CORRECT Result:**
```json
[]
```
(Empty JSON array)

**❌ WRONG Results - What They Mean:**

**Sees Google sign-in page:**
→ "Who has access" is NOT set to "Anyone"
→ Go back to Step 7, verify deployment settings

**Sees error page with "TypeError: setHeader is not a function":**
→ Old code is still deployed
→ Go back to Step 2, verify code has NO `.setHeader()`
→ Then redeploy (Steps 4-6)

**Sees "403 Forbidden" or "Access Denied":**
→ Authorization issue
→ Go back to Step 6, make sure you clicked "Allow"

**Sees "Script function not found: doGet":**
→ Code wasn't saved properly
→ Go back to Step 3, save and redeploy

### TEST 2: Test All Sports (2 min)

Try each sport tab:

```
.../exec?sport=Chess                → Should return []
.../exec?sport=TableTennis_Singles  → Should return []
.../exec?sport=TableTennis_Doubles  → Should return []
.../exec?sport=Foosball             → Should return []
.../exec?sport=Carrom_Singles       → Should return []
.../exec?sport=Carrom_Doubles       → Should return []
.../exec?sport=Snooker              → Should return []
.../exec?sport=FIFA25               → Should return []
```

If you see `{"error":"Sheet not found"}`, the tab name doesn't match.

### TEST 3: Test HTML Bracket (3 min)

1. Open `Bracket_Chess.html` in your browser

2. Check the sync status (below the title):
   - ✅ **Good:** "✅ Synced with Google Sheets" or "📊 Ready (no data yet)"
   - ❌ **Bad:** "❌ Sync error" or "⚠️ Google Sheets not configured"

3. Open browser console (**F12** → Console tab)
   - ✅ **Good:** No red errors
   - ❌ **Bad:** CORS error or 403 error → deployment issue

4. Enter a test score in any match

5. Check your Google Sheet:
   - Open "Chess" tab
   - You should see data appear in rows 2+
   - RoundID, MatchID, Player1, Player2, Score1, Score2, Winner, Time

6. Open `Bracket_Chess.html` in a SECOND browser or tab:
   - Should show the same data
   - Make a change in one browser
   - Should appear in the other within 5 seconds

---

## 🚨 Troubleshooting Guide

### Issue: "setHeader is not a function"

**Cause:** Old code with `.setHeader()` is still deployed

**Fix:**
1. Open Apps Script
2. Copy clean code from `Apps_Script_Code.js`
3. Paste (replace all code)
4. Save
5. Delete old deployment (Step 4)
6. Create new deployment (Step 5-6)

---

### Issue: 403 Forbidden or Sign-In Page

**Cause:** "Who has access" is NOT set to "Anyone"

**Fix:**
1. In Apps Script: Deploy → Manage deployments
2. Check "Access" column
3. If it doesn't say "Anyone":
   - Click pencil icon ✏️
   - Change to "Anyone"
   - Deploy
4. Test URL again

---

### Issue: "Sheet not found" Error

**Cause:** Tab names don't match exactly

**Fix:**
1. Open your Google Sheet
2. Check tab names are EXACTLY:
   - Chess (not "chess" or "CHESS")
   - TableTennis_Singles (with underscore)
   - TableTennis_Doubles (with underscore)
   - Foosball
   - Carrom_Singles (with underscore)
   - Carrom_Doubles (with underscore)
   - Snooker
   - FIFA25 (not "FIFA 25" with space)

---

### Issue: CORS Error in Browser Console

**Cause:** Deployment not set to "Anyone" access

**Fix:**
Same as 403 error - verify "Anyone" access

---

### Issue: Brackets Show "⚠️ Google Sheets not configured"

**Cause:** URL not updated in HTML files (but we already did this!)

**Fix:**
Verify HTML files have correct URL:
```javascript
const SHEET_URL = 'https://script.google.com/macros/s/AKfycbw2KqLi9-yE8MDvzZ2Eim0OgX1nFnCPhL-kJstt5Q5AUZjIVvbJT80mcTiZ3YOri4Lw/exec';
```

---

## ✅ Success Checklist

After completing all steps, you should have:

- [ ] Apps Script code has NO `.setHeader()` calls
- [ ] Deployment shows "Access: Anyone"
- [ ] Direct URL test returns `[]`
- [ ] All 8 sport URLs return `[]`
- [ ] Bracket opens without errors
- [ ] Sync status shows green/success message
- [ ] Entering score updates Google Sheet
- [ ] Data syncs between browsers

---

## 🎉 Once It Works:

You'll have:
- ✅ Auto-sync across all machines
- ✅ Data persists on refresh
- ✅ Manual editing in Google Sheet
- ✅ 5-second sync delay (acceptable for tournament)
- ✅ Version history
- ✅ Mobile access via Sheets app

---

## 📞 Still Stuck?

If after following ALL steps you still have issues:

1. Take a screenshot of:
   - Apps Script deployment settings (Deploy → Manage deployments)
   - The error you're seeing in browser console (F12)
   - The test URL result

2. Share those and I'll help debug!

---

**Follow steps 1-7, then run ALL three tests. Let me know the results!** 🚀

