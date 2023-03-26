running = 29
swimming = 25
cycling = 34



def calcuate_total_time(running, swimming, cycling):
    total_time = running + cycling + swimming 
    return total_time

def determine_award(total_time):
    if total_time <= 100:
        return "provincial colours"
    elif total_time <= 105:
        return "half colours"
    elif total_time <= 110:
        return "provincial scroll"
    else:
        "no award"

        

    print("Total time:", total_time)

    award = determine_award(total_time)
    print("Award:", award)