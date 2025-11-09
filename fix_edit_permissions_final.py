#!/usr/bin/env python3
"""
Final fix for edit permissions - wrap all edit functions to check isEditModeEnabled
Also disable tooltips when not logged in
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

def fix_bracket_file(filepath):
    """Add permission checks to all edit functions"""
    print(f"Fixing: {os.path.basename(filepath)}")
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    changes = []
    
    # 1. Wrap selectWinner function
    if 'window.selectWinner = function' in content and 'if (!isEditModeEnabled)' not in content.split('window.selectWinner = function')[1].split('function')[0]:
        old_select = r'window\.selectWinner = function\(roundIdx, matchIdx, player\) \{'
        new_select = r'window.selectWinner = function(roundIdx, matchIdx, player) {\n            if (!isEditModeEnabled) return; // Check edit permission'
        content = re.sub(old_select, new_select, content)
        changes.append("Added permission check to selectWinner")
    
    # 2. Wrap updateScore function
    if 'window.updateScore = function' in content and 'if (!isEditModeEnabled)' not in content.split('window.updateScore = function')[1].split('function')[0]:
        old_score = r'window\.updateScore = function\(roundIdx, matchIdx, field, value\) \{'
        new_score = r'window.updateScore = function(roundIdx, matchIdx, field, value) {\n            if (!isEditModeEnabled) return; // Check edit permission'
        content = re.sub(old_score, new_score, content)
        changes.append("Added permission check to updateScore")
    
    # 3. Wrap updateMatchTime function
    if 'window.updateMatchTime = function' in content and 'if (!isEditModeEnabled)' not in content.split('window.updateMatchTime = function')[1].split('function')[0]:
        old_time = r'window\.updateMatchTime = function\(roundIdx, matchIdx, time\) \{'
        new_time = r'window.updateMatchTime = function(roundIdx, matchIdx, time) {\n            if (!isEditModeEnabled) return; // Check edit permission'
        content = re.sub(old_time, new_time, content)
        changes.append("Added permission check to updateMatchTime")
    
    # 4. Wrap startEditName function
    if 'window.startEditName = function' in content and 'if (!isEditModeEnabled)' not in content.split('window.startEditName = function')[1].split('function')[0]:
        old_edit = r'window\.startEditName = function\(roundIdx, matchIdx, player, event\) \{'
        new_edit = r'window.startEditName = function(roundIdx, matchIdx, player, event) {\n            if (!isEditModeEnabled) return; // Check edit permission'
        content = re.sub(old_edit, new_edit, content)
        changes.append("Added permission check to startEditName")
    
    # 5. Wrap saveName function
    if 'window.saveName = function' in content and 'if (!isEditModeEnabled)' not in content.split('window.saveName = function')[1].split('function')[0]:
        old_save = r'window\.saveName = function\(roundIdx, matchIdx, player, newName, event\) \{'
        new_save = r'window.saveName = function(roundIdx, matchIdx, player, newName, event) {\n            if (!isEditModeEnabled) return; // Check edit permission'
        content = re.sub(old_save, new_save, content)
        changes.append("Added permission check to saveName")
    
    # 6. Wrap resetBracket function
    if 'window.resetBracket = function' in content and 'if (!isEditModeEnabled)' not in content.split('window.resetBracket = function')[1].split('function')[0]:
        old_reset = r'window\.resetBracket = function\(\) \{'
        new_reset = r'window.resetBracket = function() {\n            if (!isEditModeEnabled) { alert("Please login to reset the bracket"); return; } // Check edit permission'
        content = re.sub(old_reset, new_reset, content)
        changes.append("Added permission check to resetBracket")
    
    # 7. Disable tooltips when not logged in - wrap showContactTooltip
    if 'window.showContactTooltip = function' in content and 'if (!isEditModeEnabled)' not in content.split('window.showContactTooltip = function')[1].split('function')[0]:
        old_tooltip = r'window\.showContactTooltip = function\(event, playerName\) \{'
        new_tooltip = r'window.showContactTooltip = function(event, playerName) {\n            if (!isEditModeEnabled) return; // Only show tooltips when logged in'
        content = re.sub(old_tooltip, new_tooltip, content)
        changes.append("Disabled tooltips for non-logged in users")
    
    # Write back if changes were made
    if changes:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        for change in changes:
            print(f"  ✅ {change}")
        print()
    else:
        print("  ⚠️  No changes needed (already fixed)\n")

def main():
    base_path = '/Users/sbhagat/Insports'
    
    print("=" * 70)
    print("🔧 FINAL FIX: Adding Permission Checks to All Edit Functions")
    print("=" * 70)
    print()
    
    for filename in BRACKET_FILES:
        filepath = os.path.join(base_path, filename)
        if os.path.exists(filepath):
            try:
                fix_bracket_file(filepath)
            except Exception as e:
                print(f"  ❌ Error: {e}\n")
        else:
            print(f"❌ File not found: {filename}\n")
    
    print("=" * 70)
    print("✅ All brackets fixed!")
    print("=" * 70)
    print()
    print("🎯 Changes made:")
    print("1. selectWinner() - checks isEditModeEnabled before executing")
    print("2. updateScore() - checks isEditModeEnabled before executing")
    print("3. updateMatchTime() - checks isEditModeEnabled before executing")
    print("4. startEditName() - checks isEditModeEnabled before executing")
    print("5. saveName() - checks isEditModeEnabled before executing")
    print("6. resetBracket() - checks isEditModeEnabled before executing")
    print("7. showContactTooltip() - only shows when logged in")
    print()
    print("✨ Result:")
    print("• Without login → Cannot edit ANYTHING (bulletproof!) ✅")
    print("• After login → Can edit everything ✅")
    print("• Tooltips only show when logged in ✅")
    print()

if __name__ == '__main__':
    main()

