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
    
    # Step 1: Add manuallyEdited flag to match object initialization
    # Find the line where matches are created and add the flag
    content = re.sub(
        r"(allRoundsData\[roundIdx\]\.push\({ player1: 'TBD', player2: 'TBD', winner: null, score1: '', score2: '', time: '', matchId: i, isByeMatch: false )\}",
        r"\1, manuallyEditedP1: false, manuallyEditedP2: false }",
        content
    )
    
    # Step 2: Modify buildBracketTree to check the flag
    old_update_logic = r'''                    // Only update if TBD or if the new player is different and coming from a winner
                    if \(match\.player1 === 'TBD' \|\| \(newPlayer1 !== 'TBD' && match\.player1 !== newPlayer1\)\) {
                        match\.player1 = newPlayer1;
                    }
                    if \(match\.player2 === 'TBD' \|\| \(newPlayer2 !== 'TBD' && match\.player2 !== newPlayer2\)\) {
                        match\.player2 = newPlayer2;
                    }'''
    
    new_update_logic = '''                    // Only update if not manually edited and (TBD or different winner)
                    if (!match.manuallyEditedP1 && (match.player1 === 'TBD' || (newPlayer1 !== 'TBD' && match.player1 !== newPlayer1))) {
                        match.player1 = newPlayer1;
                    }
                    if (!match.manuallyEditedP2 && (match.player2 === 'TBD' || (newPlayer2 !== 'TBD' && match.player2 !== newPlayer2))) {
                        match.player2 = newPlayer2;
                    }'''
    
    content = re.sub(old_update_logic, new_update_logic, content)
    
    # Step 3: Update saveName function to set the manuallyEdited flag
    old_savename = r'''        window\.saveName = function\(roundIdx, matchIdx, player, newName, event\) {
        if \(\!isEditModeEnabled\) return;
        // Check edit permission
            event\.stopPropagation\(\);
            if \(newName\.trim\(\)\) {
                const match = allRoundsData\[roundIdx\]\[matchIdx\];
                const old = match\[player\];
                match\[player\] = newName\.trim\(\);
                if \(match\.winner === old\) match\.winner = newName\.trim\(\);
            }
            editingState = { roundIdx: null, matchIdx: null, player: null };
            saveToFirebase\(\);
            renderBracket\(\);
        };'''
    
    new_savename = '''        window.saveName = function(roundIdx, matchIdx, player, newName, event) {
        if (!isEditModeEnabled) return;
        // Check edit permission
            event.stopPropagation();
            if (newName.trim()) {
                const match = allRoundsData[roundIdx][matchIdx];
                const old = match[player];
                match[player] = newName.trim();
                if (match.winner === old) match.winner = newName.trim();
                // Mark as manually edited
                if (player === 'player1') match.manuallyEditedP1 = true;
                if (player === 'player2') match.manuallyEditedP2 = true;
            }
            editingState = { roundIdx: null, matchIdx: null, player: null };
            saveToFirebase();
            renderBracket();
        };'''
    
    content = re.sub(old_savename, new_savename, content, flags=re.DOTALL)
    
    with open(filename, 'w') as f:
        f.write(content)
    
    print(f"✅ Fixed {filename}")

print("\n✅ All bracket files updated with manual edit tracking!")
