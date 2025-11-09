#!/usr/bin/env python3
"""
Restrict reset button to admin users only.
"""

import re
from pathlib import Path

def fix_reset_admin_only(file_path):
    """Update reset button to only work for admin users."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Fix 1: Update applyEditControls() to check for admin role
    # Pattern to find the reset button logic
    pattern1 = r'''// Disable/enable reset button \(but NOT back/print buttons\)
\s*document\.querySelectorAll\('\.controls button'\)\.forEach\(btn => \{
\s*// Only disable reset button, not back or print buttons
\s*if \(btn\.textContent\.includes\('Reset'\) \|\| btn\.textContent\.includes\('🗑️'\)\) \{
\s*btn\.disabled = !enabled;
\s*btn\.style\.opacity = enabled \? '1' : '0\.5';
\s*btn\.style\.cursor = enabled \? 'pointer' : 'not-allowed';
\s*\}
\s*\}\);'''
    
    replacement1 = '''// Reset button - ONLY for admin users
            document.querySelectorAll('.controls button').forEach(btn => {
                if (btn.textContent.includes('Reset') || btn.textContent.includes('🗑️')) {
                    // Only admins can reset
                    const isAdmin = userRole === 'admin';
                    btn.disabled = !isAdmin;
                    btn.style.opacity = isAdmin ? '1' : '0.5';
                    btn.style.cursor = isAdmin ? 'pointer' : 'not-allowed';
                }
                // Back and Print buttons remain enabled for all users
            });'''
    
    content = re.sub(pattern1, replacement1, content, flags=re.MULTILINE)
    
    # Fix 2: Update resetBracket() function to check for admin role
    pattern2 = r'''window\.resetBracket = function\(\) \{
\s*if \(!isEditModeEnabled\) return;
\s*if \(!isEditModeEnabled\) \{ alert\("Please login to reset the bracket"\); return; \} // Check edit permission
\s*if \(confirm\('Reset entire bracket\? This will clear all scores and times\.'\)\) \{'''
    
    replacement2 = '''window.resetBracket = function() {
        // Only admin users can reset brackets
        if (userRole !== 'admin') {
            alert("Only administrators can reset the bracket");
            return;
        }
            if (confirm('Reset entire bracket? This will clear all scores and times.')) {'''
    
    content = re.sub(pattern2, replacement2, content, flags=re.MULTILINE)
    
    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✅ Updated {file_path.name}")
        return True
    else:
        print(f"⏭️  No changes needed for {file_path.name}")
        return False

def main():
    # Get all bracket HTML files
    bracket_files = list(Path('.').glob('Bracket_*.html'))
    
    if not bracket_files:
        print("❌ No bracket files found!")
        return
    
    print(f"Found {len(bracket_files)} bracket files")
    print("=" * 60)
    
    updated_count = 0
    for file_path in sorted(bracket_files):
        if fix_reset_admin_only(file_path):
            updated_count += 1
    
    print("=" * 60)
    print(f"\n✅ Complete! Updated {updated_count} files")
    print("\n📝 Changes made:")
    print("   ✅ Reset button now requires admin role")
    print("   ✅ Added admin check in resetBracket() function")
    print("\n🔐 Button Access:")
    print("   ⬅️ Back button → ALL USERS")
    print("   🖨️ Print button → ALL USERS")
    print("   🗑️ Reset button → ADMIN ONLY")
    print("\n📊 User Permissions:")
    print("   🔒 Non-logged in → Can view, cannot edit, cannot reset")
    print("   🔒 Viewer role → Can view, cannot edit, cannot reset")
    print("   ✏️  Editor role → Can view, can edit, CANNOT reset")
    print("   👑 Admin role → Can view, can edit, CAN reset")

if __name__ == '__main__':
    main()

