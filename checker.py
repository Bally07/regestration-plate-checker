numberplate=str
def main():
        plate=input("Enter the number plate:")
        if is_valid_numberplate(plate):
            print("Valid number plate")
        else:
            print("Invalid number plate")
def is_valid_numberplate(plate:numberplate)->bool:
    if len(plate)==8:
        if splitplate(plate):
            return True
        else:
            return False
    else:
        return False
    
def splitplate(plate:numberplate)->str:
        p1 = checkdvlaMemoryTag(part1=plate[0:2])
        p2 = checkYearTag(part2=plate[2:4])
        p3 = checkRandomTag(part3=plate[4:8])
        if p1 and p2 and p3:
            return True
        else:
            return False
def checkdvlaMemoryTag(plate:numberplate)->bool:
    dvlaMemoryTag=["AB","CD","EF"]
    if plate in dvlaMemoryTag:
        return True
    else:
        return False
def checkYearTag(plate:numberplate)->bool:
    
    if plate() in range(02,25):
        return True
    else:
        return False
def checkRandomTag(plate:numberplate)->bool:
        if plate.isalpha():
            return True
        else:
            return False
def getfromdatabase()->list:

