#!/usr/bin/env python3
"""
Script to add Firebase Authentication to tournament bracket HTML files
Adds role-based access control (Viewer/Editor/Admin)
"""

import os
import re

BRACKET_FILES = [
    'Bracket_Chess.html',
    'Bracket_Snooker.html',
    'Bracket_FIFA25.html',
    'Bracket_Foosball.html',
    'Bracket_Carrom_Doubles.html',
    'Bracket_Carrom_Singles.html',
    'Bracket_TableTennis_Doubles.html',
    'Bracket_TableTennis_Singles.html'
]

# Auth CSS styles
AUTH_STYLES = """        
        /* =================================== */
        /* AUTHENTICATION STYLES */
        /* =================================== */
        .auth-container { position: fixed; top: 20px; right: 20px; z-index: 1000; }
        .auth-info { background: rgba(255,255,255,0.95); padding: 12px 20px; border-radius: 25px; box-shadow: 0 4px 12px rgba(0,0,0,0.15); display: flex; align-items: center; gap: 12px; }
        .auth-info.viewer { border: 2px solid #9E9E9E; }
        .auth-info.editor { border: 2px solid #4CAF50; }
        .auth-info.admin { border: 2px solid #FF5722; }
        .role-badge { padding: 4px 12px; border-radius: 12px; font-size: 11px; font-weight: bold; text-transform: uppercase; }
        .role-badge.viewer { background: #E0E0E0; color: #424242; }
        .role-badge.editor { background: #4CAF50; color: white; }
        .role-badge.admin { background: #FF5722; color: white; }
        .user-email { font-size: 13px; color: #666; max-width: 200px; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
        .auth-btn { background: #667eea; color: white; border: none; padding: 8px 16px; border-radius: 15px; cursor: pointer; font-size: 13px; font-weight: bold; transition: all 0.3s; }
        .auth-btn:hover { background: #5568d3; transform: scale(1.05); }
        .logout-btn { background: #f44336; }
        .logout-btn:hover { background: #da190b; }
        .modal { display: none; position: fixed; z-index: 2000; left: 0; top: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.6); backdrop-filter: blur(5px); }
        .modal.show { display: flex; align-items: center; justify-content: center; }
        .modal-content { background: white; padding: 40px; border-radius: 20px; box-shadow: 0 20px 60px rgba(0,0,0,0.3); max-width: 400px; width: 90%; animation: slideIn 0.3s ease-out; }
        @keyframes slideIn { from { transform: translateY(-50px); opacity: 0; } to { transform: translateY(0); opacity: 1; } }
        .modal-header { text-align: center; margin-bottom: 30px; }
        .modal-header h2 { color: #667eea; font-size: 24px; margin-bottom: 10px; }
        .modal-header p { color: #666; font-size: 14px; }
        .form-group { margin-bottom: 20px; }
        .form-group label { display: block; margin-bottom: 8px; color: #333; font-weight: 500; font-size: 14px; }
        .form-group input { width: 100%; padding: 12px; border: 2px solid #e0e0e0; border-radius: 8px; font-size: 14px; transition: border-color 0.3s; }
        .form-group input:focus { outline: none; border-color: #667eea; }
        .form-error { color: #f44336; font-size: 13px; margin-top: 8px; display: none; }
        .form-error.show { display: block; }
        .modal-buttons { display: flex; gap: 10px; margin-top: 25px; }
        .modal-btn { flex: 1; padding: 12px; border: none; border-radius: 8px; font-size: 14px; font-weight: bold; cursor: pointer; transition: all 0.3s; }
        .modal-btn-primary { background: #667eea; color: white; }
        .modal-btn-primary:hover { background: #5568d3; }
        .modal-btn-secondary { background: #e0e0e0; color: #666; }
        .modal-btn-secondary:hover { background: #d0d0d0; }
        .read-only-notice { background: rgba(255,193,7,0.1); border: 2px solid #FFC107; border-radius: 10px; padding: 15px; margin: 15px auto; max-width: 900px; text-align: center; color: #F57C00; font-weight: bold; }
        .read-only-notice .lock-icon { font-size: 20px; margin-right: 8px; }
"""

