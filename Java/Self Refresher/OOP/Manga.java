package OOP;

public class Manga extends Book{

    private String genre;

    public Manga(String title, String author, int pages, String language, String genre) {
        super(title, author, pages, language);
        this.genre = genre;
    }

    @Override
    public String getGenre() {
        return genre;
    }

    @Override
    public void setGenre(String genre) {
        this.genre = genre;
    }

    @Override
    public String toString() {
        return "Manga{" + "title=" + getTitle() + ", author=" + getAuthor() + ", pages=" + getPages() + ", language=" + getLanguage() + ", genre=" + genre + '}';
    }
    
}
