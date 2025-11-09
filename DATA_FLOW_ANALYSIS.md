# Data Flow Analysis - Tournament Bracket System

## 📊 Complete Data Analysis

### Overview
This document analyzes all data in the tournament bracket system and categorizes it by source and storage location.

---

## 🔵 DATA SOURCES & STORAGE

### 1. **CSV Files** (Original Source)
Location: `/Users/sbhagat/Insports/*.csv`

Files:
- `TableTennis_Singles.csv`
- `TableTennis_Doubles.csv`
- `Carrom_Singles.csv`
- `Carrom_Doubles.csv`
- `Foosball.csv`
- `Snooker.csv`
- `FIFA25.csv`
- `Chess.csv`

**Data Contained:**
- TimeStamp
- Email Address
- Employee Name
- Contact Number
- Volunteering interest
- Employment confirmation
- Partner information (for doubles)

**Purpose:** 
- ✅ Initial data extraction from registration spreadsheet
- ✅ Source for generating bracket HTML files
- ❌ NOT used at runtime by brackets

---

## 📝 DATA IN HTML FILES (Hardcoded)

### Static Data - Embedded in JavaScript

#### 1. **Tournament Configuration**
```javascript
const SPORT_KEY = 'Chess';
const totalRounds = 7;
const bracketSize = 128;
const isDoubles = false;
```

**Status:** 🔴 **HARDCODED**
- Sport name
- Number of rounds
- Bracket size (power of 2)
- Doubles vs Singles flag

**Storage:** HTML file only
**Persisted in Firebase:** ❌ No

---

#### 2. **Initial Player Names & Matches**
```javascript
const initialRoundsData = [
    [
        {"player1": "Hari Prasad", "player2": "Sayantan Banerjee", 
         "winner": null, "score1": "", "score2": "", "time": "", 
         "matchId": 0, "isByeMatch": false},
        // ... more matches
    ],
    // ... more rounds
];
```

**Status:** 🔴 **HARDCODED** (initial state only)
- Round 1 player names
- Initial match pairings
- Empty scores/winners/times

**Source:** Generated from CSV files
**Storage:** HTML file (initial state)
**Persisted in Firebase:** ✅ **YES** (after first edit)

**Flow:**
```
CSV → Python Script → HTML (initialRoundsData) → Firebase (on first save)
```

---

#### 3. **Bye Players**
```javascript
const byePlayers = new Set([
    "Avneesh Dwivedi", 
    "Vikram ghadge", 
    "Piyush Jhanwar",
    // ... more players
]);
```

**Status:** 🔴 **HARDCODED**
- List of players who skip Round 1
- Calculated based on bracket size

**Source:** Generated from CSV files (power of 2 calculation)
**Storage:** HTML file only
**Persisted in Firebase:** ❌ No
**Used for:** Visual indication of bye status

---

#### 4. **Contact Information**
```javascript
const contactInfo = {
    "Shiva Sah": {"email": "shiva_sah@intuit.com", "phone": "9711668419"},
    "Syed Shahabaaz Ahmed": {"email": "syedshahabaaz_ahmed@intuit.com", "phone": "9900815696"},
    // ... all players
};
```

**Status:** 🔴 **HARDCODED**
- Email addresses
- Phone numbers
- Mapped by player name

**Source:** Extracted from CSV files
**Storage:** HTML file only
**Persisted in Firebase:** ❌ **NO**
**Used for:** Hover tooltips on player names

**⚠️ LIMITATION:** Cannot be updated without editing HTML files

---

## 🔥 DATA IN FIREBASE DATABASE

### Real-time Persisted Data

#### 1. **Match Results & Tournament Progress**
Firebase Path: `tournaments/{SPORT_KEY}/`

**Data Structure:**
```javascript
{
  "tournaments": {
    "Chess": [
      [  // Round 1
        {
          "player1": "Hari Prasad",
          "player2": "Sayantan Banerjee",
          "winner": "Hari Prasad",      // ✅ Persisted
          "score1": "10",                 // ✅ Persisted
          "score2": "5",                  // ✅ Persisted
          "time": "2:30 PM",             // ✅ Persisted
          "matchId": 0,
          "isByeMatch": false
        },
        // ... more matches
      ],
      // ... more rounds with TBD/updated players
    ],
    "TableTennis_Singles": [ ... ],
    "FIFA25": [ ... ],
    // ... other sports
  }
}
```

**Status:** ✅ **PERSISTED IN FIREBASE**
**Updated when:**
- Winner selected
- Scores entered
- Match time updated
- Player name edited
- Bracket reset (by admin)

**Sync:** Real-time across all browsers

---

#### 2. **User Authentication & Roles**
Firebase Path: `users/{uid}/`

