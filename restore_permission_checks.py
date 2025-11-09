#!/usr/bin/env python3
"""
Restore permission checks to make non-logged in users and viewer role users read-only.
"""

import re
from pathlib import Path

def restore_permission_checks(file_path):
    """Add permission checks back to all edit functions."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Functions that need permission checks restored
    functions_to_fix = [
        ('selectWinner', 'roundIdx, matchIdx, player'),
        ('updateScore', 'roundIdx, matchIdx, field, value'),
        ('updateMatchTime', 'roundIdx, matchIdx, value'),
        ('startEditName', 'roundIdx, matchIdx, player'),
        ('saveName', 'roundIdx, matchIdx, player, newName'),
        ('resetBracket', ''),
        ('showContactTooltip', 'event, playerName')
    ]
    
    for func_name, params in functions_to_fix:
        # Pattern 1: window.funcName = function(...) {
        pattern = rf'(window\.{func_name}\s*=\s*function\({re.escape(params)}\)\s*{{)\s*'
        replacement = r'\1\n        if (!isEditModeEnabled) return;\n        '
        content = re.sub(pattern, replacement, content)
        
        # Pattern 2: function funcName(...) {
        pattern = rf'(function {func_name}\({re.escape(params)}\)\s*{{)\s*'
        replacement = r'\1\n        if (!isEditModeEnabled) return;\n        '
        content = re.sub(pattern, replacement, content)
    
    # Restore the applyEditControls function to actually do something
    # Find and replace the stub function
    old_apply_function = r'''// Apply edit controls \(called after bracket renders\)
        function applyEditControls\(\) \{
            // Edit mode is always enabled for all users \(no login required\)
            // This function kept for backward compatibility
            return;
        \}'''
    
    new_apply_function = '''// Apply edit controls (called after bracket renders)
        function applyEditControls() {
            const enabled = isEditModeEnabled;
            
            // Disable/enable player selection
            document.querySelectorAll('.player').forEach(player => {
                if (!player.classList.contains('tbd')) {
                    player.style.pointerEvents = enabled ? 'auto' : 'none';
                    player.style.cursor = enabled ? 'pointer' : 'not-allowed';
                    player.style.opacity = enabled ? '1' : '0.7';
                }
            });
            
            // Disable/enable score inputs
            document.querySelectorAll('.score-input').forEach(input => {
                input.disabled = !enabled;
                input.style.cursor = enabled ? 'text' : 'not-allowed';
                input.style.opacity = enabled ? '1' : '0.6';
            });
            
            // Disable/enable time inputs
            document.querySelectorAll('.match-time input').forEach(input => {
                input.disabled = !enabled;
                input.style.cursor = enabled ? 'text' : 'not-allowed';
                input.style.opacity = enabled ? '1' : '0.6';
            });
            
            // Disable/enable edit buttons
            document.querySelectorAll('.edit-btn').forEach(btn => {
                btn.disabled = !enabled;
                btn.style.display = enabled ? 'inline-block' : 'none';
            });
            
            // Disable/enable reset button
            const resetBtn = document.querySelector('.controls button');
            if (resetBtn) {
                resetBtn.disabled = !enabled;
                resetBtn.style.opacity = enabled ? '1' : '0.5';
                resetBtn.style.cursor = enabled ? 'pointer' : 'not-allowed';
            }
        }'''
    
    content = re.sub(old_apply_function, new_apply_function, content, flags=re.MULTILINE)
    
    # Add applyEditControls() call at the end of renderBracket
    # Find the closing of renderBracket function
    pattern = r'(document\.getElementById\(\'final-section\'\)\.classList\.remove\(\'show\'\);\s*}\s*)(}\s*\n\s*function renderRound)'
    replacement = r'\1applyEditControls();\n        \2'
    content = re.sub(pattern, replacement, content)
    
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
        if restore_permission_checks(file_path):
            updated_count += 1
    
    print("=" * 60)
    print(f"\n✅ Complete! Updated {updated_count} files")
    print("\n📝 Changes made:")
    print("   ✅ Restored permission checks to all edit functions")
    print("   ✅ Restored applyEditControls() functionality")
    print("   ✅ Added applyEditControls() call after renderBracket()")
    print("\n🔐 Access Control:")
    print("   🔒 Non-logged in users → READ-ONLY")
    print("   🔒 Viewer role users → READ-ONLY")
    print("   ✏️  Editor role users → FULL EDIT ACCESS")
    print("   ✏️  Admin role users → FULL EDIT ACCESS")

if __name__ == '__main__':
    main()

