// Nishil Kapadia - 501080772

public class CartItem {
    private Product product;
    private String productOpts;

    public CartItem(Product product, String productOpts) {
        this.product = product;
        this.productOpts = productOpts;
    }

    public Product getProduct() {
        return product;
    }

    public String getProductOptions() {
        return productOpts;
    }

}