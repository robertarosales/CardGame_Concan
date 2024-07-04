# V1

### Game loops

##### Shuffle

Shuffle an unshuffled deck into a random order.

Potential Implementations:
- Mark cards 1-52, Randomize list of numbers, Initialize deck with that order

#### Deal

~The host starts as the "Dealer"~

Randomly assign a card from the top of the deck to each player, player with highest card value is the "Dealer"

Winner of previous game is the new Dealer

Give a card to each player from the top of the shuffled deck going clockwise starting with dealer

Stop when dealer has 15 cards, every other player should have 14

#### Turns

Player picks up card from card pile or discard pile

Plays a meld if possible, or can choose not to

Discards a care into the discard pile to end their turn

#### Round End

If the dicard card at the end of the players turn is the last card in that players hand then the game end and that player "wins"

Total up the points for the cards left in each player's hand and add it to each players total

#### Game End

When Round End state occurs and it is the 9th round, or the number of rounds set, then the game will not reset but display the points for each player with the option to play again or return to menu

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

Cards 2 though 10 are worth their face value, 2=2 5=5 10=10
Face Cards are all worth 10
Aces played High and Aces not played are worth 10
Aces player Low are worth 1
Jokers are worth the card they replace

### Cards
