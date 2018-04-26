books = [{
    "id": 1,
    "name": "Code Simplicity",
    "description": "O'Reilly book",
}, {
    "id": 2,
    "name": "Art of readable code",
    "description": "O'Reilly book",
}]


def listBooks():
    for book in books:
        print "************"
        print "ID: " + str(book["id"])
        print "Name: " + book["name"]
        print "Description: " + book["description"]
        print "************"


def getBook(id):
    user_book = None
    for book in books:
        if book["id"] == id:
            user_book = book
            break

    return book


print "Bienvenido a la Libreria Monkey!"
print "Estas son las operaciones disponibles: "
print "[1] Listar libros disponibles."
print "[2] Llevarte un libro."

operation = input("Que deseas realizar: ")

if operation == 1:
    listBooks()
elif operation == 2:
    book_id = input("Ingresa el ID del libro: ")
    book = getBook(book_id)

    print ""
    print "*************"
    print "Name: " + book["name"]
    print "Description: " + book["description"]
    print "*************"
    print ""
    print "Gracias, vuelve pronto!"
