// Nishil Kapadia - 501080772

import java.io.IOException;
import java.io.File;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.Map;
import java.util.Random;
import java.util.Scanner;
import java.util.TreeMap;
import java.util.Map.Entry;

/**
 * Models a simple ECommerce system. Keeps track of products for sale,
 * registered customers, product orders and
 * orders that have been shipped to a customer
 */
public class ECommerceSystem {
	Map<String, Product> products = new TreeMap<String, Product>();
	ArrayList<Customer> customers = new ArrayList<Customer>();

	ArrayList<ProductOrder> orders = new ArrayList<ProductOrder>();
	ArrayList<ProductOrder> shippedOrders = new ArrayList<ProductOrder>();

	// These variables are used to generate order numbers, customer id's, product
	// id's
	int orderNumber = 500;
	int customerId = 900;
	int productId = 700;

	// Random number generator
	Random random = new Random();

	public ECommerceSystem() {

		// read some products
		try {
			products = productsMap(readProducts("products.txt"));
		} catch (IOException e) {
			System.out.println(e.getMessage());
			System.exit(1);
		}

		// Create some customers
		customers.add(new Customer(generateCustomerId(), "Inigo Montoya", "1 SwordMaker Lane, Florin"));
		customers.add(new Customer(generateCustomerId(), "Prince Humperdinck", "The Castle, Florin"));
		customers.add(new Customer(generateCustomerId(), "Andy Dufresne", "Shawshank Prison, Maine"));
		customers.add(new Customer(generateCustomerId(), "Ferris Bueller", "4160 Country Club Drive, Long Beach"));
	}

	/**
	 * Print all Products
	 */
	public void printAllProducts() {
		for (Product p : products.values())
			p.print();
	}

	/**
	 * Print all Books
	 */
	public void printAllBooks() {
		for (Product p : products.values()) {
			if (p.getCategory() == Product.Category.BOOKS) {
				p.print();
			}
		}
	}

	/**
	 * Print all books by given author
	 * 
	 * @param author
	 * @return ArrayList<Book>
	 */
	public ArrayList<Book> booksByAuthor(String author) {
		ArrayList<Book> books = new ArrayList<Book>();
		for (Product p : products.values()) {
			if (p.getCategory() == Product.Category.BOOKS) {
				Book book = (Book) p;
				if (book.getAuthor().equals(author))
					books.add(book);
			}
		}
		return books;
	}

	/**
	 * Print all Orders
	 */
	public void printAllOrders() {
		for (ProductOrder o : orders)
			o.print();
	}

	/**
	 * Print all shipped orders
	 */
	public void printAllShippedOrders() {
		for (ProductOrder o : shippedOrders)
			o.print();
	}

	/**
	 * Print all customers
	 */
	public void printCustomers() {
		for (Customer c : customers)
			c.print();
	}

	/**
	 * Given a customer id, print all the current orders and shipped orders for them
	 * (if any)
	 * 
	 * @param customerId
	 */
	public void printOrderHistory(String customerId) {
		// Make sure customer exists
		getCustomer(customerId);

		System.out.println("Current Orders of Customer " + customerId);
		for (ProductOrder order : orders) {
			if (order.getCustomer().getId().equals(customerId))
				order.print();
		}

		System.out.println("\nShipped Orders of Customer " + customerId);

		for (ProductOrder order : shippedOrders) {
			if (order.getCustomer().getId().equals(customerId))
				order.print();
		}
	}

	/**
	 * Order Product
	 * 
	 * @param productId
	 * @param customerId
	 * @param productOptions
	 * @return String
	 */
	public String orderProduct(String productId, String customerId, String productOptions) {

		Customer customer = getCustomer(customerId);
		Product product = getProduct(productId);

		// Check if the options are valid for this product (e.g. Paperback or Hardcover
		// or EBook for Book product)
		checkProductOptions(product, productOptions);
		// Is it in stock?
		checkStock(product, productOptions);

		// Create a ProductOrder
		ProductOrder order = new ProductOrder(generateOrderNumber(), product, customer, productOptions);
		// Decrement Stock Count
		product.reduceStockCount(productOptions);
		// Increment Order Count
		product.incrementOrderCount();

		// Add to orders and return
		orders.add(order);

		return order.getOrderNumber();
	}

