import copy

with open('Input5.txt') as f:
    input = f.read().splitlines()

for i in range(len(input)):
    if input[i] == '':
        stacks = input[:i-1]
        moves = input[i+1:]
        break

stackOverview = [None] * len(stacks[-1].split(' '))
stacks.reverse()
for stack in stacks:
    stackSplit = [stack[i+1] for i in range(0, len(stack), 4)]
    for j in range(len(stackSplit)):
        if stackOverview[j] is None:
            stackOverview[j] = [stackSplit[j]]
        elif stackSplit[j] != ' ':
            stackOverview[j].append(stackSplit[j])
        else:
            continue

originalStacks = copy.deepcopy(stackOverview)

for move in moves:
    moveSplit = move.split(' ')
    amount = int(moveSplit[1])
    source = int(moveSplit[3]) - 1
    target = int(moveSplit[5]) - 1
    movedStack = originalStacks[source][len(originalStacks[source])-amount:]
    for stack in movedStack:
        originalStacks[target].append(stack)
        originalStacks[source].pop()
    for crate in range(amount):
        stackOverview[target].append(stackOverview[source][-1])
        stackOverview[source].pop()

answer1 = ''
answer2 = ''
for stack in stackOverview:
    answer1 += stack[-1]
for stack in originalStacks:
    answer2 += stack[-1]
print(answer1)
print(answer2)