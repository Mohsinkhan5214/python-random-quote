import random

def main():
  try:
    # Open the quotes file and read all lines
    with open("quotes.txt") as f:
      quotes = f.readlines()
    
    # Remove any trailing whitespace/newlines from quotes
    quotes = [quote.strip() for quote in quotes if quote.strip()]
    
    # Check if we have any quotes
    if not quotes:
      print("No quotes found in the file.")
      return
    
    # Select and print a random quote
    print(random.choice(quotes))
    
  except FileNotFoundError:
    print("Error: quotes.txt file not found.")
  except Exception as e:
    print(f"An error occurred: {e}")

if __name__== "__main__":
  main()