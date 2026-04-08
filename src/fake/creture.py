from model.creture import Creature


# fake data, until we use a real database and SQL
_creatures = [
    Creature(
        name= 'Yeti',
        aka= 'Abominable Snowman',
        country= 'CN',
        area= 'Himalaya',
        description= 'Hirsute Hmalayan'
    ),
    Creature(
        name= 'Bigfoot',
        aka= "Yeti's Cousin Eddie",
        country= 'US',
        area= '*',
        description= 'Sasquatch'
    ),
]

def get_all() -> list[Creature]:
    """Return all explorers"""
    return _creatures

def get_one(name: str) -> Creature | None:
    """Return one explorer"""
    for _creature in _creatures:
        if _creature.name == name:
            return _creature
    return None

# The following are nonfunctional for now,
# so they just act like they work, without modifying
# the actual fake _creatures list:
def create(creature: Creature) -> Creature:
    """Add an creature"""
    return creature

def modify(creature: Creature) -> Creature:
    """Partially modify an creature"""
    return creature

def replace(creature: Creature) -> Creature:
    """Completely replace an creature"""
    return creature

def delete(name: str) -> bool:
    """Delete an creature; return None if it existed"""
    return None
