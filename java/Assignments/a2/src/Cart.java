// Nishil Kapadia - 501080772

import java.util.ArrayList;

public class Cart {
    private ArrayList<CartItem> items;

    // Constructor Method
    public Cart() {
        items = new ArrayList<CartItem>();
    }

    // Add CartItem
    public void addItem(CartItem item) {
        items.add(item);
    }

    // Remove CartItem
    public void removeItem(String productId) {
        for (CartItem cartItem : this.items) {

            if (cartItem.getProduct().getId().equals(productId)) {
                items.remove(cartItem);
                break;
            }
        }
    }

    // GetItems
    public ArrayList<CartItem> getItems() {
        return items;
    }

    // Print Items
    public void printItems() {
        System.out.println("\n--- CART ITEMS ---");
        for (CartItem cartItem : items) {
            cartItem.getProduct().print();
        }
    }
}
