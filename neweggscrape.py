import csv
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import tkinter as tk
from tkinter import ttk, messagebox

def fetch_page(url):
    try:
        with uReq(url) as uClient:
            page_html = uClient.read()
        return page_html
    except Exception as e:
        messagebox.showerror("Error", f"Error fetching the URL: {e}")
        return None

def parse_page(page_html):
    try:
        page_soup = soup(page_html, "html.parser")
        return page_soup.findAll("div", {"class": "item-container"})
    except Exception as e:
        messagebox.showerror("Error", f"Error parsing the HTML: {e}")
        return []

def extract_product_info(containers):
    products = []
    for container in containers:
        try:
            title_container = container.findAll("a", {"class": "item-title"})
            product_name = title_container[0].text

            shipping_container = container.findAll("li", {"class": "price-ship"})
            shipping = shipping_container[0].text.strip().replace(" Shipping", "").replace(" shipping", "")

            price_container = container.findAll("li", {"class": "price-current"})
            price = price_container[0].text.strip().split()[0] if price_container else "N/A"

            products.append((product_name, shipping, price))
        except Exception as e:
            print(f"Error extracting product info: {e}")
    return products

def save_to_csv(filename, headers, data):
    try:
        with open(filename, "w", newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(headers)
            writer.writerows(data)
        print(f"Data saved to {filename}")
    except Exception as e:
        messagebox.showerror("Error", f"Error saving to CSV: {e}")

def display_results(products):
    result_window = tk.Toplevel()
    result_window.title("Data")
    result_window.geometry("1000x400")

    tree = ttk.Treeview(result_window, columns=("product_name", "shipping", "price"), show="headings")
    tree.heading("product_name", text="Product Name")
    tree.heading("shipping", text="Shipping")
    tree.heading("price", text="Price")
    
    tree.column("product_name", width=600)
    tree.column("shipping", width=200)
    tree.column("price", width=200)

    tree.pack(fill=tk.BOTH, expand=True)

    for product in products:
        tree.insert("", "end", values=product)

    # Make the column heading to wrap text if necessary
    for col in tree["columns"]:
        tree.heading(col, text=tree.heading(col)["text"], anchor="center")
        tree.column(col, anchor="center")

def scrape_url():
    url = url_entry.get()
    page_html = fetch_page(url)

    if page_html:
        containers = parse_page(page_html)
        products = extract_product_info(containers)

        if products:
            display_results(products)
        else:
            messagebox.showinfo("No Data", "No products found.")

def main():
    global url_entry
    root = tk.Tk()
    root.title("Newegg Scraper")
    root.geometry("500x200")

    frame = tk.Frame(root, padx=20, pady=20)
    frame.pack(expand=True)

    url_label = tk.Label(frame, text="Enter page URL:", font=("Arial", 12))
    url_label.grid(row=0, column=0, pady=10)

    url_entry = tk.Entry(frame, width=50, font=("Arial", 12))
    url_entry.grid(row=1, column=0, pady=5)
    url_entry.insert(0, 'https://www.newegg.ca/Video-Cards-Video-Devices/Category/ID-38')

    scrape_button = tk.Button(frame, text="Scrape", command=scrape_url, font=("Arial", 12))
    scrape_button.grid(row=2, column=0, pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
