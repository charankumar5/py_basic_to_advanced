# const variable.
EXPECTED_BAKE_TIME = 40
PREP_TIME = 2
def bake_time_remaining(elapsed_bake_time):


    return EXPECTED_BAKE_TIME - elapsed_bake_time

def preparation_time_in_minutes(number_of_layers):
    return number_of_layers*PREP_TIME

def elapsed_time_in_minutes(number_of_layers,elapsed_bake_time):
    return preparation_time_in_minutes(number_of_layers)+elapsed_bake_time
    
def main():
    print(bake_time_remaining(30))
    print(preparation_time_in_minutes(2))
    print(elapsed_time_in_minutes(3,20))
    return 0

if __name__ == "__main__":
    main()