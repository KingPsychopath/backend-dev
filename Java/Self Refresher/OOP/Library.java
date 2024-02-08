package OOP;
import java.util.ArrayList;

public class Library {
    private ArrayList<Book> books = new ArrayList<Book>();

    public void addBook(Book book) {
        books.add(book);
    }

    public void removeBook(Readable book) {
        books.remove(book);
    }

    public void listBooks() {
        for (Readable book : books) {
            System.out.println(book);
        }
    }

    public static void main(String[] args) {
        Library library = new Library();
        Book book1 = new Book("The Hobbit", "J.R.R. Tolkien", 310, "English");
        Book book2 = new Book("The Catcher in the Rye", "J.D. Salinger", 277, "English");
        Book book3 = new Book("The Alchemist", "Paulo Coelho", 208, "Portuguese");
        Book book4 = new Book("The Little Prince", "Antoine de Saint-Exupéry", 96, "French");
        Manga manga1 = new Manga("Naruto", "Masashi Kishimoto", 700, "Japanese", "Shonen");
        Manga manga2 = new Manga("One Piece", "Eiichiro Oda", 1000, "Japanese", "Shonen");

        library.addBook(book1);
        library.addBook(book2);
        library.addBook(book3);
        library.addBook(book4);
        library.addBook(manga1);
        library.addBook(manga2);

        library.listBooks();
    }
}
