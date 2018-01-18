function electionWinner(votes) {
    var countOfVotes = votes[0];
    votes = votes.slice(1);
    // First Sort
    votes.sort();
    // Second count the votes for each person
    var countedNames = votes.reduce(function (allNames, name, currentIndex) { 
        if (name in allNames) {
            allNames[name]++;
        }
        else {
            allNames[name] = 1;
        }
        return allNames;
    }, {});
    // Find the Max
    var winningVotes = Object.values(countedNames).reduce( ( max, cur ) => Math.max( max, cur ), 0 );
    var winnersCircle = [];
    // Find all electors that have the max votes
    for (var winner in countedNames) {
        if (countedNames[winner] == winningVotes) {
            winnersCircle.push(winner);
        }
    }
    // Return the last person in that array
    return winnersCircle[winnersCircle.length - 1];
}
    
    console.log(electionWinner([10,"Alex","Micheal","Harry","Dave","Micheal","Victor","Harry","Alex","Mary","Mary"]))