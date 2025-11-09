import re

# Read all bracket files
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
    
    # Find and replace the buildBracketTree function
    old_function = r'''        function buildBracketTree\(\) {
            for \(let roundIdx = 1; roundIdx < totalRounds; roundIdx\+\+\) {
                const matchesInThisRound = bracketSize / Math\.pow\(2, roundIdx \+ 1\);
                if \(\!allRoundsData\[roundIdx\] \|\| allRoundsData\[roundIdx\]\.length !== matchesInThisRound\) {
                    allRoundsData\[roundIdx\] = \[\];
                    for \(let i = 0; i < matchesInThisRound; i\+\+\) {
                        allRoundsData\[roundIdx\]\.push\({ player1: 'TBD', player2: 'TBD', winner: null, score1: '', score2: '', time: '', matchId: i, isByeMatch: false }\);
                    }
                }
                for \(let matchIdx = 0; matchIdx < matchesInThisRound; matchIdx\+\+\) {
                    const match = allRoundsData\[roundIdx\]\[matchIdx\];
                    if \(roundIdx === 1\) {
                        const r2slots = \[\];
                        for \(let i = 0; i < allRoundsData\[0\]\.length; i\+\+\) r2slots\.push\(allRoundsData\[0\]\[i\]\.winner \|\| 'TBD'\);
                        byePlayers\.forEach\(p => r2slots\.push\(p\)\);
                        match\.player1 = r2slots\[matchIdx \* 2\] \|\| 'TBD';
                        match\.player2 = r2slots\[matchIdx \* 2 \+ 1\] \|\| 'TBD';
                    } else {
                        const prevRound = allRoundsData\[roundIdx - 1\];
                        match\.player1 = prevRound\[matchIdx \* 2\]\?\.winner \|\| 'TBD';
                        match\.player2 = prevRound\[matchIdx \* 2 \+ 1\]\?\.winner \|\| 'TBD';
                    }
                }
            }
        }'''
    
    new_function = '''        function buildBracketTree() {
            for (let roundIdx = 1; roundIdx < totalRounds; roundIdx++) {
                const matchesInThisRound = bracketSize / Math.pow(2, roundIdx + 1);
                if (!allRoundsData[roundIdx] || allRoundsData[roundIdx].length !== matchesInThisRound) {
                    allRoundsData[roundIdx] = [];
                    for (let i = 0; i < matchesInThisRound; i++) {
                        allRoundsData[roundIdx].push({ player1: 'TBD', player2: 'TBD', winner: null, score1: '', score2: '', time: '', matchId: i, isByeMatch: false });
                    }
                }
                for (let matchIdx = 0; matchIdx < matchesInThisRound; matchIdx++) {
                    const match = allRoundsData[roundIdx][matchIdx];
                    
                    // Only update player names if they are currently TBD or if winner has changed
                    let newPlayer1, newPlayer2;
                    
                    if (roundIdx === 1) {
                        const r2slots = [];
                        for (let i = 0; i < allRoundsData[0].length; i++) r2slots.push(allRoundsData[0][i].winner || 'TBD');
                        byePlayers.forEach(p => r2slots.push(p));
                        newPlayer1 = r2slots[matchIdx * 2] || 'TBD';
                        newPlayer2 = r2slots[matchIdx * 2 + 1] || 'TBD';
                    } else {
                        const prevRound = allRoundsData[roundIdx - 1];
                        newPlayer1 = prevRound[matchIdx * 2]?.winner || 'TBD';
                        newPlayer2 = prevRound[matchIdx * 2 + 1]?.winner || 'TBD';
                    }
                    
                    // Only update if TBD or if the new player is different and coming from a winner
                    if (match.player1 === 'TBD' || (newPlayer1 !== 'TBD' && match.player1 !== newPlayer1)) {
                        match.player1 = newPlayer1;
                    }
                    if (match.player2 === 'TBD' || (newPlayer2 !== 'TBD' && match.player2 !== newPlayer2)) {
                        match.player2 = newPlayer2;
                    }
                }
            }
        }'''
    
    # Replace the function
    content = re.sub(old_function, new_function, content)
    
    with open(filename, 'w') as f:
        f.write(content)
    
    print(f"✅ Fixed {filename}")

print("\n✅ All bracket files updated!")
