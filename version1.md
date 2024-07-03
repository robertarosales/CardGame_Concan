# V1

### Game Cycle

The user requires 4 different game stages.

The shuffle and deal stages can be combined into a game setup stage

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

The players have few options when it becomes there turn:


#### Game End


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
