// Nishil Kapadia - 501080772

public class Shoe extends Product {
    int[] blackStock = new int[5];
    int[] brownStock = new int[5];
    final static String colors = "Black, Brown";
    final static String sizes = "6, 7, 8, 9, 10";

    public Shoe(String name, String id, double price, int[] blackStock, int[] brownStock) {
        super(name, id, price, 0, Product.Category.SHOES);
        this.blackStock = blackStock;
        this.brownStock = brownStock;
    }

    // Check if a valid format
    public boolean validOptions(String productOptions) {
        productOptions = productOptions.toLowerCase();

        if (!productOptions.contains("brown") && !productOptions.contains("black")) {
            return false;
        }

        String color = getColor(productOptions);
        int size = getSize(productOptions);

        if (color.equalsIgnoreCase("brown") || color.equalsIgnoreCase("black")) {
            if (size == 6 || size == 7 || size == 8 || size == 9 || size == 10) {
                return true;
            }
        }

        return false;
    }

    // Override getStockCount() in super class.
    public int getStockCount(String productOptions) {
        String color = getColor(productOptions);
        int size = getSize(productOptions);

        if (color.equalsIgnoreCase("black")) {
            return blackStock[size - 6];
        }

        return brownStock[size - 6];
    }

    public void setStockCount(int stockCount, String productOptions) {
        String color = getColor(productOptions);
        int size = getSize(productOptions);

        if (color.equalsIgnoreCase("black")) {
            blackStock[size - 6] = stockCount;
        }

        brownStock[size - 6] = stockCount;
    }

    public void reduceStockCount(String productOptions) {
        String color = getColor(productOptions);
        int size = getSize(productOptions);

        if (color.equalsIgnoreCase("black")) {
            blackStock[size - 6]--;
        }

        brownStock[size - 6]--;
    }

    public String getColor(String productOptions) {
        String[] opts = productOptions.split(" ");
        return opts[0];
    }

    public int getSize(String productOptions) {
        String[] opts = productOptions.split(" ");
        return Integer.parseInt(opts[1]);
    }

    public void print() {
        super.print();
        System.out.printf("Colors: %-10s Sizes: %-10s", colors, sizes);
    }

}
