import sys
import itertools


def dfs_reachable_states(start_state, transitions):
    visited = set()
    stack = [start_state]

    while stack:
        current_state = stack.pop()
        visited.add(current_state)

        for transition in transitions:
            if current_state == transition.split(",")[0]:
                next_state = transitions[transition]
                if next_state not in visited:
                    stack.append(next_state)
    return visited


def recursive_marking(state1, state2, marked_pairs, list_of_states):
    if list_of_states[(state1, state2)] in list_of_states.keys():
        marked_pairs.add((state1, state2))
        marked_pairs.add(list_of_states[(state1, state2)])
        list_of_states.pop((state1, state2))
        recursive_marking(state1, state2, marked_pairs, list_of_states)


def identical_states(unmarked_pairs):
    unique_states = {}
    for pair in unmarked_pairs:  # adding lower state as the key and higher state as the value
        if pair[0] not in unique_states and pair[0] < pair[1]:
            unique_states[pair[0]] = {pair[1]}
        elif pair[0] < pair[1]:
            unique_states[pair[0]].add(pair[1])

        if pair[1] not in unique_states and pair[1] < pair[0]:
            unique_states[pair[1]] = {pair[0]}
        elif pair[1] < pair[0]:
            unique_states[pair[1]].add(pair[0])

    sorted_dict = {key: unique_states[key] for key in sorted(unique_states.keys())}

    return remove_redundant_states(sorted_dict)


def remove_redundant_states(unique_states):
    new_states = {}
    for key in unique_states:
        redundant = set()
        for state in unique_states[key]:
            if state in unique_states:
                redundant.add(state)
        for state in redundant:
            unique_states[key].update(unique_states[state])
            unique_states[state] = set()
        if key not in new_states:
            new_states[key] = unique_states[key]
        if new_states[key] == set():
            new_states.pop(key)
    return new_states


def main():
    input().split(",")
    alphabet = input().split(",")
    acceptable_sets = input().split(",")
    start_state = input()
    transitions = {}
    for line in sys.stdin:
        line = line.split("->")
        transitions[line[0]] = line[1].strip()

    set_of_states = list(dfs_reachable_states(start_state, transitions))  # all reachable states
    set_of_states.sort()

    for key in list(transitions.keys()):
        if key.split(",")[0] not in set_of_states:  # remove unreachable transitions
            transitions.pop(key)
            if key.split(",")[0] in acceptable_sets:  # remove unreachable acceptable states
                acceptable_sets.remove(key.split(",")[0])

    different_acceptance_pairs = set()

    for index, state1 in enumerate(set_of_states):  # find all pairs of states with different acceptances
        for state2 in set_of_states[index + 1:]:
            if (state1 in acceptable_sets) != (state2 in acceptable_sets):
                different_acceptance_pairs.add(tuple(sorted((state1, state2))))

    list_of_states = {}  # list (dict) we use for recursive marking

    for index, state1 in enumerate(set_of_states):
        for state2 in set_of_states[index + 1:]:
            if (tuple(sorted((state1, state2)))) in different_acceptance_pairs:
                continue
            for symbol in alphabet:
                key1 = state1 + "," + symbol
                key2 = state2 + "," + symbol
                # transition states pair is marked
                if (tuple(sorted((transitions[key1], transitions[key2])))) in different_acceptance_pairs:
                    different_acceptance_pairs.add((state1, state2))  # mark the pair

                    if (state1, state2) in list_of_states.keys():  # if we mark the pair that was unmarked before
                        different_acceptance_pairs.add(list_of_states[(state1, state2)])  # mark the pair
                        recursive_marking(state1, state2, different_acceptance_pairs, list_of_states)
                        list_of_states.pop((state1, state2))  # remove it from the list

                elif transitions[key1] != transitions[key2]:
                    list_of_states[(transitions[key1], transitions[key2])] = (state1, state2)

    all_pairs = set(itertools.combinations(set_of_states, 2))   # all possible pairs of states
    # all pairs \ marked pairs = unmarked pairs
    unique_states = identical_states(set(all_pairs) - different_acceptance_pairs)  # remove redundant states

    output = ""
    for state in set_of_states:
        for values in unique_states.values():
            if state in values:
                break
        else:
            output += state + "," if state != set_of_states[-1] else state
    set_of_states = output.strip(",").split(",")  # remove redundant states from set of states
    output = ""
    print(",".join(set_of_states))
    print(",".join(alphabet))

    if len(acceptable_sets) == 0:
        print("")
    else:
        for state in acceptable_sets:
            if state in set_of_states:
                output += state + "," if state != acceptable_sets[-1] else state
        print(output.strip(","))

    if start_state in set_of_states:
        print(start_state)
    else:
        for key in unique_states:
            if start_state in unique_states[key]:
                print(key)
                break

    for transition in transitions:
        if transition.split(",")[0] in set_of_states:
            if transitions[transition] in set_of_states:  # if transition leads to a state that is not redundant
                print(f"{transition}->{transitions[transition]}")
            else:
                for key in unique_states:
                    if transitions[transition] in unique_states[key]:
                        print(f"{transition}->{key}")  # print transition to the non-redundant state
                        break


if __name__ == "__main__":
    main()