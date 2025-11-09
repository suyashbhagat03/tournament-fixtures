# 🏆 Insportsathon - Tournament Management System

A real-time, web-based tournament bracket management system for organizing and tracking multiple sports tournaments simultaneously. Built with Firebase for real-time synchronization and role-based access control.

[![Firebase](https://img.shields.io/badge/Firebase-FFCA28?style=flat&logo=firebase&logoColor=black)](https://firebase.google.com/)
[![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat&logo=javascript&logoColor=black)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
[![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat&logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/HTML)
[![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat&logo=css3&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/CSS)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## 📋 Table of Contents

- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Demo](#-demo)
- [Screenshots](#-screenshots)
- [Getting Started](#-getting-started)
- [Firebase Setup](#-firebase-setup)
- [Security Rules](#-security-rules)
- [Deployment](#-deployment)
- [Usage](#-usage)
- [Project Structure](#-project-structure)
- [User Roles](#-user-roles)
- [Contributing](#-contributing)
- [License](#-license)

---

## ✨ Features

### 🎯 Core Functionality
- **Real-time Tournament Brackets** - Live updates across all devices
- **8 Sports Support** - Chess, Table Tennis (Singles & Doubles), Carrom (Singles & Doubles), Foosball, Snooker, FIFA 25
- **Single Elimination Format** - Automatic bracket generation with bye management
- **Score Tracking** - Live score input with automatic winner advancement
- **Match Scheduling** - Editable time slots for each match
- **Contact Management** - Player email and phone on-hover tooltips

### 🔐 Security & Access Control
- **Firebase Authentication** - Secure email/password login
- **Role-Based Access Control (RBAC)** - Three user roles: Viewer, Editor, Admin
- **Read-Only Mode** - Non-authenticated users can view but not edit
- **Admin Panel** - User management and contact information editing
- **Secure Rules** - Firebase security rules prevent unauthorized access

### 🎨 User Experience
- **Responsive Design** - Works on desktop, tablet, and mobile
- **Interactive UI** - Click to select winners, edit names, update scores
- **Visual Feedback** - Color-coded winners, live status indicators
- **Print Support** - Tournament brackets can be printed
- **Dark Mode Headers** - Modern gradient design

### 🚀 Performance
- **Real-time Sync** - Changes reflect instantly across all devices
- **Offline Support** - Firebase handles connectivity issues gracefully
- **Fast Loading** - Optimized asset delivery via Firebase Hosting
- **CDN Distribution** - Global Firebase CDN for low latency

---

## 🛠️ Tech Stack

### Frontend
- **HTML5** - Semantic markup
- **CSS3** - Modern styling with gradients and animations
- **Vanilla JavaScript** - No framework dependencies
- **Firebase SDK** - Client-side Firebase integration

### Backend & Infrastructure
- **Firebase Realtime Database** - NoSQL real-time data storage
- **Firebase Authentication** - User authentication and management
- **Firebase Hosting** - Static site hosting with CDN
- **Firebase Security Rules** - Server-side access control

### Development Tools
- **Python** - Data processing and CSV parsing
- **Bash Scripts** - Automation and deployment
- **Git** - Version control

---

## 🎬 Demo

**Live Demo:** [Your Firebase URL here]

**Test Credentials:**
- **Viewer:** viewer@example.com / [password]
- **Editor:** editor@example.com / [password]
- **Admin:** admin@example.com / [password]

---

## 📸 Screenshots

<!-- Add screenshots here -->
```
[Main Dashboard]          [Tournament Bracket]       [Admin Panel]
     |                           |                        |
     v                           v                        v
[Screenshot]              [Screenshot]              [Screenshot]
```

---

## 🚀 Getting Started

### Prerequisites

- **Node.js** (v14+) - [Download](https://nodejs.org/)
- **Firebase CLI** - Install globally
- **Firebase Project** - Create at [Firebase Console](https://console.firebase.google.com/)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/insportsathon.git
   cd insportsathon
   ```

2. **Install Firebase CLI**
   ```bash
   npm install -g firebase-tools
   ```

3. **Login to Firebase**
   ```bash
   firebase login
   ```

4. **Initialize Firebase** (if not already done)
   ```bash
   firebase init
   ```
   Select:
   - ✅ Realtime Database
   - ✅ Hosting
   - ✅ Authentication (optional)

5. **Configure Firebase**
   - Update Firebase config in all HTML files (see [Firebase Setup](#-firebase-setup))

---

## 🔥 Firebase Setup

### Step 1: Create Firebase Project

1. Go to [Firebase Console](https://console.firebase.google.com/)
2. Click **"Add project"**
3. Name it (e.g., "Insportsathon")
4. Enable Google Analytics (optional)

### Step 2: Enable Services

#### **Realtime Database**
1. Go to **Realtime Database** in sidebar
2. Click **"Create Database"**
3. Choose location (e.g., `asia-southeast1`)
4. Start in **Test Mode** (we'll secure it later)

#### **Authentication**
1. Go to **Authentication** in sidebar
2. Click **"Get Started"**
3. Enable **Email/Password** provider
4. **Important:** Go to **Settings** → Disable **"Create (sign-up)"** to prevent spam accounts

#### **Hosting**
1. Firebase CLI will set this up automatically
2. Or manually: Go to **Hosting** → **Get Started**

### Step 3: Get Firebase Config

1. Go to **Project Settings** (gear icon)
2. Scroll to **"Your apps"**
3. Click **Web** icon (`</>`)
4. Copy the `firebaseConfig` object

### Step 4: Update Config in HTML Files

Update the config in these files:
- All `Bracket_*.html` files (8 files)
- `index.html`
- `contact_management.html`
- `user_management.html`

Replace this section:
```javascript
const firebaseConfig = {
    apiKey: "YOUR_API_KEY",
    authDomain: "YOUR_PROJECT.firebaseapp.com",
    databaseURL: "https://YOUR_PROJECT.firebasedatabase.app",
    projectId: "YOUR_PROJECT",
    storageBucket: "YOUR_PROJECT.appspot.com",
    messagingSenderId: "YOUR_SENDER_ID",
    appId: "YOUR_APP_ID"
};
```

---

## 🔒 Security Rules

### Deploy Database Security Rules

**Important:** Replace test mode rules with production rules!

1. **Choose your security level:**
   - `database.rules.json` - Basic secure rules
   - `database.rules.enhanced.json` - Enhanced with validation
   - `database.rules.whitelist.json` - Maximum security (recommended)

2. **Deploy rules:**
   ```bash
   # Option 1: Via CLI
   firebase deploy --only database

   # Option 2: Via Console
   # Copy contents from database.rules.whitelist.json
   # Paste in Firebase Console → Realtime Database → Rules
   # Click "Publish"
   ```

### Security Rules Overview

| Path | Read Access | Write Access |
|------|-------------|--------------|
| `/tournaments/{sport}/` | ✅ Public | 👥 Editors & Admins only |
| `/contacts/{sport}/` | 🔒 Authenticated users | 👑 Admins only |
| `/users/{uid}/` | 🔒 Self & Admins | 👑 Admins only |

**Recommended:** Use `database.rules.whitelist.json` for production (explicitly whitelists 8 sports only).

---

## 🚀 Deployment

### Initial Setup

1. **Create first admin user**
   ```bash
   # Run local server
   firebase serve

   # Open in browser
   open http://localhost:5000/setup_admin.html

   # Create admin account
   # Then delete setup_admin.html
   ```

2. **Import contact information**
   ```bash
   # Open import tool
   open http://localhost:5000/import_contacts_initial.html

   # Click "Start Import"
   # Wait for completion (~30 seconds)
   ```

3. **Deploy security rules**
   ```bash
   firebase deploy --only database
   ```

4. **Deploy application**
   ```bash
   firebase deploy --only hosting
   ```

### Update Deployment

```bash
# Deploy everything
firebase deploy

# Deploy only hosting
firebase deploy --only hosting

# Deploy only database rules
firebase deploy --only database
```

### CI/CD (Optional)

Set up GitHub Actions for automatic deployment:

```yaml
# .github/workflows/deploy.yml
name: Deploy to Firebase
on:
  push:
    branches: [main]
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: w9jds/firebase-action@master
        with:
          args: deploy --only hosting
        env:
          FIREBASE_TOKEN: ${{ secrets.FIREBASE_TOKEN }}
```

---

## 📖 Usage

### For Viewers (Non-logged in users)

1. Visit the application URL
2. Click on any sport from the dashboard
3. View live tournament brackets
4. See match results and scores
5. Cannot edit or modify anything

### For Editors

1. **Login** with editor credentials
2. **View tournaments** from dashboard
3. **Edit match details:**
   - Click player names to select winners
   - Enter scores for each player
   - Update match times/schedules
   - Edit player/team names
4. **View contact info** (hover over player names)
5. Cannot manage users or contacts

### For Admins

**All editor permissions, plus:**

1. **Manage Users** (`user_management.html`)
   - Add new users
   - Assign roles (viewer/editor/admin)
   - Delete users

2. **Manage Contacts** (`contact_management.html`)
   - Add player contact information
   - Edit email and phone numbers
   - Update team partner details

3. **Reset Brackets** (use with caution)
   - Reset tournament to initial state

---

## 📁 Project Structure

```
insportsathon/
├── index.html                          # Main dashboard
├── Bracket_*.html (8 files)            # Tournament bracket pages
├── contact_management.html             # Contact editor (admin)
├── user_management.html                # User manager (admin)
├── *.csv (8 files)                     # Source registration data
├── firebase.json                       # Firebase hosting config
├── database.rules.json                 # Basic security rules
├── database.rules.enhanced.json        # Enhanced security rules
├── database.rules.whitelist.json       # Maximum security rules (recommended)
├── .firebaserc                         # Firebase project config
└── README.md                           # This file
```

### HTML Files

| File | Purpose | Access |
|------|---------|--------|
| `index.html` | Main dashboard with sport links | Public |
| `Bracket_Chess.html` | Chess tournament bracket | Public view, Auth edit |
| `Bracket_TableTennis_Singles.html` | TT Singles bracket | Public view, Auth edit |
| `Bracket_TableTennis_Doubles.html` | TT Doubles bracket | Public view, Auth edit |
| `Bracket_Carrom_Singles.html` | Carrom Singles bracket | Public view, Auth edit |
| `Bracket_Carrom_Doubles.html` | Carrom Doubles bracket | Public view, Auth edit |
| `Bracket_Foosball.html` | Foosball bracket | Public view, Auth edit |
| `Bracket_Snooker.html` | Snooker bracket | Public view, Auth edit |
| `Bracket_FIFA25.html` | FIFA 25 bracket | Public view, Auth edit |
| `contact_management.html` | Contact info editor | Admin only |
| `user_management.html` | User role manager | Admin only |

### Data Files

| File | Purpose |
|------|---------|
| `Chess.csv` | Chess registrations (66 players) |
| `TableTennis_Singles.csv` | TT Singles (94 players) |
| `TableTennis_Doubles.csv` | TT Doubles (50 teams) |
| `Carrom_Singles.csv` | Carrom Singles (60 players) |
| `Carrom_Doubles.csv` | Carrom Doubles (32 teams) |
| `Foosball.csv` | Foosball (50 teams) |
| `Snooker.csv` | Snooker (38 players) |
| `FIFA25.csv` | FIFA 25 (52 players) |

---

## 👥 User Roles

### Viewer
- ✅ View all tournament brackets
- ✅ See match results and scores
- ✅ See player/team names
- ❌ Cannot edit anything
- ❌ Cannot see contact information
- ❌ Cannot manage users

### Editor
- ✅ All viewer permissions
- ✅ Edit tournament brackets
- ✅ Select match winners
- ✅ Update scores
- ✅ Modify match times
- ✅ Edit player names
- ✅ View contact information
- ❌ Cannot manage users
- ❌ Cannot edit contacts
- ❌ Cannot reset brackets

### Admin
- ✅ All editor permissions
- ✅ Manage user accounts
- ✅ Assign/change user roles
- ✅ Edit contact information
- ✅ Add/remove players
- ✅ Reset tournament brackets
- ✅ Full system access

---

## 🔄 Data Flow

```
┌─────────────────────────────────────────────────────────┐
│                     CSV Files (Initial)                 │
│  Chess.csv, TableTennis_*.csv, Carrom_*.csv, etc.      │
└─────────────────┬───────────────────────────────────────┘
                  │ import_contacts_initial.html
                  ↓
┌─────────────────────────────────────────────────────────┐
│              Firebase Realtime Database                 │
│  ├── tournaments/{sport}/rounds                         │
│  ├── contacts/{sport}/{player}                          │
│  └── users/{uid}/role                                   │
└─────────────────┬───────────────────────────────────────┘
                  │ Real-time sync
                  ↓
┌─────────────────────────────────────────────────────────┐
│                HTML Bracket Files                       │
│  ├── Read: Tournament state                            │
│  ├── Write: Score updates, winner selection            │
│  └── Subscribe: Real-time changes                      │
└─────────────────────────────────────────────────────────┘
```

---

## 🛡️ Security Features

### Authentication
- ✅ Firebase Email/Password authentication
- ✅ Secure password hashing (Firebase handles)
- ✅ Session management with `onAuthStateChanged`
- ✅ Auto-logout on session expiry

### Authorization
- ✅ Role-based access control (RBAC)
- ✅ Server-side Firebase security rules
- ✅ Client-side UI permission guards
- ✅ Function-level permission checks

### Data Protection
- ✅ Contact info not hardcoded (loaded from Firebase)
- ✅ No sensitive data in client-side code
- ✅ Public registration disabled (admin-only user creation)
- ✅ Whitelist-based database paths

### Best Practices
- ✅ HTTPS-only (Firebase Hosting enforces)
- ✅ Regular security rule audits
- ✅ Minimal client-side trust
- ✅ Server-side validation via Firebase rules

---

## 🧪 Testing

### Manual Testing Checklist

**As Non-logged User:**
- [ ] Can view all tournament brackets
- [ ] Cannot edit match details
- [ ] Cannot see contact tooltips
- [ ] Cannot reset brackets
- [ ] Login button visible

**As Viewer:**
- [ ] Can view all brackets
- [ ] Cannot edit anything
- [ ] Can see contact tooltips
- [ ] Cannot access admin panels

**As Editor:**
- [ ] Can select winners
- [ ] Can update scores
- [ ] Can edit player names
- [ ] Can modify match times
- [ ] Cannot reset (admin only)
- [ ] Cannot access admin panels

**As Admin:**
- [ ] All editor permissions work
- [ ] Can access user management
- [ ] Can access contact management
- [ ] Can reset brackets
- [ ] Can create/delete users

---

## 🐛 Troubleshooting

### Firebase Connection Issues

**Problem:** "FIREBASE SETUP REQUIRED" warning  
**Solution:** 
1. Verify Firebase config is correct
2. Ensure Realtime Database is created
3. Check browser console for errors
4. Clear browser cache

### Authentication Issues

**Problem:** Cannot login  
**Solution:**
1. Check Firebase Auth is enabled
2. Verify user exists in Firebase Console
3. Check browser console for errors
4. Try password reset

### Permission Denied Errors

**Problem:** "Permission Denied" in console  
**Solution:**
1. Deploy security rules: `firebase deploy --only database`
2. Verify user has correct role in Firebase Console
3. Check `/users/{uid}/role` exists in database

### Real-time Sync Not Working

**Problem:** Changes not appearing on other devices  
**Solution:**
1. Check internet connection
2. Verify Firebase Database URL is correct
3. Check browser console for WebSocket errors
4. Refresh all browser tabs

---

## 🚧 Known Limitations

- Bracket structure is fixed (single elimination only)
- No double elimination support
- No round-robin support
- Manual advancement only (no automatic scheduling)
- Limited to 8 predefined sports

---

## 🗺️ Roadmap

### v2.0 (Future)
- [ ] Double elimination brackets
- [ ] Round-robin support
- [ ] Automatic match scheduling
- [ ] Email notifications
- [ ] Mobile app (React Native)
- [ ] Export to PDF
- [ ] Advanced statistics
- [ ] Live streaming integration

---

## 🤝 Contributing

Contributions are welcome! Please follow these guidelines:

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/amazing-feature
   ```
3. **Commit your changes**
   ```bash
   git commit -m 'Add amazing feature'
   ```
4. **Push to the branch**
   ```bash
   git push origin feature/amazing-feature
   ```
5. **Open a Pull Request**

### Code Style
- Use consistent indentation (2 spaces)
- Add comments for complex logic
- Follow existing naming conventions
- Test on multiple browsers

### Reporting Bugs
- Use GitHub Issues
- Include browser version
- Provide steps to reproduce
- Include console errors (if any)

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2025 Insportsathon

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## 👨‍💻 Authors

- **Your Name** - *Initial work* - [YourGitHub](https://github.com/yourusername)

---

## 🙏 Acknowledgments

- Firebase team for excellent documentation
- All tournament participants
- Open source community
- [Add your acknowledgments here]

---

## 📞 Support

- **Issues:** [GitHub Issues](https://github.com/yourusername/insportsathon/issues)
- **Email:** your.email@example.com
- **Documentation:** See `/docs` folder for detailed guides

---

## 📊 Stats

- **Sports:** 8
- **Total Participants:** ~400+
- **Lines of Code:** ~10,000+
- **Firebase Services:** 3 (Database, Auth, Hosting)
- **Deployment Time:** < 5 minutes

---

<div align="center">

**⭐ Star this repo if you found it helpful!**

Made with ❤️ for Insportsathon 2025

[Live Demo](#) • [Report Bug](https://github.com/yourusername/insportsathon/issues) • [Request Feature](https://github.com/yourusername/insportsathon/issues)

</div>

