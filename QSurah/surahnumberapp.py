import quranSurahs

def SurahName():
    SNumber = int(input("What is the number of Surah?"))
    print(quranSurahs.SurahNames[SNumber-1])

SurahName()