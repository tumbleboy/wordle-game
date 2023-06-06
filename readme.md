# Wordle Game
### Rules
- Players must guess the 5-letter word in 6 total guesses.
- Only 5-letter words are accepted and words that are in the word bank.
    - If you input an invalid guess, this will not use up an attempt.
### Useful commands 
- `/quit` - end the program.
- `/giveup` - reveal the answer and end the run.
- `/help` - displays helpful information.
### Entire program flowchart
```mermaid
 flowchart LR
    A([Start]) --> D[Greeting message]
    D --> B[[Get target word]]
    B --> E[[Prompt for guess]]
    E --> |/help| Z[Display help message]
    Z --> E
    E --> |/quit| M
    E --> F{Is it valid?}
    F --> |YES| G[[Score guess]]
    F --> |NO| H[Invalid guess message]
    H --> E
    G --> I{Was the word <br/> guessed correctly?}
    I --> |NO| K{Are there still <br/> attempts left?}
    I --> |YES| J[Victory message]
    K --> |YES| E
    K --> |NO| L[Defeat message]
    J --> C[[Play again?]]
    L --> C
    C --> |NO|M([End program])
    C --> |YES|A
```
### Score Guess Algorithm
```mermaid

flowchart LR
    Start --> A
    A[/Get user word and target word/] --> B{"for index_value in range(len(user_word))"}
    B --> C{"Is user_word[index_value] == \ntarget_word[index_value]"}
    C --> |True| D["result[index_value] = 2"] --> Z
    C --> |False| E{"is user_word[index_value] <br/> in target_word?"}
    E --> |True| F["result[index_value] = 1"] --> Z
    E --> |False| G["result[index_value] = 0"] --> Z
    Z{"end of loop?"} --> |False| B
    Z --> |True| Y[/"print(result)"/] --> X
    X[End]
```

