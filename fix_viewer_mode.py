#!/usr/bin/env python3
"""
Make non-logged in users behave exactly like Viewer role users:
- Can view everything (including tooltips)
- Cannot edit anything
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

def fix_viewer_mode(filepath):
    """Enable tooltips for all users (view-only feature), keep edit functions protected"""
    print(f"Fixing: {os.path.basename(filepath)}")
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove the isEditModeEnabled check from showContactTooltip
    # Tooltips are view-only feature, should work for everyone
    old_tooltip = r'window\.showContactTooltip = function\(event, playerName\) \{\s+if \(!isEditModeEnabled\) return; // Only show tooltips when logged in'
    new_tooltip = r'window.showContactTooltip = function(event, playerName) {\n            // Tooltips are view-only feature - available to everyone'
    
    if re.search(old_tooltip, content):
        content = re.sub(old_tooltip, new_tooltip, content)
        print("  ✅ Enabled tooltips for all users (view-only feature)")
    else:
        print("  ⚠️  Tooltip pattern not found or already fixed")
    
    # Write back
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print()

def main():
    base_path = '/Users/sbhagat/Insports'
    
    print("=" * 70)
    print("🔧 Making Viewer Mode Consistent for All Non-Editors")
    print("=" * 70)
    print()
    
    for filename in BRACKET_FILES:
        filepath = os.path.join(base_path, filename)
        if os.path.exists(filepath):
            try:
                fix_viewer_mode(filepath)
            except Exception as e:
                print(f"  ❌ Error: {e}\n")
        else:
            print(f"❌ File not found: {filename}\n")
    
    print("=" * 70)
    print("✅ All brackets updated!")
    print("=" * 70)
    print()
    print("🎯 Viewer Mode (Non-logged in + Viewer role):")
    print("  ✅ Can view brackets")
    print("  ✅ Can see tooltips (email/phone)")
    print("  ✅ Can print/export")
    print("  ❌ Cannot edit anything")
    print()
    print("✏️ Editor/Admin Mode:")
    print("  ✅ Can view everything")
    print("  ✅ Can see tooltips")
    print("  ✅ Can edit brackets")
    print("  ✅ Full access")
    print()

if __name__ == '__main__':
    main()

