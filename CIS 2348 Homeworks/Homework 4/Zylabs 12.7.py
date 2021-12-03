def get_age():
    age=int(input())
    if(age>=18 and age<=75):
        return age
    else:
        raise ValueError("Could not calculate heart rate info.\n")
    
def fat_burning_heart_rate(age):
    return (0.7*(220-age))
if __name__=="__main__":
    try:
        age = get_age()
        
        rate = fat_burning_heart_rate(age)
        print("Fat burning heart rate for a "+str(age)+" year-old: "+str(rate)+" bpm")
    except Exception as ex:
        print("Invalid age.")
        print(ex)
        