**Data Structure:**
```javascript
{
  "users": {
    "abc123uid": {
      "email": "admin@example.com",
      "role": "admin",              // ✅ Persisted
      "createdAt": "2025-11-08"
    },
    "def456uid": {
      "email": "editor@example.com",
      "role": "editor",              // ✅ Persisted
      "createdAt": "2025-11-08"
    },
    "ghi789uid": {
      "email": "viewer@example.com",
      "role": "viewer",              // ✅ Persisted
      "createdAt": "2025-11-08"
    }
  }
}
```

**Status:** ✅ **PERSISTED IN FIREBASE**
**Managed via:**
- `setup_admin.html` (first admin)
- `user_management.html` (admin manages users)

**Used for:**
- Permission checks
- UI enable/disable
- Role badges

---

## 📊 DATA FLOW DIAGRAM

```
┌──────────────────────────────────────────────────────────────┐
│                    DATA FLOW OVERVIEW                         │
└──────────────────────────────────────────────────────────────┘

1. INITIAL SETUP (One-time)
   ════════════════════════════════════════════════════════════
   
   CSV Files (Source)
        ↓
   Python Script
        ↓
   Generates HTML with:
        - initialRoundsData (player names, initial matches)
        - byePlayers (calculated byes)
        - contactInfo (email/phone)
        - Configuration (rounds, bracket size)
        ↓
   Bracket_*.html (Hardcoded Data)


2. RUNTIME (Browser)
   ════════════════════════════════════════════════════════════
   
   User Opens Bracket
        ↓
   Load initialRoundsData from HTML
        ↓
   Check Firebase for saved state
        ↓
   ┌─────────────────────────────────────┐
   │ Firebase has data?                  │
   └─────────────────────────────────────┘
           │
     ┌─────┴─────┐
    YES          NO
     │            │
     ↓            ↓
   Load from    Use initialRoundsData
   Firebase     (hardcoded)
     │            │
     └─────┬──────┘
           ↓
   Render Bracket
           ↓
   User Interactions:
   - Select winner → Save to Firebase ✅
   - Update scores → Save to Firebase ✅
   - Edit times → Save to Firebase ✅
   - Edit names → Save to Firebase ✅
   - View contact → Read from contactInfo (HTML) ❌


3. AUTHENTICATION (Runtime)
   ════════════════════════════════════════════════════════════
   
   User Clicks Login
        ↓
   Firebase Authentication
        ↓
   Get User Role from Firebase
        ↓
   Apply Permissions (viewer/editor/admin)
```

---

## 📋 DATA CATEGORIZATION TABLE

| Data Type | Source | Initial Storage | Runtime Storage | Real-time Sync | Can Update Without Code Change |
|-----------|--------|-----------------|-----------------|----------------|--------------------------------|
| **Player Names (Initial)** | CSV | HTML (hardcoded) | Firebase (after edit) | ✅ Yes | ❌ No (need to regenerate HTML) |
| **Player Names (Edited)** | User Input | - | Firebase | ✅ Yes | ✅ Yes (via edit button) |
| **Match Winners** | User Input | - | Firebase | ✅ Yes | ✅ Yes |
| **Match Scores** | User Input | - | Firebase | ✅ Yes | ✅ Yes |
| **Match Times** | User Input | - | Firebase | ✅ Yes | ✅ Yes |
| **Contact Info (Email/Phone)** | CSV | HTML (hardcoded) | HTML only | ❌ No | ❌ No |
| **Bye Players** | CSV (calculated) | HTML (hardcoded) | HTML only | ❌ No | ❌ No |
| **Tournament Config** | Python Script | HTML (hardcoded) | HTML only | ❌ No | ❌ No |
| **User Roles** | Admin Setup | - | Firebase | ✅ Yes | ✅ Yes (via user mgmt) |
| **User Authentication** | Firebase Auth | - | Firebase | ✅ Yes | ✅ Yes |

---

## 🔴 HARDCODED DATA (Cannot Change at Runtime)

### 1. Initial Player List
- **Where:** `initialRoundsData` in HTML
- **Why:** Generated from CSV during bracket creation
- **Limitation:** Adding/removing players requires regenerating HTML

### 2. Contact Information
- **Where:** `contactInfo` object in HTML
- **Why:** Extracted from CSV during bracket creation
- **Limitation:** Email/phone updates require regenerating HTML
- **Impact:** Tooltips show outdated info if players change contact

### 3. Bye Players
- **Where:** `byePlayers` Set in HTML
- **Why:** Calculated based on bracket size
- **Limitation:** Cannot reassign byes without regenerating

### 4. Tournament Structure
- **Where:** `SPORT_KEY`, `totalRounds`, `bracketSize`, `isDoubles`
- **Why:** Defined at bracket creation time
- **Limitation:** Cannot change tournament format after creation

