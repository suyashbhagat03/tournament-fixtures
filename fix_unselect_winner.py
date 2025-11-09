import re

bracket_files = [
    'Bracket_Chess.html',
    'Bracket_TableTennis_Singles.html',
    'Bracket_TableTennis_Doubles.html',
    'Bracket_Carrom_Singles.html',
    'Bracket_Carrom_Doubles.html',
    'Bracket_Foosball.html',
    'Bracket_Snooker.html',
    'Bracket_FIFA25.html'
]

for filename in bracket_files:
    print(f"Fixing {filename}...")
    
    with open(filename, 'r') as f:
        content = f.read()
    
    # Find and replace the selectWinner function to also clear player names
    old_logic = r'''            if \(match\.winner === selected\) {
                match\.winner = null;
                for \(let i = roundIdx \+ 1; i < totalRounds; i\+\+\) {
                    allRoundsData\[i\]\.forEach\(m => { m\.winner = null; m\.score1 = ''; m\.score2 = ''; }\);
                }
            }'''
    
    new_logic = '''            if (match.winner === selected) {
                match.winner = null;
                // Clear subsequent rounds (winners, scores, and player names)
                for (let i = roundIdx + 1; i < totalRounds; i++) {
                    allRoundsData[i].forEach(m => { 
                        m.winner = null; 
                        m.score1 = ''; 
                        m.score2 = ''; 
                        m.player1 = 'TBD'; 
                        m.player2 = 'TBD';
                        m.manuallyEditedP1 = false;
                        m.manuallyEditedP2 = false;
                    });
                }
            }'''
    
    content = re.sub(old_logic, new_logic, content)
    
    with open(filename, 'w') as f:
        f.write(content)
    
    print(f"✅ Fixed {filename}")

print("\n✅ All bracket files updated to clear player names when winner is unselected!")
