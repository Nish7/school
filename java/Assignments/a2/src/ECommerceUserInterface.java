// Nishil Kapadia - 501080772

import java.io.IOException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

/**
 * Simulation of a Simple E-Commerce System (like Amazon)
 */
public class ECommerceUserInterface {
	public static void main(String[] args) {
		// Create the system
		ECommerceSystem amazon = new ECommerceSystem();

		try (Scanner scanner = new Scanner(System.in)) {
			System.out.print(">");

			// Process keyboard actions
			while (scanner.hasNextLine()) {
				String action = scanner.nextLine();

				try {

					if (action == null || action.equals("")) {
						System.out.print("\n>");
						continue;
					} else if (action.equalsIgnoreCase("Q") || action.equalsIgnoreCase("QUIT")) {
						return;
					} else if (action.equalsIgnoreCase("PRODS")) {
						// List all products for sale
						amazon.printAllProducts();
					} else if (action.equalsIgnoreCase("BOOKS")) {
						// List all books for sale
						amazon.printAllBooks();
					} else if (action.equalsIgnoreCase("BOOKSBYAUTHOR")) {
						String author = "";

						System.out.print("Author: ");
						if (scanner.hasNextLine())
							author = scanner.nextLine();

						ArrayList<Book> books = amazon.booksByAuthor(author);
						Collections.sort(books);
						for (Book book : books) {
							book.print();
						}
					} else if (action.equalsIgnoreCase("CUSTS")) {
						// List all registered customers
						amazon.printCustomers();
					} else if (action.equalsIgnoreCase("ORDERS")) {
						// List all current product orders
						amazon.printAllOrders();
					} else if (action.equalsIgnoreCase("SHIPPED")) {
						// List all orders that have been shipped
						amazon.printAllShippedOrders();
					} else if (action.equalsIgnoreCase("NEWCUST")) {
						// Create a new registered customer
						String name = "";
						String address = "";

						System.out.print("Name: ");
						if (scanner.hasNextLine())
							name = scanner.nextLine();

						System.out.print("\nAddress: ");
						if (scanner.hasNextLine())
							address = scanner.nextLine();

						amazon.createCustomer(name, address);

					} else if (action.equalsIgnoreCase("SHIP")) {
						// ship an order to a customer
						String orderNumber = "";

						System.out.print("Order Number: ");
						if (scanner.hasNextLine())
							orderNumber = scanner.nextLine();

						ProductOrder order = amazon.shipOrder(orderNumber);
						order.print();
					} else if (action.equalsIgnoreCase("CUSTORDERS")) {
						// List all the current orders and shipped orders for
						// this customer
						String customerId = "";

						System.out.print("Customer Id: ");
						if (scanner.hasNextLine())
							customerId = scanner.nextLine();

						// Prints all current orders and all shipped orders for this customer
						amazon.printOrderHistory(customerId);

					} else if (action.equalsIgnoreCase("ORDER")) {
						// order a product for a certain customer
						String productId = "";
						String customerId = "";

						System.out.print("Product Id: ");
						if (scanner.hasNextLine())
							productId = scanner.nextLine();

						System.out.print("\nCustomer Id: ");
						if (scanner.hasNextLine())
							customerId = scanner.nextLine();

						String orderNumber = amazon.orderProduct(productId, customerId, "");

						System.out.println("Order #" + orderNumber);

					} else if (action.equalsIgnoreCase("ORDERBOOK")) {
						// order a book for a customer, provide a format
						// (Paperback, Hardcover or EBook)
						String productId = "";
						String customerId = "";
						String format = "";

						System.out.print("Product Id: ");
						if (scanner.hasNextLine())
							productId = scanner.nextLine();

						System.out.print("\nCustomer Id: ");
						if (scanner.hasNextLine())
							customerId = scanner.nextLine();

						System.out.print("\nFormat [Paperback Hardcover EBook]: ");
						if (scanner.hasNextLine())
							format = scanner.nextLine();

						String orderNumber = amazon.orderProduct(productId, customerId, format);

						System.out.println("Order #" + orderNumber);

					} else if (action.equalsIgnoreCase("ORDERSHOES")) {
						// order a book for a customer, provide a format
						// (Paperback, Hardcover or EBook)
						String productId = "";
						String customerId = "";
						String sizeColor = "";

						System.out.print("Product Id: ");
						if (scanner.hasNextLine())
							productId = scanner.nextLine();

						System.out.print("\nCustomer Id: ");
						if (scanner.hasNextLine())
							customerId = scanner.nextLine();

						System.out.print("\nSize (6, 7, 8, 9, 10) and Color (Black or Brown): ");
						if (scanner.hasNextLine())
							sizeColor = scanner.nextLine();

						String orderNumber = amazon.orderProduct(productId, customerId, sizeColor);

						System.out.println("Order #" + orderNumber);

					} else if (action.equalsIgnoreCase("CANCEL")) {
						// Cancel an existing order
						String orderNumber = "";

						System.out.print("Order Number: ");
						if (scanner.hasNextLine())
							orderNumber = scanner.nextLine();

						amazon.cancelOrder(orderNumber);

					} else if (action.equalsIgnoreCase("PRINTBYPRICE")) {
						// sort products by price
						amazon.printByPrice();
					} else if (action.equalsIgnoreCase("PRINTBYNAME")) {
						// sort products by name (alphabetic)
						amazon.printByName();
					} else if (action.equalsIgnoreCase("SORTCUSTS")) {
						// sort products by name (alphabetic)
						amazon.sortCustomersByName();
					} else if (action.equalsIgnoreCase("ADDTOCART")) {

						String productId = "";
						String customerId = "";
						String productOpts = "";

						System.out.print("Product Id: ");
						if (scanner.hasNextLine())
							productId = scanner.nextLine();

						System.out.print("\nCustomer Id: ");
						if (scanner.hasNextLine())
							customerId = scanner.nextLine();

						System.out.print("\nProduct Options: ");
						if (scanner.hasNextLine())
							productOpts = scanner.nextLine();

						amazon.addToCart(productId, customerId, productOpts);

						System.out.println("Product ID: " + productId + " Added to the Cart");

					} else if (action.equalsIgnoreCase("PRINTCART")) {

						String customerId = "";

						System.out.print("Customer ID: ");
						if (scanner.hasNextLine())
							customerId = scanner.nextLine();

						amazon.printCart(customerId);

					} else if (action.equalsIgnoreCase("REMCARTITEM")) {

						String productId = "";
						String customerId = "";

						System.out.print("Product Id: ");
						if (scanner.hasNextLine())
							productId = scanner.nextLine();

						System.out.print("\nCustomer Id: ");
						if (scanner.hasNextLine())
							customerId = scanner.nextLine();

						amazon.removeCartItem(customerId, productId);

						System.out.println("Product ID: " + productId + " removed from the Cart");

					} else if (action.equalsIgnoreCase("ORDERITEMS")) {

						String customerId = "";

						System.out.print("Customer ID: ");

						if (scanner.hasNextLine()) {
							customerId = scanner.nextLine();
						}

						ArrayList<String> ordernbrs = amazon.orderItems(customerId);

						for (String order : ordernbrs) {
							System.out.println("Order: " + order);
						}

					} else if (action.equalsIgnoreCase("STATS")) {
						amazon.stats();
					} else if (action.equalsIgnoreCase("RATEPROD")) {
						String productId = "";
						String rating = "";

						System.out.print("Product Id: ");
						if (scanner.hasNextLine())
							productId = scanner.nextLine();

						System.out.print("Rating: 1/2/3/4/5: ");
						if (scanner.hasNextLine())
							rating = scanner.nextLine();

						amazon.rateProduct(productId, rating);
					} else if (action.equalsIgnoreCase("PRINTPRODRATING")) {
						String productId = "";

						System.out.print("Product Id: ");
						if (scanner.hasNextLine())
							productId = scanner.nextLine();

						System.out.println(amazon.printProductRating(productId) + " Stars");

					} else if (action.equalsIgnoreCase("PRODSBYCATEGORYRATING")) {
						String category = "";
						String ratingThreshold = "";

						System.out.print("Category to filter (plural): ");
						if (scanner.hasNextLine())
							category = scanner.nextLine();

						System.out.print("Rating Threshold: ");
						if (scanner.hasNextLine())
							ratingThreshold = scanner.nextLine();

						amazon.ProductByCategoryAndRating(category, ratingThreshold);
					}

				} catch (RuntimeException e) {
					System.out.println("Error: " + e.getMessage());
				} catch (IOException e) {
					System.out.println("Error: " + e.getMessage());
					System.exit(1);
				} finally {
					System.out.print("\n>");
				}
			}
		}

	}
}