---

## ✅ DYNAMIC DATA (Changes at Runtime)

### 1. Match Results
- **Where:** `allRoundsData` → Firebase
- **When:** User selects winner, updates scores
- **Sync:** Real-time across all browsers

### 2. Match Scores
- **Where:** `allRoundsData` → Firebase
- **When:** User enters scores
- **Sync:** Real-time across all browsers

### 3. Match Times
- **Where:** `allRoundsData` → Firebase
- **When:** User edits time field
- **Sync:** Real-time across all browsers

### 4. Player Names (After Edit)
- **Where:** `allRoundsData` → Firebase
- **When:** User clicks edit button and saves new name
- **Sync:** Real-time across all browsers
- **Note:** Original name in `initialRoundsData` unchanged

### 5. User Roles & Permissions
- **Where:** Firebase `users/{uid}/role`
- **When:** Admin manages users
- **Sync:** Immediately upon login

---

## 🎯 RECOMMENDATIONS

### Issue 1: Contact Info Not Dynamic
**Problem:** Email/phone hardcoded in HTML, can't update

**Solutions:**

#### Option A: Store in Firebase (Recommended)
```javascript
// Store contact info in Firebase
firebase.database().ref(`contacts/${SPORT_KEY}`).set(contactInfo);

// Load from Firebase
firebase.database().ref(`contacts/${SPORT_KEY}`).on('value', (snapshot) => {
    contactInfo = snapshot.val();
});
```

**Pros:**
- ✅ Can update contact info without code changes
- ✅ Admin can manage via UI
- ✅ Syncs across browsers

**Cons:**
- ❌ Requires additional UI for contact management
- ❌ Initial setup needed

---

#### Option B: Reference Original CSV
```javascript
// Store CSV data in Firebase on first load
if (!csvDataInFirebase) {
    // Upload contact info from initialContactInfo
    firebase.database().ref(`csvData/${SPORT_KEY}`).set({
        contacts: contactInfo,
        registrationData: { /* full CSV data */ }
    });
}
```

**Pros:**
- ✅ Preserves original registration data
- ✅ Can update if needed

---

### Issue 2: Initial Player List Hardcoded
**Problem:** Adding/removing players requires regenerating HTML

**Solutions:**

#### Option A: Dynamic Bracket Creation UI
Create admin interface to:
1. Upload CSV
2. Generate bracket in Firebase
3. HTML reads from Firebase

#### Option B: Keep Current Approach
- Acceptable if player list is final at creation time
- Regenerate HTML only if player list changes significantly

---

## 🔍 SUMMARY

### What's in CSV Files:
- ✅ Player names
- ✅ Email addresses
- ✅ Phone numbers
- ✅ Registration metadata
- **Usage:** One-time extraction to generate HTML

### What's Hardcoded in HTML:
- 🔴 Initial player names and pairings
- 🔴 Contact information (email/phone)
- 🔴 Bye players list
- 🔴 Tournament configuration
- **Limitation:** Cannot change without regenerating file

### What's in Firebase Database:
- ✅ Match results (winners)
- ✅ Match scores
- ✅ Match times
- ✅ Edited player names
- ✅ User roles and authentication
- **Advantage:** Real-time sync, editable at runtime

---

## 📈 DATA PERSISTENCE OVERVIEW

```
┌────────────────────────────────────────────────────────────┐
│                    DATA PERSISTENCE                         │
├────────────────────────────────────────────────────────────┤
│                                                             │
│  CSV Files (Source)                                        │
│  ├── Read Once → Generate HTML                            │
│  └── Not Used at Runtime                                  │
│                                                             │
│  HTML Files (Hybrid)                                       │
│  ├── Static Data (hardcoded)                              │
│  │   ├── Initial player list                              │
│  │   ├── Contact info                                     │
│  │   ├── Bye players                                      │
│  │   └── Config                                           │
│  └── Initial State Only                                   │
│      └── Overridden by Firebase if data exists           │
│                                                             │
│  Firebase Database (Dynamic)                               │
│  ├── Tournament Progress                                  │
│  │   ├── Match results     ✅ Real-time                  │
│  │   ├── Scores            ✅ Real-time                  │
│  │   ├── Times             ✅ Real-time                  │
│  │   └── Edited names      ✅ Real-time                  │
│  └── User Management                                      │
│      ├── Roles             ✅ Real-time                  │
│      └── Authentication    ✅ Real-time                  │
│                                                             │
└────────────────────────────────────────────────────────────┘
```

---

**Status:** Complete analysis
**Last Updated:** Current session
**Recommendation:** Consider moving contact info to Firebase for better maintainability

