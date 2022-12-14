// Nishil Kapadia - 501080772

import java.util.Comparator;

/* A book IS A product that has additional information - e.g. title, author

 	 A book also comes in different formats ("Paperback", "Hardcover", "EBook")
 	 
 	 The format is specified as a specific "stock type" in get/set/reduce stockCount methods.

*/
public class Book extends Product {
  private String author;
  private String title;
  private int year;

  // Stock related information NOTE: inherited stockCount variable is used for
  // EBooks
  int paperbackStock;
  int hardcoverStock;

  public Book(String name, String id, double price, int paperbackStock, int hardcoverStock, String title,
      String author, int year) {
    // Make use of the constructor in the super class Product. Initialize additional
    // Book instance variables.
    // Set category to BOOKS
    super(name, id, price, Integer.MAX_VALUE, Product.Category.BOOKS);
    this.paperbackStock = paperbackStock;
    this.hardcoverStock = hardcoverStock;
    this.author = author;
    this.title = title;
    this.year = year;
  }

  // Check if a valid format
  public boolean validOptions(String productOptions) {
    // check productOptions for "Paperback" or "Hardcover" or "EBook"
    // if it is one of these, return true, else return false
    if (productOptions.equalsIgnoreCase("paperback") || productOptions.equalsIgnoreCase("hardcover")
        || productOptions.equalsIgnoreCase("ebook")) {
      return true;
    }

    return false;
  }

  // Get AuthorName
  public String getAuthor() {
    return this.author;
  }

  // Get Year
  public int getYear() {
    return this.year;
  }

  // Override getStockCount() in super class.
  public int getStockCount(String productOptions) {
    // Use the productOptions to check for (and return) the number of stock for
    // "Paperback" etc
    // Use the variables paperbackStock and hardcoverStock at the top.
    // For "EBook", use the inherited stockCount variable.
    if (productOptions.equalsIgnoreCase("paperback")) {
      return this.paperbackStock;
    } else if (productOptions.equalsIgnoreCase("hardcover")) {
      return this.hardcoverStock;
    }
    return super.getStockCount("ebook");
  }

  public void setStockCount(int stockCount, String productOptions) {
    // Use the productOptions to check for (and set) the number of stock for
    // "Paperback" etc
    // Use the variables paperbackStock and hardcoverStock at the top.
    // For "EBook", set the inherited stockCount variable.

    if (productOptions.equalsIgnoreCase("paperback")) {
      this.paperbackStock = stockCount;
    } else if (productOptions.equalsIgnoreCase("hardcover")) {
      this.hardcoverStock = stockCount;
    } else if (productOptions.equalsIgnoreCase("ebook")) {
      super.setStockCount(stockCount, "EBook");
    }

  }

  /*
   * When a book is ordered, reduce the stock count for the specific stock type
   */
  public void reduceStockCount(String productOptions) {
    // Use the productOptions to check for (and reduce) the number of stock for
    // "Paperback" etc
    // Use the variables paperbackStock and hardcoverStock at the top.
    // For "EBook", set the inherited stockCount variable.
    if (productOptions.equalsIgnoreCase("paperback")) {
      this.paperbackStock--;
    } else if (productOptions.equalsIgnoreCase("hardcover")) {
      this.hardcoverStock--;
    } else if (productOptions.equalsIgnoreCase("ebook")) {
      super.setStockCount(super.getStockCount("EBook") - 1, "EBook");
    }
  }

  /*
   * Print product information in super class and append Book specific information
   * title and author
   */
  public void print() {
    // Replace the line below.
    // Make use of the super class print() method and append the title and author
    // info. See the video
    super.print();
    System.out.printf("Book Title: %-30s Author: %-10s Year: %5d", title, author, year);
  }
}

class sortAuthor implements Comparator<Book> {
  public int compare(Book b1, Book b2) {
    if (b1.getYear() < b2.getYear())
      return -1;
    if (b1.getYear() > b2.getYear())
      return 1;
    else
      return 0;
  }
}