	/**
	 * Create a new Customer
	 * 
	 * @param name
	 * @param address
	 */
	public void createCustomer(String name, String address) {
		// Check to ensure name is valid
		if (name == null || name.equals("")) {
			throw new InvalidCustomerNameException("Invalid Customer Name " + name);
		}

		// Check to ensure address is valid
		if (address == null || address.equals("")) {
			throw new InvalidCustomerAddressException("Invalid Customer Address " + address);
		}

		Customer customer = new Customer(generateCustomerId(), name, address);
		customers.add(customer);

	}

	/**
	 * Ship Order
	 * 
	 * @param orderNumber
	 * @return ProductOrder
	 */
	public ProductOrder shipOrder(String orderNumber) {
		// Check if order number exists
		ProductOrder order = getOrder(orderNumber);

		orders.remove(order);
		shippedOrders.add(order);
		return order;
	}

	/**
	 * Cancels Order
	 * 
	 * @return this Student's name.
	 */
	public void cancelOrder(String orderNumber) {
		// Check if order number exists
		ProductOrder order = getOrder(orderNumber);

		orders.remove(order);
	}

	/**
	 * Sort products by increasing price and prints them
	 * 
	 * @throws IOException
	 */
	public void printByPrice() throws IOException {
		// Assuming no edits are done to the products (file) at runtime.
		ArrayList<Product> productsTemp = readProducts("products.txt");
		Collections.sort(productsTemp, new PriceComparator());

		for (Product product : productsTemp) {
			product.print();
		}
	}

	/**
	 * Sort products alphabetically by product name and prints them
	 * 
	 * @throws IOException
	 */
	public void printByName() throws IOException {
		ArrayList<Product> productsTemp = readProducts("products.txt");
		Collections.sort(productsTemp, new NameComparator());

		for (Product product : productsTemp) {
			product.print();
		}
	}

	/**
	 * Sort products alphabetically by product name
	 */
	public void sortCustomersByName() {
		Collections.sort(customers);
	}

	/**
	 * Add to Cart
	 * 
	 * @param productid
	 * @param customerID
	 * @param productOptions
	 */
	public void addToCart(String productid, String customerID, String productOptions) {

		Customer customer = getCustomer(customerID);
		Product product = getProduct(productid);
		checkProductOptions(product, productOptions);
		checkStock(product, productOptions);

		// Get Cart and add CartItem
		Cart cart = customer.getCart();
		CartItem newCartItem = new CartItem(product, productOptions);
		cart.addItem(newCartItem);
	}

	/**
	 * Remove a cart Item from the Cart
	 * 
	 * @param customerId
	 * @param productId
	 */
	// Remove Cart Item
	public void removeCartItem(String customerId, String productId) {
		Customer customer = getCustomer(customerId);
		getProduct(productId);

		// Get Cart and add CartItem
		Cart cart = customer.getCart();
		cart.removeItem(productId);
	}

	/**
	 * Print the CartItems from the Cart
	 * 
	 * @param customerId
	 */
	public void printCart(String customerId) {

		Customer customer = getCustomer(customerId);
		customer.getCart().printItems();

	}

	/**
	 * Order Items from the Cart
	 * 
	 * @param customerId
	 * @return ArrayList<String>
	 */
	public ArrayList<String> orderItems(String customerId) {

		Customer customer = getCustomer(customerId);

		// Get cart
		Cart cart = customer.getCart();
		ArrayList<CartItem> cartItems = cart.getItems();

		ArrayList<String> orderNbrs = new ArrayList<String>();

		for (int i = 0; i < cartItems.size(); i++) {
			CartItem item = cartItems.get(i);
			String orderNumber = orderProduct(item.getProduct().getId(), customerId, item.getProductOptions());
			orderNbrs.add(orderNumber);
			removeCartItem(customerId, item.getProduct().getId());
			i--;
		}

		return orderNbrs;

	}

	/**
	 * Keeps track of the number of times a product was ordered and in decending
	 * order
	 */
	public void stats() {
		Map<String, Integer> map = new TreeMap<String, Integer>();

		for (Product p : products.values()) {
			map.put(p.getId(), p.getOrderCount());
		}

		ArrayList<Entry<String, Integer>> sortedList = new ArrayList<Entry<String, Integer>>(map.entrySet());
		Collections.sort(sortedList, new OrderCountComparator());

		for (Entry<String, Integer> entry : sortedList) {
			String productId = entry.getKey();
			Product p = getProduct(productId);

			System.out.printf("\nId: %-5s Name: %-20s Total Orders: %-5d", p.getId(), p.getName(), entry.getValue());

		}
	}

