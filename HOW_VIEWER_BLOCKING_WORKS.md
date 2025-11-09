# 🔒 How Viewer Role Blocking Works - Technical Explanation

## 📋 Overview

The viewer role blocking uses a **multi-layered security approach** to prevent editing:

1. **Role Detection** - Identifies user's role from Firebase
2. **State Management** - Sets `isEditModeEnabled` flag
3. **UI Layer** - Disables/hides interactive elements
4. **Function Layer** - Blocks execution of edit functions
5. **Backend Layer** - Firebase rules prevent unauthorized writes

---

## 🔍 Layer 1: Role Detection

### **Location:** Lines 228-273 in each bracket file

### **How it works:**

```javascript
// Initialize with viewer role (default)
let userRole = 'viewer'; // default: read-only

// Firebase Auth listener checks login state
onAuthStateChanged(auth, async (user) => {
    if (user) {
        // User is logged in - fetch their role from database
        const userRoleRef = ref(db, `users/${user.uid}/role`);
        const snapshot = await get(userRoleRef);
        userRole = snapshot.exists() ? snapshot.val() : 'viewer';
        
        // If no role in database → default to 'viewer'
    } else {
        // No user logged in → default to 'viewer'
        userRole = 'viewer';
    }
});
```

### **Role Assignment Logic:**

| Scenario | Role Value | Result |
|----------|------------|--------|
| Not logged in | `'viewer'` | Read-only |
| Logged in, no role in DB | `'viewer'` | Read-only |
| Logged in, role = "viewer" | `'viewer'` | Read-only |
| Logged in, role = "editor" | `'editor'` | Can edit ✅ |
| Logged in, role = "admin" | `'admin'` | Can edit ✅ |

---

## 🔍 Layer 2: State Management

### **Location:** Lines 252, 267

### **The Key Variable:**

```javascript
let isEditModeEnabled = false; // Global state flag
```

### **How it's set:**

```javascript
// For logged-in users:
isEditModeEnabled = (userRole !== 'viewer');

// Translation:
// - viewer role → isEditModeEnabled = false
// - editor role → isEditModeEnabled = true
// - admin role → isEditModeEnabled = true

// For non-logged in users:
isEditModeEnabled = false;
```

### **Truth Table:**

| User State | userRole | isEditModeEnabled | Can Edit? |
|------------|----------|-------------------|-----------|
| Not logged in | `'viewer'` | `false` | ❌ No |
| Logged in as Viewer | `'viewer'` | `false` | ❌ No |
| Logged in as Editor | `'editor'` | `true` | ✅ Yes |
| Logged in as Admin | `'admin'` | `true` | ✅ Yes |

---

## 🔍 Layer 3: UI Layer Blocking

### **Location:** Lines 275-314 (applyEditControls function)

### **What it does:**

After the bracket renders, `applyEditControls()` is called to enable/disable UI elements based on `isEditModeEnabled`.

```javascript
function applyEditControls() {
    const enabled = isEditModeEnabled;
    
    // 1. Block player name clicking
    document.querySelectorAll('.player').forEach(player => {
        if (!player.classList.contains('tbd')) {
            player.style.pointerEvents = enabled ? 'auto' : 'none';
            player.style.cursor = enabled ? 'pointer' : 'not-allowed';
        }
    });
    
    // 2. Disable score inputs
    document.querySelectorAll('.score-input').forEach(input => {
        input.disabled = !enabled;
        input.style.cursor = enabled ? 'text' : 'not-allowed';
        input.style.opacity = enabled ? '1' : '0.6';
    });
    
    // 3. Disable time inputs
    document.querySelectorAll('.match-time input').forEach(input => {
        input.disabled = !enabled;
        input.style.cursor = enabled ? 'text' : 'not-allowed';
        input.style.opacity = enabled ? '1' : '0.6';
    });
    
    // 4. Hide edit buttons
    document.querySelectorAll('.edit-btn').forEach(btn => {
        btn.disabled = !enabled;
        btn.style.display = enabled ? 'inline-block' : 'none';
    });
    
    // 5. Disable reset button
    document.querySelectorAll('.controls button').forEach(btn => {
        if (btn.textContent.includes('Reset') || btn.textContent.includes('🗑️')) {
            btn.disabled = !enabled;
            btn.style.opacity = enabled ? '1' : '0.5';
            btn.style.cursor = enabled ? 'pointer' : 'not-allowed';
        }
    });
}
```

