#!/usr/bin/python
from bs4 import BeautifulSoup
import requests, sys

if __name__ == '__main__':
    if sys.argv[1] == "AustralianShepards":
        shepardDogHumane = "https://www.utahhumane.org/adopt?f%5B0%5D=field_species%3A3&f%5B1%5D=field_primary_breed%3A63"
        shepardDogBestFriends = "https://bestfriends.org/adopt/adopt-our-sanctuary/dogs?field_animal_primary_breed_tid_selective=2991&field_animal_secondary_breed_tid_selective=All&field_animal_age_value_selective=All&field_animal_size_value_selective=All&field_animal_color_tid_selective=All&field_animal_sex_value_selective=All&title="
        shepardNuzzlesAndCo = "https://nuzzlesandco.org/adopt-a-pet/?species%5B%5D=Dog&gender%5B%5D&age_group%5B%5D&size%5B%5D&breed%5B%5D=Australian+Shepherd&wpv_post_id=969&wpv_view_count=855-CPID969&wpv_paged=1"

        print("-----------------Australian Shepards----------------")
        humaneReq = requests.get(shepardDogHumane)
        humaneData = humaneReq.text
        soup = BeautifulSoup(humaneData, "html.parser")
        humaneDogCount = len(soup.find_all('div', class_="item"))
        numDogString = str(humaneDogCount)
        print("Humane Society: " + numDogString)
        print(shepardDogHumane)

        print("------------------------------------------------------------")
        bfReq = requests.get(shepardDogBestFriends)
        bfData = bfReq.text
        soup = BeautifulSoup(bfData, "html.parser")
        bfDogCount = len(soup.find_all('div', class_="rg-animal"))
        eachDogStr = str(bfDogCount)
        print("Best Friends: " + eachDogStr)
        print(shepardDogBestFriends)

        print("------------------------------------------------------------")
        nuzzlesReq = requests.get(shepardNuzzlesAndCo)
        nuzzlesData = nuzzlesReq.text
        soup = BeautifulSoup(nuzzlesData, "html.parser")
        nuzzlesDogCount = len(soup.find_all('div', class_="pet-result-img"))
        strNuzz = str(nuzzlesDogCount)
        print("Nuzzles And Co: " + strNuzz)
        print(shepardNuzzlesAndCo)

        print("------------------------------------------------------------")
        totalNumDogs = humaneDogCount + bfDogCount + nuzzlesDogCount
        totalNumDogsStr = str(totalNumDogs)
        print("Total Number Available: " + totalNumDogsStr)
    elif sys.argv[1] == "PitBulls":
        pitBullHumane = "https://www.utahhumane.org/adopt?f%5B0%5D=field_species%3A3&f%5B1%5D=field_primary_breed%3A25"
        pitBullBestFriends ="https://bestfriends.org/adopt/adopt-our-sanctuary/dogs?field_animal_primary_breed_tid_selective=3177&field_animal_secondary_breed_tid_selective=All&field_animal_age_value_selective=All&field_animal_size_value_selective=All&field_animal_color_tid_selective=All&field_animal_sex_value_selective=All&title="
        pitBullNuzzlesAndCo = "https://nuzzlesandco.org/adopt-a-pet/?species%5B%5D&gender%5B%5D&age_group%5B%5D&size%5B%5D&breed%5B%5D=Pit+Bull+Terrier&wpv_post_id=969&wpv_view_count=855-CPID969&wpv_paged=1"

        print("-----------------Pit Bulls----------------")
        humaneReq = requests.get(pitBullHumane)
        humaneData = humaneReq.text
        soup = BeautifulSoup(humaneData, "html.parser")
        humaneDogCount = len(soup.find_all('div', class_="item"))
        numDogString = str(humaneDogCount)
        print("Humane Society: " + numDogString)
        print(pitBullHumane)

        print("------------------------------------------------------------")
        bfReq = requests.get(pitBullBestFriends)
        bfData = bfReq.text
        soup = BeautifulSoup(bfData, "html.parser")
        bfDogCount = len(soup.find_all('div', class_="rg-animal"))
        eachDogStr = str(bfDogCount)
        print("Best Friends: " + eachDogStr)
        print(pitBullBestFriends)

        print("------------------------------------------------------------")
        nuzzlesReq = requests.get(pitBullNuzzlesAndCo)
        nuzzlesData = nuzzlesReq.text
        soup = BeautifulSoup(nuzzlesData, "html.parser")
        nuzzlesDogCount = len(soup.find_all('div', class_="pet-result-img"))
        strNuzz = str(nuzzlesDogCount)
        print("Nuzzles And Co: " + strNuzz)
        print(pitBullNuzzlesAndCo)

        print("------------------------------------------------------------")
        totalNumDogs = humaneDogCount + bfDogCount + nuzzlesDogCount
        totalNumDogsStr = str(totalNumDogs)
        print("Total Number Available: " + totalNumDogsStr)
    else:
        print("Invalid Input! Can only choose AustralianShepards or PitBulls. Dog types must be typed in as shown.")