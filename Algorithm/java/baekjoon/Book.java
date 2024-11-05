import java.util.ArrayList;
import java.util.List;

public class Book {
    private final String bookName;
    private final List<Book> books;

    public Book(String bookName) {
        this.bookName = bookName;
        this.books = generateBooks();
    }

    public String getBookName() {
        return bookName;
    }

    public List<Book> generateBooks() {
        List<Book> books = new ArrayList<>();

        for (int i = 0; i < 5; i++) {
            books.add(this);
        }
        return books;
    }

    public List<Book> getBooks() {
        return new ArrayList<>(books);
    }

    public static void main(String[] args) {

        Book book = new Book("name");
        String name = book.getBookName();
        List<Book> books = book.getBooks();

        books.add(new Book("another"));
        name = "nono";
        System.out.println(book.getBooks());
        System.out.println(book.getBookName());


    }



}
