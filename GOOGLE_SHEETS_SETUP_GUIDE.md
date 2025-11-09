# 📊 Google Sheets Sync Setup Guide

## ⏱️ Total Time: 25-30 minutes (one-time setup)

---

## STEP 1: Create Google Sheet (5 minutes)

### 1.1 Create New Sheet
1. Go to https://sheets.google.com
2. Click **"+ Blank"** to create new spreadsheet
3. Rename to: **"Insportsathon_Tournament_Data"**

### 1.2 Create Tabs for Each Sport
Create these 8 tabs:
- Chess
- TableTennis_Singles
- TableTennis_Doubles
- Foosball
- Carrom_Singles
- Carrom_Doubles
- Snooker
- FIFA25

### 1.3 Add Headers
In **Row 1** of EACH tab, add these columns:
```
RoundID | MatchID | Player1 | Player2 | Score1 | Score2 | Winner | Time
```

**✅ CHECKPOINT:** Sheet has 8 tabs, all with headers

---

## STEP 2: Create Apps Script Web App (10 minutes)

### 2.1 Open Apps Script
1. In your Google Sheet, click: **Extensions → Apps Script**
2. Delete any default code

### 2.2 Paste This Code
Copy and paste the complete code below:

```javascript
function doGet(e) {
  const sport = e.parameter.sport;
  const sheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName(sport);
  
  if (!sheet) {
    return ContentService.createTextOutput(JSON.stringify({error: 'Sheet not found'}))
      .setMimeType(ContentService.MimeType.JSON);
  }
  
  const data = sheet.getDataRange().getValues();
  const headers = data[0];
  const rows = data.slice(1);
  
  // Convert to array of objects
  const result = rows.map(row => {
    const obj = {};
    headers.forEach((header, index) => {
      obj[header] = row[index];
    });
    return obj;
  });
  
  return ContentService.createTextOutput(JSON.stringify(result))
    .setMimeType(ContentService.MimeType.JSON);
}

function doPost(e) {
  try {
    const data = JSON.parse(e.postData.contents);
    const sport = data.sport;
    const rounds = data.rounds;
    
    const sheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName(sport);
    
    if (!sheet) {
      return ContentService.createTextOutput(JSON.stringify({error: 'Sheet not found'}))
        .setMimeType(ContentService.MimeType.JSON);
    }
    
    // Clear existing data (except headers)
    const lastRow = sheet.getLastRow();
    if (lastRow > 1) {
      sheet.deleteRows(2, lastRow - 1);
    }
    
    // Convert rounds data to rows
    const rows = [];
    rounds.forEach((round, roundIdx) => {
      if (round && Array.isArray(round)) {
        round.forEach((match, matchIdx) => {
          rows.push([
            roundIdx,
            matchIdx,
            match.player1 || '',
            match.player2 || '',
            match.score1 || '',
            match.score2 || '',
            match.winner || '',
            match.time || ''
          ]);
        });
      }
    });
    
    // Append new data
    if (rows.length > 0) {
      sheet.getRange(2, 1, rows.length, 8).setValues(rows);
    }
    
    return ContentService.createTextOutput(JSON.stringify({status: 'success', rows: rows.length}))
      .setMimeType(ContentService.MimeType.JSON);
      
  } catch (error) {
    return ContentService.createTextOutput(JSON.stringify({error: error.toString()}))
      .setMimeType(ContentService.MimeType.JSON);
  }
}
```

### 2.3 Save the Project
1. Click **Save** icon (💾)
2. Name: **"Tournament Sync API"**

### 2.4 Deploy as Web App
1. Click **Deploy → New deployment**
2. Click **gear icon** (⚙️) → Select **"Web app"**
3. Configure:
   - **Description:** "Tournament Bracket API v1"
   - **Execute as:** "Me (your email)"
   - **Who has access:** "Anyone"
4. Click **"Deploy"**

### 2.5 Authorize Access
1. Click **"Authorize access"**
2. Choose your Google account
3. Click **"Advanced"** → **"Go to Tournament Sync API (unsafe)"**
4. Click **"Allow"**

### 2.6 Copy Web App URL
You'll see a URL like:
```
https://script.google.com/macros/s/AKfycbXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/exec
```

**⚠️ IMPORTANT: COPY THIS URL!** You'll need it in the next step.

### 2.7 Test the API
1. Open new browser tab
2. Paste: `YOUR_WEB_APP_URL?sport=Chess`
3. You should see: `[]` (empty array)
4. If you see this, it's working! ✅

**✅ CHECKPOINT:** Web app deployed and responding

---

## STEP 3: Update HTML Files (I'll do this automatically)

I will update all 8 bracket HTML files with:
- Google Sheets sync code
- Your web app URL
- Auto-save functionality
- Auto-load on page load
- Polling for updates every 5 seconds

**You just need to provide the Web App URL from Step 2.6**

---

## STEP 4: Test the Setup (5 minutes)

### 4.1 Test Single Browser
1. Open any bracket (e.g., `Bracket_Chess.html`)
2. Enter a score for any match
3. Open Google Sheet
4. Check "Chess" tab → Data should appear! ✅

### 4.2 Test Multi-Browser Sync
1. Open `Bracket_Chess.html` in Browser 1
2. Open `Bracket_Chess.html` in Browser 2
3. In Browser 1: Enter a score
4. Watch Browser 2: Should update within 5 seconds ✅

### 4.3 Test Refresh Persistence
1. In Browser 1: Enter several scores
2. Refresh the page (F5)
3. All data should still be there ✅

### 4.4 Test Manual Edit
1. Open Google Sheet
2. Manually change a score in "Chess" tab
3. Watch browsers: Should update within 5 seconds ✅

**✅ CHECKPOINT:** All tests passing!

---

## 📊 What You'll See in Google Sheets

After entering tournament data, your "Chess" tab will look like:

| RoundID | MatchID | Player1    | Player2     | Score1 | Score2 | Winner     | Time    |
|---------|---------|------------|-------------|--------|--------|------------|---------|
| 0       | 0       | John Doe   | Jane Smith  | 21     | 15     | John Doe   | 2:00 PM |
| 0       | 1       | Mike Lee   | Sara Khan   | 18     | 21     | Sara Khan  | 2:15 PM |
| 1       | 0       | John Doe   | Sara Khan   | 19     | 21     | Sara Khan  | 3:00 PM |
| 2       | 0       | Sara Khan  | TBD         |        |        |            |         |

---

## 🎯 How It Works

1. **Page Load:** Bracket loads data from Google Sheet
2. **Score Entry:** Data saves to Google Sheet (1-2 seconds)
3. **Auto-Sync:** All browsers poll every 5 seconds for updates
4. **Refresh:** Data persists (loaded from sheet)
5. **Manual Edit:** Changes in sheet sync to all browsers

---

## 🚨 Troubleshooting

### "Sheet not found" error
- Check tab names match exactly (case-sensitive)
- Verify all 8 tabs exist

### Data not syncing
- Check browser console for errors (F12)
- Verify Web App URL is correct
- Ensure Apps Script is deployed as "Anyone" access

### Slow updates
- Normal! Google Sheets syncs in 3-7 seconds
- If too slow, consider Firebase instead

---

## ✅ Benefits You Get

- ✅ Auto-sync across all machines
- ✅ Survives browser refresh
- ✅ Manual editing in spreadsheet
- ✅ 30-day version history
- ✅ Export to Excel/PDF anytime
- ✅ View/edit from mobile (Sheets app)
- ✅ Built-in backup
- ✅ Free forever

---

## 🎉 You're Done!

Your tournament brackets now sync automatically via Google Sheets!

