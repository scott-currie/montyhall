import random

def main():
    trials = int(input('How many trials?').strip())
    sw_wins, st_wins = 0, 0
    for t in range(trials):
        sw_wins += play_game(True)
        st_wins += play_game(False)
    print('switching % wins = ', sw_wins / trials)
    print('standing % wins = ', st_wins / trials)

def play_game(switch):
    '''
    :param switch: Should player switch his choice?
    :return: 1 if player won, else 0
    '''
    # Make prizes then shuffle. Doors are referenced by index.
    prizes = [0, 0, 1]
    random.shuffle(prizes)

    # p_choice is chosen completely randomly.
    p_choice = random.choice(range(3))

    # elim is the door Monty will eliminate. Selected randomly from the 2 doors player didn't choose, but only if the
    # door is a dud. Monty never removes the prize door.
    elim = random.choice([i for i in range(len(prizes)) if i != p_choice and prizes[i] == 0])

    # If player is programmed to switch doors.
    if switch:
        # This expression happens to return a single-item list that I'm slicing at [0]. p_choice becomes the door that
        # he didn't originally choose and that Monty hasn't eliminated.
        p_choice = [c for c in range(len(prizes)) if c != p_choice and c != elim][0]

    if prizes[p_choice]:
        return 1
    else:
        return 0

if __name__ == "__main__":
    main()