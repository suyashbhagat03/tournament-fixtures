// Google Apps Script Code for Google Sheets
// Copy and paste this into Extensions → Apps Script in your Google Sheet

// Handle CORS preflight OPTIONS request
function doOptions(e) {
  return ContentService.createTextOutput('')
    .setMimeType(ContentService.MimeType.JSON);
}

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