	/**
	 * Rate a Product
	 * 
	 * @param productId
	 * @param Rating
	 */
	public void rateProduct(String productId, String rating) {

		Product product = getProduct(productId);

		if (rating.isBlank()) {
			throw new InvalidRatingNumber("Invalid Rating Number");
		}

		Integer rate = Integer.parseInt(rating);

		if (rate < 1 || rate > 5) {
			throw new InvalidRatingNumber("Invalid Rating Number");
		}

		product.rate(rate);

	}

	/**
	 * Print Average Product Ratings
	 * 
	 * @param productId
	 * @return
	 */
	public Double printProductRating(String productId) {
		Product product = getProduct(productId);
		return product.getAverageRating();
	}

	public void ProductByCategoryAndRating(String category, String Rating) {

		ArrayList<Product> filterList = new ArrayList<Product>();
		Product.Category cat;

		try {
			cat = Product.Category.valueOf(category.toUpperCase());
		} catch (IllegalArgumentException e) {
			throw new InvalidCategory("Invalid Category");
		}

		// Get all products from a category
		for (Product p : products.values()) {
			// filter them based on rating and category
			if ((p.getCategory() == cat)
					&& p.getAverageRating() > Double.parseDouble(Rating)) {
				filterList.add(p);
			}
		}

		// sort them based on the rating then
		Collections.sort(filterList, new RatingsComparator());

		for (Product p : filterList) {
			p.print();
			System.out.print(" Rating: " + p.getAverageRating() + " Stars");
		}

	}

	// ------- COMPARATOR CLASSES ------------

	private class PriceComparator implements Comparator<Product> {
		public int compare(Product a, Product b) {
			if (a.getPrice() > b.getPrice())
				return 1;
			if (a.getPrice() < b.getPrice())
				return -1;
			return 0;
		}
	}

	private class NameComparator implements Comparator<Product> {
		public int compare(Product a, Product b) {
			return a.getName().compareTo(b.getName());
		}
	}

	private class OrderCountComparator implements Comparator<Entry<String, Integer>> {

		public int compare(Entry<String, Integer> o1, Entry<String, Integer> o2) {
			if (o2.getValue() > o1.getValue()) {
				return 1;
			}
			if (o2.getValue() < o1.getValue()) {
				return -1;
			}
			return 0;
		}
	}

	private class RatingsComparator implements Comparator<Product> {
		public int compare(Product a, Product b) {
			if (a.getAverageRating() > b.getAverageRating())
				return 1;
			if (a.getAverageRating() < b.getAverageRating())
				return -1;
			return 0;
		}
	}

	// ------- PRIVATE HELPER METHODS --------

	/**
	 * Generate a orderNumber
	 * 
	 * @return String
	 */
	private String generateOrderNumber() {
		return "" + orderNumber++;
	}

	/**
	 * Generates a unique customer Id
	 * 
	 * @return String
	 */
	private String generateCustomerId() {
		return "" + customerId++;
	}

	/**
	 * Generates a unique Product Id
	 * 
	 * @return String
	 */
	private String generateProductId() {
		return "" + productId++;
	}

	/**
	 * Gets Customer and checks for exceptions
	 * 
	 * @param customerId
	 * @return Customer
	 */
	private Customer getCustomer(String customerId) {
		// Get customer
		int index = customers.indexOf(new Customer(customerId));

		if (index == -1) {
			throw new UnknownCustomerException("Customer " + customerId + " Not Found");
		}

		Customer customer = customers.get(index);
		return customer;
	}

	/**
	 * Gets Product and checks for exceptions
	 * 
	 * @param productId
	 * @return Product
	 */
	private Product getProduct(String productId) {
		Product p = products.get(productId);

		if (p == null) {
			throw new UnknownProductException("Product " + productId + " Not Found");
		}

		return p;
	}

	/**
	 * Gets Order and checks for exceptions
	 * 
	 * @param orderNumber
	 * @return ProductOrder
	 */
	private ProductOrder getOrder(String orderNumber) {
		int index = orders.indexOf(new ProductOrder(orderNumber, null, null, ""));

		if (index == -1) {
			throw new InvalidOrderNumber("Order " + orderNumber + " Not Found");
		}

		ProductOrder order = orders.get(index);
		return order;
	}

