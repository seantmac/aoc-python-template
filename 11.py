class Seat:
    def __init__(self):
        self.filled = False
        self.buffer = False
        self.adjacent_seats = set()
        self.line_of_sight_seats = set()

    def buffer_seat(self, p1=True):
        filled_count = [s.filled for s in (self.adjacent_seats if p1 else self.line_of_sight_seats)].count(True)
        if self.filled:
            if filled_count >= (4 if p1 else 5):
                self.buffer = False
            else:
                self.buffer = self.filled
        else:
            if filled_count == 0:
                self.buffer = True
            else:
                self.buffer = self.filled

    def commit(self):
        if self.filled != self.buffer:
            self.filled = self.buffer


def update(p1=True):
    for s in seats.values():
        s.buffer_seat(p1=p1)
    for s in seats.values():
        s.commit()


def go(p1=True):
    for s in seats.values():
        s.filled = False

    prev_count = [s.filled for s in seats.values()].count(True)
    update(p1=p1)
    new_count = [s.filled for s in seats.values()].count(True)
    while prev_count != new_count:
        prev_count = new_count
        update(p1=p1)
        new_count = [s.filled for s in seats.values()].count(True)
    return prev_count


seats = {}
for j, line in enumerate(open('11.txt')):
    for i, char in enumerate(line):
        if char == 'L':
            seats[complex(i, j)] = Seat()

max_real = max([int(location.real) for location in seats.keys()])
max_imag = max([int(location.imag) for location in seats.keys()])
for location, seat in seats.items():
    for loc in [1j, 1+1j, 1, -1j, -1-1j, -1, 1-1j, -1+1j]:
        for i in range(1, max([max_real, max_imag])):
            los_loc = location + loc*i
            if any([los_loc.real < 0, los_loc.real > max_real, los_loc.imag < 0, los_loc.imag > max_imag]):
                break
            if los_loc in seats.keys():
                if i == 1:
                    seats[los_loc].adjacent_seats.add(seat)
                    seat.adjacent_seats.add(seats[los_loc])
                seat.line_of_sight_seats.add(seats[los_loc])
                seats[los_loc].line_of_sight_seats.add(seat)
                break

print(f"Part 1 Answer: {go(p1=True)}")
print(f"Part 2 Answer: {go(p1=False)}")

##  Part 1 Answer: 2354
##  Part 2 Answer: 2072



####    AOC 2020 Day 11
####    Part 1 Answer: 2354
####    Part 2 Answer: 2072
####    Loaded puzzle input from 11.txt