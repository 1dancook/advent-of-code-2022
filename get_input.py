# don't know if there would be two different 
# types of data for one day or not
def get_input(day, folder="input", strip=True):
    try:
        with open(f"{folder}/{day}.txt", "r") as f:
            return f.read().strip() if strip else f.read()
    except:
        return ""

def get_sample_input(day, strip=True):
    return get_input(day, folder="sample_input", strip=strip)

def sample_as_lines(day):
    data = get_input(day, folder="sample_input")
    return [x.strip() for x in data.splitlines()]

def data_as_lines(day):
    data = get_input(day)
    return [x.strip() for x in data.splitlines()]

