#
def checkMagazine(magazine, note):
    magazine.sort()
    note.sort()

    for word in note:
        try:
            r = magazine.index(word)
        except ValueError:
            print("No")
            return
        del magazine[r]

    print("Yes")
