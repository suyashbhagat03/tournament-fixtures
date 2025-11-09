#!/usr/bin/env python3
"""
Update contact loading to be fully async and remove initialContactInfo references.
"""

import re
from pathlib import Path

def update_contact_loading(file_path):
    """Update contact loading to be async without blocking."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Find and replace the loadContactsFromFirebase function
    old_function_pattern = r'''        function loadContactsFromFirebase\(\) \{
            if \(!isFirebaseConfigured \|\| !db\) \{
                // Use initial hardcoded contacts
                contactInfo = initialContactInfo;
                return;
            \}
            
            const contactsRef = ref\(db, `contacts/\$\{SPORT_KEY\}`\);
            
            // Check if contacts exist in Firebase
            get\(contactsRef\)\.then\(\(snapshot\) => \{
                if \(snapshot\.exists\(\)\) \{
                    // Load from Firebase
                    contactInfo = snapshot\.val\(\);
                    console\.log\('✅ Contacts loaded from Firebase'\);
                \} else \{
                    // First time - upload initial contacts to Firebase
                    set\(contactsRef, initialContactInfo\)\.then\(\(\) => \{
                        contactInfo = initialContactInfo;
                        console\.log\('✅ Initial contacts uploaded to Firebase'\);
                    \}\)\.catch\(\(error\) => \{
                        console\.error\('Error uploading contacts:', error\);
                        contactInfo = initialContactInfo;
                    \}\);
                \}
            \}\)\.catch\(\(error\) => \{
                console\.error\('Error loading contacts:', error\);
                contactInfo = initialContactInfo;
            \}\);
        \}'''
    
    new_function = '''        // Load contact information from Firebase asynchronously (non-blocking)
        async function loadContactsFromFirebase() {
            if (!isFirebaseConfigured || !db) {
                console.warn('⚠️ Firebase not configured - contacts unavailable');
                contactsLoading = false;
                return;
            }
            
            try {
                const contactsRef = ref(db, `contacts/${SPORT_KEY}`);
                const snapshot = await get(contactsRef);
                
                if (snapshot.exists()) {
                    contactInfo = snapshot.val();
                    contactsLoading = false;
                    console.log('✅ Contacts loaded from Firebase:', Object.keys(contactInfo).length, 'players');
                } else {
                    console.warn('⚠️ No contacts found in Firebase for', SPORT_KEY);
                    console.log('💡 Use contact_management.html to add contacts');
                    contactsLoading = false;
                }
            } catch (error) {
                console.error('❌ Error loading contacts:', error);
                contactsLoading = false;
            }
        }'''
    
    content = re.sub(old_function_pattern, new_function, content, flags=re.MULTILINE | re.DOTALL)
    
    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✅ Updated {file_path.name}")
        return True
    else:
        print(f"⏭️  No changes for {file_path.name}")
        return False

def main():
    bracket_files = list(Path('.').glob('Bracket_*.html'))
    
    if not bracket_files:
        print("❌ No bracket files found!")
        return
    
    print(f"Found {len(bracket_files)} bracket files")
    print("=" * 60)
    
    updated_count = 0
    for file_path in sorted(bracket_files):
        if update_contact_loading(file_path):
            updated_count += 1
    
    print("=" * 60)
    print(f"\n✅ Complete! Updated {updated_count} files")

if __name__ == '__main__':
    main()
