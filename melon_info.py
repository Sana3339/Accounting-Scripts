"""Print out all the melons in our inventory."""

from melons import melons

def print_melon(melons):
    """Print each melon with corresponding attribute information."""

    for key,value in melons.items():
        print(key.upper())

        for value, inner_value in value.items():
            print(f"{value}: {inner_value}")
            
        print()
        
print_melon(melons)
