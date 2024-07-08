# V0

### Game loops

##### Shuffle

Shuffle an unshuffled deck into a random order

Potential Implementation:
- Mark cards 1-52, Randomize list of numbers, Initialize deck with that order

#### Deal

Deal cards to the players

~The host starts as the "Dealer"~
- Randomly assign a card from the top of the deck to each player, player with highest card value is the "Dealer"
- Winner of previous game is the new Dealer
- Give a card to each player from the top of the shuffled deck going clockwise starting with dealer
- Stop when dealer has 15 cards, every other player should have 14

#### Turns

- Player picks up card from card pile or discard pile
  - if the player picks up from the discard pile then they must use that card in their current turn for a meld
- Plays a meld if possible, or can choose not to
- Can choose to annouce possession of Joker in their card
- Discards a care into the discard pile to end their turn

#### Round End

- If the dicard card at the end of the players turn is the last card in that players hand then the will game end and that player "wins" the round
- Total up the points for the cards left in each player's hand and add it to each players total

#### Game End

- When Round End state occurs and it is the 9th round, or the number of rounds set
- The score for each player, for each round will be displayed before displaying the total
ex:

| players | round 1 | round 2| etc | total |
| :---: | :---: | :---: | :---: | :---: |
| p1 | score # | score # | etc | ## |
| p2 | score # | score # | etc | ## |  

### Acquiring points
The user described 3 conditions or "Melds" to acquire points
- A Set which is when a player obtains 3 or 4 of the same card in different suits, "3/4 of a kind"
- A Run which is when a player abtains a sequence of cards of consecutive ranks, "Straight"
  - Aces are player both low, below 2, and high, above King
  - it cannot be played both low and high at the same time, "Around the world"
- A Layoff which is when a player can player a card on top of another players Set or Run that has already been layed down, "Rummy"
  - Adding the fourth card to a Set to complete a 4 of a kind
  - Adding a card to a staight or run that is one above or one below the current ending of the sequence
  
### Scoring

`Rule of 51 Research Needed`

- Whoever ends the round gets -25 points, typically marked as an X in the score sheet
- Players with no melds automatically recieve 100 points regardless of current cards in hand
- Players with meld count the number of points left in their hand 
  - Cards 2 though 9 are worth their face value, 2=2 5=5 9=9
  - Face Cards are all worth 10
  - Aces are worth 10
  - Announced jokers are worth 2
  - Unannouced joekers are worth 25

### Cards

`Research Needed`

enums:
- Needs card name
- card id value for shuffling
- card value 
- card suit

### Tournament style

- 12 to 16 players divided into 3-4 groups
- each group players 3 to 4 games
- winners advance to player eachother

