package OOP;

public class Book implements Readable {
    // fields, constructors, and methods
    private String title;
    private String author;
    private int pages;
    private String language;

    public Book(String title, String author, int pages, String language) {
        this.title = title;
        this.author = author;
        this.pages = pages;
        this.language = language;
    }

    @Override
    public String getTitle() {
        return title;
    }

    @Override
    public String getAuthor() {
        return author;
    }

    @Override
    public int getPages() {
        return pages;
    }

    @Override
    public String getLanguage() {
        return language;
    }

    @Override
    public void setTitle(String title) {
        this.title = title;
    }

    @Override
    public void setAuthor(String author) {
        this.author = author;
    }

    @Override
    public void setPages(int pages) {
        this.pages = pages;
    }

    @Override
    public void setLanguage(String language) {
        this.language = language;
    }

    @Override
    public String toString() {
        return "Book{" + "title=" + getTitle() + ", author=" + getAuthor() + ", pages=" + getPages() + ", language=" + getLanguage() + '}';
    }

    @Override
    public int hashCode() {
        final int prime = 31;
        int result = 1;
        result = prime * result + ((title == null) ? 0 : title.hashCode());
        result = prime * result + ((author == null) ? 0 : author.hashCode());
        result = prime * result + pages;
        result = prime * result + ((language == null) ? 0 : language.hashCode());
        return result;
    }

    // Override the equals method
    @Override
    public boolean equals(Object obj) {
        if (this == obj)
            return true;
        if (obj == null)
            return false;
        if (getClass() != obj.getClass())
            return false;
        Book other = (Book) obj;
        if (title == null) {
            if (other.title != null)
                return false;
        } else if (!title.equals(other.title))
            return false;
        if (author == null) {
            if (other.author != null)
                return false;
        } else if (!author.equals(other.author))
            return false;
        if (pages != other.pages)
            return false;
        if (language == null) {
            if (other.language != null)
                return false;
        } else if (!language.equals(other.language))
            return false;
        return true;
    }
}