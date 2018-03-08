#!/usr/bin/python
from bs4 import BeautifulSoup
import requests, sys, webbrowser

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
        webbrowser.open_new(shepardDogHumane)

        print("------------------------------------------------------------")
        bfReq = requests.get(shepardDogBestFriends)
        bfData = bfReq.text
        soup = BeautifulSoup(bfData, "html.parser")
        bfDogCount = len(soup.find_all('div', class_="rg-animal"))
        eachDogStr = str(bfDogCount)
        print("Best Friends: " + eachDogStr)
        webbrowser.open_new_tab(shepardDogBestFriends)

        print("------------------------------------------------------------")
        nuzzlesReq = requests.get(shepardNuzzlesAndCo)
        nuzzlesData = nuzzlesReq.text
        soup = BeautifulSoup(nuzzlesData, "html.parser")
        nuzzlesDogCount = len(soup.find_all('div', class_="pet-result-img"))
        strNuzz = str(nuzzlesDogCount)
        print("Nuzzles And Co: " + strNuzz)
        webbrowser.open_new_tab(shepardNuzzlesAndCo)

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
        webbrowser.open_new(pitBullHumane)

        print("------------------------------------------------------------")
        bfReq = requests.get(pitBullBestFriends)
        bfData = bfReq.text
        soup = BeautifulSoup(bfData, "html.parser")
        bfDogCount = len(soup.find_all('div', class_="rg-animal"))
        eachDogStr = str(bfDogCount)
        print("Best Friends: " + eachDogStr)
        webbrowser.open_new_tab(pitBullBestFriends)

        print("------------------------------------------------------------")
        nuzzlesReq = requests.get(pitBullNuzzlesAndCo)
        nuzzlesData = nuzzlesReq.text
        soup = BeautifulSoup(nuzzlesData, "html.parser")
        nuzzlesDogCount = len(soup.find_all('div', class_="pet-result-img"))
        strNuzz = str(nuzzlesDogCount)
        print("Nuzzles And Co: " + strNuzz)
        webbrowser.open_new_tab(pitBullNuzzlesAndCo)

        print("------------------------------------------------------------")
        totalNumDogs = humaneDogCount + bfDogCount + nuzzlesDogCount
        totalNumDogsStr = str(totalNumDogs)
        print("Total Number Available: " + totalNumDogsStr)
    elif sys.argv[1] == "Cats":
        catHumaneSociety = "https://www.utahhumane.org/adopt?f%5B0%5D=field_species%3A2&f%5B1%5D=field_primary_breed%3A394"
        catBestFriends = "https://bestfriends.org/adopt/adopt-our-sanctuary/cats?field_animal_primary_breed_tid_selective=2887&field_animal_secondary_breed_tid_selective=All&field_animal_age_value_selective=All&field_animal_size_value_selective=All&field_animal_color_tid_selective=All&field_animal_sex_value_selective=All&title="
        catNuzzlesAndCo = "https://nuzzlesandco.org/adopt-a-pet/?species%5B%5D=Cat&gender%5B%5D&age_group%5B%5D&size%5B%5D&breed%5B%5D=Domestic+Long+Hair&wpv_post_id=969&wpv_view_count=855-CPID969&wpv_paged=1"

        print("-----------------Long Haired Cats----------------")
        humaneReq = requests.get(catHumaneSociety)
        humaneData = humaneReq.text
        soup = BeautifulSoup(humaneData, "html.parser")
        humanecatCount = len(soup.find_all('div', class_="item"))
        numCatString = str(humanecatCount)
        print("Humane Society: " + numCatString)
        webbrowser.open_new(catHumaneSociety)

        print("------------------------------------------------------------")
        bfReq = requests.get(catBestFriends)
        bfData = bfReq.text
        soup = BeautifulSoup(bfData, "html.parser")
        bfcatCount = len(soup.find_all('div', class_="rg-animal"))
        eachcatStr = str(bfcatCount)
        print("Best Friends: " + eachcatStr)
        webbrowser.open_new_tab(catBestFriends)

        print("------------------------------------------------------------")
        nuzzlesReq = requests.get(catNuzzlesAndCo)
        nuzzlesData = nuzzlesReq.text
        soup = BeautifulSoup(nuzzlesData, "html.parser")
        nuzzlescatCount = len(soup.find_all('div', class_="pet-result-img"))
        strNuzz = str(nuzzlescatCount)
        print("Nuzzles And Co: " + strNuzz)
        webbrowser.open_new_tab(catNuzzlesAndCo)

        print("------------------------------------------------------------")
        totalNumcats = humanecatCount + bfcatCount + nuzzlescatCount
        totalNumcatsStr = str(totalNumcats)
        print("Total Number Available: " + totalNumcatsStr)
    elif sys.argv[1] == "Other":
        otherHumaneSociety = "https://www.utahhumane.org/adopt?f%5B0%5D=field_species%3A387"
        otherBestFriends = "https://bestfriends.org/adopt/adopt-our-sanctuary/rabbits"

        print("-----------------Other Creatures----------------")
        humaneReq = requests.get(otherHumaneSociety)
        humaneData = humaneReq.text
        soup = BeautifulSoup(humaneData, "html.parser")
        humaneotherCount = len(soup.find_all('div', class_="item"))
        numotherString = str(humaneotherCount)
        print("Humane Society: " + numotherString)
        webbrowser.open_new(otherHumaneSociety)

        print("------------------------------------------------------------")
        bfReq = requests.get(otherBestFriends)
        bfData = bfReq.text
        soup = BeautifulSoup(bfData, "html.parser")
        bfotherCount = len(soup.find_all('div', class_="rg-animal"))
        eachotherStr = str(bfotherCount)
        print("Best Friends: " + eachotherStr)
        webbrowser.open_new_tab(otherBestFriends)

        print("------------------------------------------------------------")
        totalNumothers = humaneotherCount + bfotherCount
        totalNumothersStr = str(totalNumothers)
        print("Total Number Available: " + totalNumothersStr)
    else:
        print("Invalid Input! Choices: AustralianShepards, PitBulls, Cats, or Other")