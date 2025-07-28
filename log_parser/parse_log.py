with open("sample.log", "r") as file:
    for line in file:
        if "ERROR" in line or "WARN" in line:
            print(line.strip())