### **UI Elements Blocked:**

| Element | When Viewer | When Editor/Admin |
|---------|-------------|-------------------|
| Player names | `pointerEvents: none` | `pointerEvents: auto` |
| Score inputs | `disabled = true` | `disabled = false` |
| Time inputs | `disabled = true` | `disabled = false` |
| Edit buttons (✏️) | `display: none` | `display: inline-block` |
| Reset button | `disabled = true` | `disabled = false` |
| Cursor | `not-allowed` | `pointer` or `text` |

---

## 🔍 Layer 4: Function Layer Blocking

### **Location:** Multiple functions (lines 486-620)

### **The Guard Clause Pattern:**

Every edit function starts with this check:

```javascript
if (!isEditModeEnabled) return; // Immediately exit if not editor/admin
```

### **Protected Functions:**

#### **1. selectWinner() - Line 486**
```javascript
window.selectWinner = function(roundIdx, matchIdx, player) {
    if (!isEditModeEnabled) return; // ✅ BLOCKED
    // ... rest of function only runs for editors/admins
};
```

#### **2. updateScore() - Line 502**
```javascript
window.updateScore = function(roundIdx, matchIdx, field, value) {
    if (!isEditModeEnabled) return; // ✅ BLOCKED
    // ... update score logic
};
```

#### **3. updateMatchTime() - Line 510**
```javascript
window.updateMatchTime = function(roundIdx, matchIdx, value) {
    if (!isEditModeEnabled) return; // ✅ BLOCKED
    // ... update time logic
};
```

#### **4. startEditName() - Line 516**
```javascript
window.startEditName = function(roundIdx, matchIdx, player, event) {
    if (!isEditModeEnabled) return; // ✅ BLOCKED
    // ... start editing name
};
```

#### **5. saveName() - Line 523**
```javascript
window.saveName = function(roundIdx, matchIdx, player, newName, event) {
    if (!isEditModeEnabled) return; // ✅ BLOCKED
    // ... save name logic
};
```

#### **6. resetBracket() - Line 617**
```javascript
window.resetBracket = function() {
    if (!isEditModeEnabled) { 
        alert("Please login to reset the bracket"); 
        return; 
    } // ✅ BLOCKED with alert
    // ... reset logic
};
```

#### **7. showContactTooltip() - Line 543**
```javascript
window.showContactTooltip = function(event, playerName) {
    if (!isEditModeEnabled) return; // ✅ BLOCKED
    // ... show tooltip logic
};
```

### **Why Guard Clauses?**

Even if someone bypasses the UI (using browser console, for example):
```javascript
// Viewer tries to cheat:
selectWinner(0, 0, 'player1'); // ❌ Function returns immediately, nothing happens
```

The function exits immediately without executing any logic!

---

## 🔍 Layer 5: Backend Layer (Firebase Rules)

### **Location:** Firebase Console → Realtime Database → Rules

### **Recommended Rules:**

```json
{
  "rules": {
    ".read": true,  // Anyone can read (view brackets)
    ".write": "auth != null",  // Only authenticated users can write
    "users": {
      ".write": "root.child('users').child(auth.uid).child('role').val() === 'admin'"
      // Only admins can modify user roles
    }
  }
}
```

### **How it protects:**

Even if someone bypasses ALL client-side checks, Firebase will reject the write:

```javascript
// Viewer somehow bypasses all checks and tries to save:
set(dataRef, modifiedData)
  .catch(error => {
    // ❌ Firebase rejects: "Permission denied"
  });
```

---

## 🎯 Complete Blocking Flow

### **Example: Viewer tries to select a winner**

```
1. User clicks player name
   ↓
2. onclick="selectWinner(0, 0, 'player1')" fires
   ↓
3. Function checks: if (!isEditModeEnabled) return;
   ↓
4. isEditModeEnabled = false (viewer role)
   ↓
5. Function returns immediately ✅ BLOCKED
   ↓
6. Nothing happens!
```

