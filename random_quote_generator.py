#!/usr/bin/env python3

import random

quotes = [
    "The only way to do great work is to love what you do. - Steve Jobs",
    "Strive not to be a success, but rather to be of value. - Albert Einstein",
    "The mind is everything. What you think you become. - Buddha",
    "Your time is limited, so don't waste it living someone else's life. - Steve Jobs",
    "The best way to predict the future is to create it. - Peter Drucker"
]

def get_random_quote():
  """Randomly selects a quote from the list of quotes."""
  return random.choice(quotes)

if __name__ == "__main__":
  print(get_random_quote())
