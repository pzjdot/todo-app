def parse(feet_inch):
    parts = feet_inch.split()
    feet = float(parts[0])
    inch = float(parts[1])
    return {"feet": feet, "inch": inch}
