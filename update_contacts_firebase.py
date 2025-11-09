#!/usr/bin/env python3
"""
Update bracket files to load contact info from Firebase instead of using hardcoded data.
"""

import re
from pathlib import Path

def update_bracket_for_firebase_contacts(file_path):
    """Update bracket file to load contacts from Firebase."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Find the contactInfo line
    contact_pattern = r'(\s+)(const contactInfo = \{[^}]+\};)'
    
    match = re.search(contact_pattern, content, re.DOTALL)
    if not match:
        print(f"⚠️  Could not find contactInfo in {file_path.name}")
        return False
    
    indent = match.group(1)
    old_contact_line = match.group(2)
    
    # Replace with Firebase-loading version
    new_code = f'''{indent}// Contact info - loaded from Firebase
{indent}const initialContactInfo = {old_contact_line}
{indent}let contactInfo = {{}};  // Will be loaded from Firebase'''
    
    content = content.replace(indent + old_contact_line, new_code)
    
    # Now add Firebase contact loading code after loadFromFirebase function
    # Find loadFromFirebase function
    load_firebase_pattern = r'(function loadFromFirebase\(\) \{[^}]+\})\s*\n'
    
    firebase_contact_code = '''
        
        // Load contact information from Firebase
        function loadContactsFromFirebase() {
            if (!isFirebaseConfigured || !db) {
                // Use initial hardcoded contacts
                contactInfo = initialContactInfo;
                return;
            }
            
            const contactsRef = ref(db, `contacts/${SPORT_KEY}`);
            
            // Check if contacts exist in Firebase
            get(contactsRef).then((snapshot) => {
                if (snapshot.exists()) {
                    // Load from Firebase
                    contactInfo = snapshot.val();
                    console.log('✅ Contacts loaded from Firebase');
                } else {
                    // First time - upload initial contacts to Firebase
                    set(contactsRef, initialContactInfo).then(() => {
                        contactInfo = initialContactInfo;
                        console.log('✅ Initial contacts uploaded to Firebase');
                    }).catch((error) => {
                        console.error('Error uploading contacts:', error);
                        contactInfo = initialContactInfo;
                    });
                }
            }).catch((error) => {
                console.error('Error loading contacts:', error);
                contactInfo = initialContactInfo;
            });
        }
        
        // Load contacts on page load
        loadContactsFromFirebase();
'''
    
    # Find where to insert (after loadFromFirebase function)
    load_match = re.search(load_firebase_pattern, content, re.DOTALL)
    if load_match:
        insert_pos = load_match.end()
        content = content[:insert_pos] + firebase_contact_code + content[insert_pos:]
    else:
        print(f"⚠️  Could not find loadFromFirebase in {file_path.name}")
        return False
    
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
        if update_bracket_for_firebase_contacts(file_path):
            updated_count += 1
    
    print("=" * 60)
    print(f"\n✅ Complete! Updated {updated_count} files")
    print("\n📝 Changes made:")
    print("   ✅ Contacts now load from Firebase")
    print("   ✅ Initial contacts uploaded to Firebase on first load")
    print("   ✅ Contact info can be updated via contact_management.html")
    print("\n📞 Contact Management:")
    print("   Open contact_management.html to update player contacts")

if __name__ == '__main__':
    main()

