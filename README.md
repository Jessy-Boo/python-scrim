# python-scrim

Three small python scripts I apparently needed at some point. Two magic 8-balls and a Newegg scraper, which is a spread of use cases I can not explain either.

## scripts

| file | what it is |
|---|---|
| `8ball_input.py` | magic 8-ball in the terminal. asks for a question, prints one of the 20 classic answers, clears the screen, repeats. type `exit` to quit |
| `8ball_tk.py` | same 8-ball, same 20 answers, now with a tkinter window. type a question and hit Enter or press Ask |
| `neweggscrape.py` | tkinter app: paste a Newegg URL, it fetches the page with urllib, parses product name / shipping / price out of `item-container` divs with BeautifulSoup, shows them in a table, and saves `products.csv` |

## running

The 8-balls have no dependencies:

```
python3 8ball_input.py
python3 8ball_tk.py
```

The scraper needs beautifulsoup4:

```
pip install beautifulsoup4
python3 neweggscrape.py
```

## honest status

The 8-balls still work. The scraper almost certainly does not: it looks for Newegg's `item-container` / `item-title` / `price-current` class names, and that markup has not survived contact with the current site. Expect zero products found unless the layout regresses in our favor. It was written for a tutorial-era Newegg and I have not updated it. Whoopsie daisies.

Tkinter ships with python on Windows and macOS builds; on linux you may need your package manager's python3-tk.
