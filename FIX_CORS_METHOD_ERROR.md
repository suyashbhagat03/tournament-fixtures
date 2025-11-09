# Fix: METHOD Not Allowed (CORS Preflight)

## 🔧 The Problem
"METHOD not allowed" happens because the browser sends an OPTIONS request (CORS preflight) before POST, but your Apps Script doesn't handle it.

## ✅ The Fix (2 Minutes)

### Step 1: Update Apps Script Code
1. Go to your Google Sheet with the Apps Script
2. Click **Extensions** → **Apps Script**
3. **Replace ALL code** with the updated code from `Apps_Script_Code.js` (which now includes `doOptions` function)
4. Click **Save** (💾 icon)

### Step 2: Redeploy
1. Click **Deploy** → **Manage deployments**
2. Click the **Edit** (pencil) icon next to your active deployment
3. Under **Version**, change to **New version**
4. Click **Deploy**
5. ✅ Done!

**Important:** You don't need a new URL - the same URL will work after redeploying!

---

## 📝 What Changed?

Added this function to handle CORS preflight:

```javascript
function doOptions(e) {
  return ContentService.createTextOutput('')
    .setMimeType(ContentService.MimeType.JSON);
}
```

This tells the browser "yes, you can make POST requests to this endpoint."

---

## ⚠️ Don't Forget!

After updating the code, you **MUST redeploy** for changes to take effect. Just saving isn't enough!

---

## 🧪 Test It

After redeploying:
1. Open any bracket (e.g., `Bracket_Chess.html`)
2. Make a change (enter a score)
3. Check the status indicator - it should say "☁️ Synced ✅"

If you still see errors, check the browser console (F12 → Console tab).