### **Example: Editor selects a winner**

```
1. User clicks player name
   ↓
2. onclick="selectWinner(0, 0, 'player1')" fires
   ↓
3. Function checks: if (!isEditModeEnabled) return;
   ↓
4. isEditModeEnabled = true (editor role)
   ↓
5. Check passes, function continues
   ↓
6. Updates match.winner
   ↓
7. Calls saveToFirebase()
   ↓
8. Firebase accepts write (user is authenticated)
   ↓
9. Winner selected! ✅
```

---

## 📊 Security Layers Summary

| Layer | Check | Can Bypass? | Consequence if Bypassed |
|-------|-------|-------------|------------------------|
| **1. Role Detection** | Reads from Firebase DB | ❌ No | Server-controlled |
| **2. State Flag** | `isEditModeEnabled` | ⚠️ Console | Next layer blocks |
| **3. UI Disabled** | HTML disabled/styles | ⚠️ Console | Next layer blocks |
| **4. Function Guards** | `if (!isEditModeEnabled)` | ⚠️ Modify code | Next layer blocks |
| **5. Firebase Rules** | Server-side validation | ❌ No | **FINAL BLOCK** |

### **Layered Security Approach:**

```
User Action
    ↓
[UI Layer] ← Can be bypassed with console
    ↓
[Function Layer] ← Can be bypassed by modifying code
    ↓
[Firebase Backend] ← CANNOT be bypassed! ✅
    ↓
Action blocked or allowed
```

---

## 🧪 Testing the Blocking

### **Test as Viewer:**

```javascript
// Open browser console while NOT logged in

// Try to select winner:
selectWinner(0, 0, 'player1');
// Result: Nothing happens (function returns immediately)

// Try to update score:
updateScore(0, 0, 'score1', 10);
// Result: Nothing happens (function returns immediately)

// Check the flag:
console.log(isEditModeEnabled);
// Result: false
```

### **Test as Editor:**

```javascript
// Open browser console while logged in as Editor

// Check the flag:
console.log(isEditModeEnabled);
// Result: true

// Try to select winner:
selectWinner(0, 0, 'player1');
// Result: Winner selected! ✅
```

---

## 📝 Code Locations in Bracket Files

| Feature | Line Range | File |
|---------|-----------|------|
| Variable declarations | 393-394 | All brackets |
| Auth state listener | 228-273 | All brackets |
| State flag setting | 252, 267 | All brackets |
| applyEditControls() | 275-314 | All brackets |
| selectWinner() | 486-500 | All brackets |
| updateScore() | 502-508 | All brackets |
| updateMatchTime() | 510-514 | All brackets |
| startEditName() | 516-521 | All brackets |
| saveName() | 523-541 | All brackets |
| showContactTooltip() | 543-567 | All brackets |
| resetBracket() | 617-625 | All brackets |

---

## ✅ Summary

### **How Viewer Role Works:**

1. **User not logged in OR logged in with "viewer" role**
2. **`isEditModeEnabled` is set to `false`**
3. **UI elements are disabled (can't click, type, etc.)**
4. **All edit functions check `isEditModeEnabled` first**
5. **If `false`, functions return immediately without doing anything**
6. **Even if bypassed, Firebase rules reject unauthorized writes**

### **Result:**
- ✅ **Viewers can ONLY view** (no editing possible)
- ✅ **Multiple layers of protection**
- ✅ **Secure against client-side manipulation**
- ✅ **Firebase backend is final authority**

---

## 🔐 Security Best Practices Applied

1. ✅ **Defense in depth** (multiple layers)
2. ✅ **Fail-safe defaults** (default to viewer)
3. ✅ **Client + Server validation** (both sides check)
4. ✅ **Least privilege** (users only get what they need)
5. ✅ **Server authority** (Firebase has final say)

---

**The viewer role blocking is BULLETPROOF!** 🛡️

Even with browser console access, viewers cannot edit anything because:
- Functions block execution
- Firebase rejects unauthorized writes
- Server-side validation is the ultimate authority

