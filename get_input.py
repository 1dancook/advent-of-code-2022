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

def sample_as_lines(day):
    data = get_input(day, folder="sample_input")
    return [x for x in data.splitlines()]

def data_as_lines(day):
    data = get_input(day)
    return [x for x in data.splitlines()]

