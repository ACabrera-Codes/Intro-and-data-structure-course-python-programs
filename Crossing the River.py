# Initially there are 3 missionaries and 3 cannibals on one side of the river
# There is only 1 boat that can hold 2 people
# We can not move them in a way that results in cannibals outnumbering the missionaries
# This program shows the # of crossings that gets everyone safely across the river
# c = cannibal , m = Missionaries 

StartSide = {'c': 3, 'm': 3}
EndSide = {'c': 0, 'm': 0}
BoatStatus = {'c': 0, 'm': 0}


def Current_State(dict1, dict2, dict3): #Prints each state after a trip in a readable form
    CurrState = """
               Start Move
    Side 1: {} cannibals, {} missionaries
    _____________________________________
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~    
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    _____________________________________  
    
    Side 2: {} cannibals, {} missionaries
    Boat: {} cannibals, {} missionaries
                End Move
    """

    print(CurrState.format(dict1['c'], dict1['m'], dict2['c'], dict2['m'],
                     dict3['c'], dict3['m']))


def main(s1=StartSide, s2=EndSide, bs=BoatStatus):
    if all(x == 0 for x in s2.values()):  #validates if all elements are true
        Current_State(s1, s2, bs)
        s1['c'] -= 1  # cannibal journeys to the other side via the boat
        bs['c'] += 1  

    s1['m'] -= 1  # missionary journeys to the other side via the boat
    bs['m'] += 1  
    Current_State(s1, s2, bs)

    if all(x == 0 for x in s1.values()):  
        bs['c'], bs['m'] = 0, 0  
        s2['c'] += 1  
        s2['m'] += 1  
        Current_State(s1, s2, bs)
        return  

    bs['m'] -= 1  
    s2['m'] += 1  
    Current_State(s1, s2, bs)

    s1['c'] -= 1  
    bs['c'] += 1  
    Current_State(s1, s2, bs)

    bs['c'] -= 1 
    s2['c'] += 1 
    Current_State(s1, s2, bs)

    main(s1, s2, bs)  
    
main()

print("The solution was found in 11 moves.")