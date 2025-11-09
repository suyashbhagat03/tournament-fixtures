# 🔒 Fix 403 Forbidden Error

## ❌ Problem:
Your Apps Script is redirecting to Google sign-in page and returning 403 Forbidden.

## 🔍 Root Cause:
The web app deployment is requiring authentication instead of allowing anonymous access.

---

## ✅ SOLUTION: Fix Deployment Settings (5 minutes)

### STEP 1: Open Apps Script
1. Open Google Sheet: **"Insportsathon_Tournament_Data"**
2. Click **Extensions → Apps Script**

### STEP 2: Delete Old Deployment & Create New One

**Option A: Clean Slate (Recommended)**

1. Click **Deploy → Manage deployments**
2. Click the **trash icon** 🗑️ to delete the old deployment
3. Click **Deploy → New deployment**
4. Click the **gear icon** ⚙️ next to "Select type"
5. Choose **"Web app"**

6. **CRITICAL SETTINGS:**
   ```
   Description: Tournament Bracket API v3
   
   Execute as: Me (YOUR_EMAIL@intuit.com)
   
   Who has access: Anyone  ⚠️ MUST BE "Anyone"
   ```

7. Click **Deploy**

8. **IMPORTANT:** Click **Authorize access**
   - Choose your Google account
   - Click **Advanced**
   - Click **"Go to Tournament Bracket API (unsafe)"**
   - Click **Allow**

9. **Copy the NEW Web App URL**
   - Format: `https://script.google.com/macros/s/XXXXX/exec`

10. **Update ALL 8 HTML files** with the new URL (I'll help with this)

---

### STEP 3: Verify Deployment Settings

After deploying, check:

1. Click **Deploy → Manage deployments**
2. You should see:
   ```
   Type: Web app
   Version: 1 (or higher)
   Execute as: YOUR_EMAIL
   Access: Anyone ✅
   ```

3. **Test the URL directly in browser:**
   - Copy your Web App URL
   - Add `?sport=Chess` to the end
   - Open in browser: `https://script.google.com/.../exec?sport=Chess`
   - **Expected result:** `[]` (empty JSON array)
   - **NOT expected:** Google sign-in page ❌

---

## 🎯 Common Mistakes

### ❌ Wrong: "Who has access" = "Only myself"
This requires authentication and causes 403 error.

### ✅ Correct: "Who has access" = "Anyone"
This allows anonymous access from your HTML files.

### ❌ Wrong: "Execute as" = "User accessing the web app"
This won't work for anonymous users.

### ✅ Correct: "Execute as" = "Me"
This runs the script with your permissions.

---

## 🔐 Security Note

**"Anyone" access is safe for your use case because:**
- ✅ The script only reads/writes to YOUR Google Sheet
- ✅ Only YOU can edit the script
- ✅ The URL is not publicly listed anywhere
- ✅ Data is only accessible to people who have the URL
- ✅ Your Google account credentials are NOT exposed

For a private internal event, this is perfectly fine!

---

## 🧪 Testing Steps

### Test 1: Direct URL Access
```
https://YOUR_WEB_APP_URL/exec?sport=Chess
```
**Expected:** `[]` or JSON data (NOT a sign-in page)

### Test 2: Browser Console
1. Open any bracket HTML file
2. Press **F12** (open Developer Tools)
3. Go to **Console** tab
4. Look for errors:
   - ✅ Good: "✅ Synced with Google Sheets"
   - ❌ Bad: "403 Forbidden" or redirect errors

### Test 3: Network Tab
1. Open bracket HTML file
2. Press **F12**
3. Go to **Network** tab
4. Refresh page
5. Look for request to your Apps Script URL
6. Click on it → Check "Response" tab
   - ✅ Good: JSON data
   - ❌ Bad: HTML sign-in page

---

## 🚨 Still Getting 403?

### Check 1: Deployment Authorization
- Make sure you clicked **"Allow"** during deployment
- Try deploying again and watch for authorization popup

### Check 2: Account Mismatch
- Deploy using the SAME Google account that owns the sheet
- If using work account (@intuit.com), make sure you're signed in

### Check 3: Script Permissions
1. In Apps Script, click **Run** → Select `doGet` function
2. Click **Run**
3. If asked, **Review permissions** → **Allow**

### Check 4: Incognito Test
- Open bracket in incognito/private window
- If it works there, clear your browser cache
- If it still fails, the deployment settings are wrong

---

## 💡 Alternative: Test Without Deployment

If you keep having issues, test the script directly:

1. In Apps Script editor, select `doGet` function
2. Click **Run**
3. Check **Execution log** for output
4. If this works but web app doesn't = deployment issue

---

## 📝 Checklist

Before testing, verify:

- [ ] Apps Script code has CORS headers (from previous fix)
- [ ] Deployment created/updated
- [ ] "Execute as" = "Me"
- [ ] "Who has access" = "Anyone" ⚠️ CRITICAL
- [ ] Authorized access during deployment
- [ ] Copied the correct Web App URL
- [ ] Updated all 8 HTML files with URL
- [ ] Tested URL directly in browser (should show `[]`)
- [ ] No redirect to accounts.google.com

---

## 🎉 Success Indicators

You'll know it's working when:

1. ✅ Direct URL test shows `[]` (not sign-in page)
2. ✅ Bracket shows "✅ Synced with Google Sheets"
3. ✅ No 403 errors in browser console
4. ✅ Entering scores updates Google Sheet
5. ✅ No authentication prompts

---

**After fixing deployment, let me know and I'll help update the HTML files with the new URL!**

