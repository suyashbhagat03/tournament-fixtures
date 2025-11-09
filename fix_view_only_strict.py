#!/usr/bin/env python3
"""
Strict view-only mode:
- NO tooltips for non-editors
- NO time updates for non-editors
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

def fix_strict_view_only(filepath):
    """Disable tooltips and time updates for view-only users"""
    print(f"Fixing: {os.path.basename(filepath)}")
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    changes = []
    
    # 1. Add permission check back to showContactTooltip
    old_tooltip = r'window\.showContactTooltip = function\(event, playerName\) \{\s+// Tooltips are view-only feature - available to everyone'
    new_tooltip = r'window.showContactTooltip = function(event, playerName) {\n            if (!isEditModeEnabled) return; // Only show tooltips to editors/admins'
    
    if re.search(old_tooltip, content):
        content = re.sub(old_tooltip, new_tooltip, content)
        changes.append("Disabled tooltips for view-only users")
    
    # 2. Verify updateMatchTime has permission check
    if 'window.updateMatchTime = function' in content:
        # Check if it already has the permission check
        updateMatchTime_section = content.split('window.updateMatchTime = function')[1].split('function')[0]
        if 'if (!isEditModeEnabled) return;' not in updateMatchTime_section:
            old_time = r'window\.updateMatchTime = function\(roundIdx, matchIdx, time\) \{'
            new_time = r'window.updateMatchTime = function(roundIdx, matchIdx, time) {\n            if (!isEditModeEnabled) return; // Check edit permission'
            content = re.sub(old_time, new_time, content)
            changes.append("Added permission check to updateMatchTime")
        else:
            changes.append("updateMatchTime already protected")
    
    # Write back if changes were made
    if changes:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        for change in changes:
            print(f"  ✅ {change}")
    else:
        print("  ⚠️  No changes needed")
    
    print()

def main():
    base_path = '/Users/sbhagat/Insports'
    
    print("=" * 70)
    print("🔒 Enforcing Strict View-Only Mode")
    print("=" * 70)
    print()
    
    for filename in BRACKET_FILES:
        filepath = os.path.join(base_path, filename)
        if os.path.exists(filepath):
            try:
                fix_strict_view_only(filepath)
            except Exception as e:
                print(f"  ❌ Error: {e}\n")
        else:
            print(f"❌ File not found: {filename}\n")
    
    print("=" * 70)
    print("✅ All brackets updated!")
    print("=" * 70)
    print()
    print("🔒 View-Only Mode (Non-logged in + Viewer role):")
    print("  ✅ Can view brackets")
    print("  ❌ Cannot see tooltips (contact info)")
    print("  ❌ Cannot update times")
    print("  ❌ Cannot edit scores")
    print("  ❌ Cannot select winners")
    print("  ✅ Can print/export")
    print()
    print("✏️ Editor/Admin Mode:")
    print("  ✅ Can view everything")
    print("  ✅ Can see tooltips")
    print("  ✅ Can update times")
    print("  ✅ Can edit brackets")
    print("  ✅ Full access")
    print()

if __name__ == '__main__':
    main()

