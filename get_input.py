# don't know if there would be two different 
# types of data for one day or not
def get_input(day, folder="input"):
    try:
        with open(f"{folder}/{day}.txt", "r") as f:
            return f.read().strip()
    except:
        return ""

def get_sample_input(day):
    return get_input(day, folder="sample_input")
