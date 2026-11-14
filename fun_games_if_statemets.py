# Each year for a human is like 7.18 years for a dog
DOG_YRS_MULTIPLIER = 7.18  

def main():
    calender_year =float(input("Enter an age in calendar years:"))
    dog_year = calender_year*DOG_YRS_MULTIPLIER
    dog_year =round(dog_year,2)
    print(f"That's {dog_year} in dog years!")
    pass

if __name__ == '__main__':
    main()