# Auth HTML
AUTH_HTML = """    
    <!-- Authentication Container -->
    <div class="auth-container">
        <div class="auth-info" id="auth-info" style="display: none;">
            <span class="user-email" id="user-email"></span>
            <span class="role-badge" id="role-badge"></span>
            <button class="auth-btn logout-btn" onclick="logout()">Logout</button>
        </div>
        <button class="auth-btn" id="login-btn" onclick="showLoginModal()">Login</button>
    </div>
    
    <!-- Read-Only Notice -->
    <div class="read-only-notice" id="read-only-notice" style="display: none;">
        <span class="lock-icon">🔒</span>
        <span>You're in READ-ONLY mode. Login to edit brackets.</span>
    </div>
    
    <!-- Login Modal -->
    <div class="modal" id="login-modal">
        <div class="modal-content">
            <div class="modal-header">
                <h2>🔐 Login</h2>
                <p>Enter your credentials to access edit mode</p>
            </div>
            <div class="form-group">
                <label for="login-email">Email</label>
                <input type="email" id="login-email" placeholder="your.email@example.com" autocomplete="email">
            </div>
            <div class="form-group">
                <label for="login-password">Password</label>
                <input type="password" id="login-password" placeholder="Enter your password" autocomplete="current-password">
            </div>
            <div class="form-error" id="login-error"></div>
            <div class="modal-buttons">
                <button class="modal-btn modal-btn-secondary" onclick="hideLoginModal()">Cancel</button>
                <button class="modal-btn modal-btn-primary" onclick="loginWithEmail()">Login</button>
            </div>
        </div>
    </div>
"""

# Auth imports addition
AUTH_IMPORT = """        import { getAuth, signInWithEmailAndPassword, onAuthStateChanged, signOut } from 'https://www.gstatic.com/firebasejs/10.7.1/firebase-auth.js';"""

# Auth logic
AUTH_LOGIC = """
        
        // ========================================
        // AUTHENTICATION & ACCESS CONTROL
        // ========================================
        const auth = getAuth(app);
        let currentUser = null;
        let userRole = 'viewer'; // default: read-only
        
        // Check authentication state
        onAuthStateChanged(auth, async (user) => {
            if (user) {
                currentUser = user;
                // Get user role from database
                const userRoleRef = ref(db, `users/${user.uid}/role`);
                const snapshot = await get(userRoleRef);
                userRole = snapshot.exists() ? snapshot.val() : 'viewer';
                
                // Update UI
                document.getElementById('login-btn').style.display = 'none';
                document.getElementById('auth-info').style.display = 'flex';
                document.getElementById('auth-info').className = `auth-info ${userRole}`;
                document.getElementById('user-email').textContent = user.email;
                document.getElementById('role-badge').textContent = userRole;
                document.getElementById('role-badge').className = `role-badge ${userRole}`;
                
                // Show/hide read-only notice
                if (userRole === 'viewer') {
                    document.getElementById('read-only-notice').style.display = 'block';
                } else {
                    document.getElementById('read-only-notice').style.display = 'none';
                }
                
                // Enable/disable edit features
                enableEditFeatures(userRole !== 'viewer');
                
                console.log(`✅ Logged in as ${user.email} (${userRole})`);
            } else {
                currentUser = null;
                userRole = 'viewer';
                
                // Update UI
                document.getElementById('login-btn').style.display = 'block';
                document.getElementById('auth-info').style.display = 'none';
                document.getElementById('read-only-notice').style.display = 'block';
                
                // Disable edit features
                enableEditFeatures(false);
                
                console.log('👁️ Viewing as guest (read-only)');
            }
        });
        
        // Enable/disable edit features
        function enableEditFeatures(enabled) {
            // Disable player selection
            document.querySelectorAll('.player').forEach(player => {
                if (!player.classList.contains('tbd')) {
                    player.style.pointerEvents = enabled ? 'auto' : 'none';
                    player.style.cursor = enabled ? 'pointer' : 'not-allowed';
                }
            });
            
            // Disable score inputs
            document.querySelectorAll('.score-input').forEach(input => {
                input.disabled = !enabled;
                input.style.cursor = enabled ? 'text' : 'not-allowed';
                input.style.opacity = enabled ? '1' : '0.6';
            });
            
            // Disable time inputs
            document.querySelectorAll('.match-time input').forEach(input => {
                input.disabled = !enabled;
                input.style.cursor = enabled ? 'text' : 'not-allowed';
                input.style.opacity = enabled ? '1' : '0.6';
            });
            
            // Disable edit buttons
            document.querySelectorAll('.edit-btn').forEach(btn => {
                btn.disabled = !enabled;
                btn.style.display = enabled ? 'inline-block' : 'none';
            });
            
            // Disable reset button
            document.querySelectorAll('.controls button').forEach(btn => {
                if (btn.textContent.includes('Reset') || btn.textContent.includes('🗑️')) {
                    btn.disabled = !enabled;
                    btn.style.opacity = enabled ? '1' : '0.5';
                    btn.style.cursor = enabled ? 'pointer' : 'not-allowed';
                }
            });
        }
        
        // Login/Logout functions
        window.showLoginModal = function() {
            document.getElementById('login-modal').classList.add('show');
            document.getElementById('login-email').focus();
        };
        
        window.hideLoginModal = function() {
            document.getElementById('login-modal').classList.remove('show');
            document.getElementById('login-error').classList.remove('show');
            document.getElementById('login-email').value = '';
            document.getElementById('login-password').value = '';
        };
        
        window.loginWithEmail = async function() {
            const email = document.getElementById('login-email').value.trim();
            const password = document.getElementById('login-password').value;
            const errorEl = document.getElementById('login-error');
            
            if (!email || !password) {
                errorEl.textContent = 'Please enter both email and password';
                errorEl.classList.add('show');
                return;
            }
            
            try {
                await signInWithEmailAndPassword(auth, email, password);
                hideLoginModal();
            } catch (error) {
                console.error('Login error:', error);
                errorEl.textContent = error.message || 'Login failed. Please check your credentials.';
                errorEl.classList.add('show');
            }
        };
        
        window.logout = async function() {
            if (confirm('Are you sure you want to logout?')) {
                try {
                    await signOut(auth);
                    console.log('✅ Logged out successfully');
                } catch (error) {
                    console.error('Logout error:', error);
                    alert('Logout failed: ' + error.message);
                }
            }
        };
        
        // Enter key to login
        document.getElementById('login-password').addEventListener('keypress', (e) => {
            if (e.key === 'Enter') loginWithEmail();
        });
"""

def add_auth_to_file(filepath):
    """Add authentication to a single bracket file"""
    print(f"Processing: {os.path.basename(filepath)}")
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Add auth styles (before .bracket-container style)
    if '/* AUTHENTICATION STYLES */' not in content:
        content = content.replace(
            '        .bracket-container {',
            AUTH_STYLES + '        .bracket-container {'
        )
        print("  ✅ Added auth styles")
    else:
        print("  ⏭️  Auth styles already exist")
    
    # 2. Add auth HTML (after .header div, before .controls div)
    if '<!-- Authentication Container -->' not in content:
        content = content.replace(
            '    <div class="controls">',
            AUTH_HTML + '    <div class="controls">'
        )
        print("  ✅ Added auth HTML")
    else:
        print("  ⏭️  Auth HTML already exists")
    
    # 3. Add auth import
    if 'getAuth' not in content:
        old_imports = "import { getDatabase, ref, set, onValue, get } from 'https://www.gstatic.com/firebasejs/10.7.1/firebase-database.js';"
        new_imports = old_imports + "\n" + AUTH_IMPORT
        content = content.replace(old_imports, new_imports)
        print("  ✅ Added auth imports")
    else:
        print("  ⏭️  Auth imports already exist")
    
    # 4. Add auth logic (after firebase initialization)
    if '// AUTHENTICATION & ACCESS CONTROL' not in content:
        # Find the line after "dataRef = ref(db, `tournaments/{SPORT}`);"
        pattern = r"(dataRef = ref\(db, `tournaments/[^`]+`\);)"
        match = re.search(pattern, content)
        if match:
            insertion_point = match.end()
            content = content[:insertion_point] + AUTH_LOGIC + content[insertion_point:]
            print("  ✅ Added auth logic")
        else:
            print("  ⚠️  Could not find insertion point for auth logic")
    else:
        print("  ⏭️  Auth logic already exists")
    
    # Write back
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"  ✅ {os.path.basename(filepath)} updated!\n")

def main():
    base_path = '/Users/sbhagat/Insports'
    
    print("=" * 60)
    print("🔐 Adding Authentication to Tournament Brackets")
    print("=" * 60)
    print()
    
    for filename in BRACKET_FILES:
        filepath = os.path.join(base_path, filename)
        if os.path.exists(filepath):
            try:
                add_auth_to_file(filepath)
            except Exception as e:
                print(f"  ❌ Error: {e}\n")
        else:
            print(f"❌ File not found: {filename}\n")
    
    print("=" * 60)
    print("✅ Authentication added to all brackets!")
    print("=" * 60)
    print()
    print("📝 Next steps:")
    print("1. Enable Firebase Authentication in Firebase Console")
    print("2. Open setup_admin.html to create your first admin user")
    print("3. Test login on any bracket page")
    print("4. Read AUTH_SETUP_GUIDE.md for full documentation")
    print()

if __name__ == '__main__':
    main()

