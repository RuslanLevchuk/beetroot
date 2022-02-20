
def Remove(tuples):
    tuples = [t for t in tuples if t]
    return tuples

tuples = [(), ('ram'), (), ('laxman', 'sita'),
('krishna', 'akbar', '45'), ('', ''), ()]
print(Remove(tuples))