	/**
	 * Validates Product Options
	 * 
	 * @param product
	 * @param productOptions
	 */
	private void checkProductOptions(Product product, String productOptions) {
		if (!product.validOptions(productOptions)) {
			throw new InvalidProductOptsException(
					"Product " + product.getName() + " ProductId " + productId + " Invalid Options: " + productOptions);
		}
	}

	/**
	 * Checks stock for the product
	 * 
	 * @param product
	 * @param productOptions
	 */
	private void checkStock(Product product, String productOptions) {
		if (product.getStockCount(productOptions) == 0) {
			throw new OutOfStockException("Product " + product.getName() + " ProductId " + productId + " Out of Stock");
		}
	}

	/**
	 * Reads products file and outputs ArrayList
	 * 
	 * @param filename
	 * @return ArrayList<Product>
	 * @throws IOException
	 */
	private ArrayList<Product> readProducts(String filename) throws IOException {
		File file = new File(filename);
		Scanner in = new Scanner(file);

		ArrayList<Product> productList = new ArrayList<Product>();

		/*
		 * 1. Category
		 * 2. ProductName
		 * 3. Price
		 * 4. StockCount:
		 * Non-Book-Shoes: int
		 * Book: 2 int (Paperback & Hardcover)
		 * Shoes: TBD
		 * 5.Additional Info: seperated by colon
		 * Book: title:author:year
		 */

		while (in.hasNextLine()) {
			in.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");
			String line = in.nextLine();
			Product.Category category = Product.Category.valueOf(line);
			String name = in.nextLine();
			double price = Double.parseDouble(in.nextLine());

			switch (category) {
				case BOOKS:

					String stocks[] = in.nextLine().split(" ");
					int paperbackStock = Integer.parseInt(stocks[0]);
					int hardcoverStock = Integer.parseInt(stocks[1]);

					Scanner lineScanner = new Scanner(in.nextLine());
					lineScanner.useDelimiter(":");

					String title = lineScanner.next();
					String author = lineScanner.next();
					int year = Integer.parseInt(lineScanner.next());

					lineScanner.close();

					productList.add(new Book(name, generateProductId(), price, paperbackStock, hardcoverStock, title,
							author, year));

					break;

				case SHOES:
					// TODO: TBD
					// productTemp.add(new Shoes(name, generateProductId(), price, stockCounts));
					break;
				default:
					int stock = Integer.parseInt(in.nextLine());
					productList.add(new Product(name, generateProductId(), price, stock, category));
					break;
			}

		}

		in.close();
		return productList;
	}

	/**
	 * Convert Products ArrayList to an TreeMap
	 * 
	 * @param prodsList
	 * @return Map<String, Product>
	 */
	private Map<String, Product> productsMap(ArrayList<Product> prodsList) {
		Map<String, Product> productsTemp = new TreeMap<String, Product>();

		for (Product p : prodsList) {
			productsTemp.put(p.getId(), p);
		}

		return productsTemp;
	}
}

// ------------- Custom Exception Classes ----------------

class UnknownCustomerException extends RuntimeException {
	public UnknownCustomerException() {
	}

	public UnknownCustomerException(String message) {
		super(message);
	}
}

class UnknownProductException extends RuntimeException {
	public UnknownProductException() {
	}

	public UnknownProductException(String message) {
		super(message);
	}
}

class InvalidProductOptsException extends RuntimeException {
	public InvalidProductOptsException() {
	}

	public InvalidProductOptsException(String message) {
		super(message);
	}
}

class OutOfStockException extends RuntimeException {
	public OutOfStockException() {
	}

	public OutOfStockException(String message) {
		super(message);
	}
}

class InvalidCustomerNameException extends RuntimeException {
	public InvalidCustomerNameException() {
	}

	public InvalidCustomerNameException(String message) {
		super(message);
	}
}

class InvalidCustomerAddressException extends RuntimeException {
	public InvalidCustomerAddressException() {
	}

	public InvalidCustomerAddressException(String message) {
		super(message);
	}
}

class InvalidOrderNumber extends RuntimeException {
	public InvalidOrderNumber() {
	}

	public InvalidOrderNumber(String message) {
		super(message);
	}
}

class InvalidRatingNumber extends RuntimeException {
	public InvalidRatingNumber() {
	}

	public InvalidRatingNumber(String message) {
		super(message);
	}
}

class InvalidCategory extends RuntimeException {
	public InvalidCategory() {
	}

	public InvalidCategory(String message) {
		super(message);
	}
}
