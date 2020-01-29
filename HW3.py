# Your name: Shahbab Ahmed
# Your student id: 64818147
# Your email: shahbaba@umich.edu
# List who you have worked with on this homework:

# import the random module for use in this program
import random

# Create the class Random_Quote_Generator
class Random_Quote_Generator:
    def __init__(self, quotes_list, author_list):
        self.quotes_list = quotes_list
        self.author_list = author_list
        self.quote_history_list = []
    # create the constructor (__init__) method
    # it takes as input:
    #   a list of possible quotes and
    #   a list of authors of the quotes
    # it sets this object's quotes_list (instance variable) to the passed list of quotes
    # it sets this object's author_list (instance variable) to the passed list of authors
    # it sets this object's quote_history_list to the empty list (instance variable)
    def quote(self):
        num = random.randrange(0, len(self.quotes_list) - 1)
        self.quote_history_list.append(num)
        return self.quotes_list[num] + self.author_list[num]
    # create the quote method
    # it randomly picks an index from 0 to the number of items in the quotes_list minus one
    # it adds that index to the end of the quote_history_list
    # it returns a string combining the quote and the author at that index in this object's quotes_list
    # "Quote - Author"

    def __str__(self):
        if len(self.quote_history_list) == 0:
            return "No quotes so far!"
        else:
            recent = self.quote_history_list[-1]
            return "Most recent: " + self.quotes_list[recent] + " - " + self.author_list[recent]
    # create the __str__ method
    # if the length of quote_history_list is 0 it returns "No quotes so far!"
    # else it returns the quote and the author at the last index in the quote_history_list as
    # "Most recent: Quote - Author"
    
    def print_history(self):
        for i in self.quote_history_list:
            print("[" + i + "] " self.quotes_list[i] " - " + self.author_list[i])
    # create the print_history method
    # prints "[index] Quote - Author" for each of the indicies in the quote_history_list
    # from the first to the last with each on a single line
    # it does not return anything!

    def print_count_for_num(self, index):
        count = 0
        for i in self.quote_history_list:
            if i == index:
                count += 1
        
        print(str(index) + " occured " + str(count) + "times")
        
        return (str(index) + " occured " + str(count) + "times")
    # create the print_count_for_num method
    # it prints and returns how many times the passed index is found in the quote_history_list
    # The return statement is "<index> occurned <N> times" (printing format and example also provided in the instruction document)

    # EXTRA POINTS
    def five_hundred method(self):
        
    # it calls the quote method 500 times, prints the counts for each index, and
    # prints the most frequently occurring index (printing format and example provided in the instruction document)

def main():
    # You are welcome to replace the quotes and names with your favorite quotes and authors 
    quote_list = ["If one is lucky, a solitary fantasy can totally transform one million realities.", \
    "Do not follow where the path may lead. Go, instead, where there is no path and leave a trail." \
    "We cannot solve our problems with the same thinking we used when we created them." \
    "We read the world wrong and say that it deceives us." \
    "Get your facts first, then you can distort them as you please."]

    author_list = ["Maya Angelou", "Ralph Waldo Emerson", "Albert Einstein", "Rabindranath Tagore", "Mark Twain"]

    print("Testing the first quote-generator:")
    quote_bot = Random_Quote_Generator(quote_list, author_list)
    print("Quote : " + quote_bot.quote())
    print("\nTesting most recent quote")
    print(quote_bot)
    print("\nQuote : " + quote_bot.quote())
    print("\nTesting most recent quote")
    print(quote_bot)
    print("\nPrinting the full history:")
    quote_bot.print_history()
    print("\nPrinting the number of times index 1 occured")
    quote_bot.print_count_for_num(1)

    print("\n===================================================================================================\n")

    #Create another quote-generator
    print("Testing the second quote-generator:")
    quote_bot2 = Random_Quote_Generator(quote_list, author_list)
    print("\nTesting when no quotes have been generated yet")
    print(quote_bot2)
    print("\nQuote : " + quote_bot2.quote())
    print("\nTesting most recent quote")
    print(quote_bot2)
    print("\nGenerating five quotes randomly")
    for x in range(5):
        print("Quote : " + quote_bot2.quote())
    print("\nPrinting the full history:")
    quote_bot2.print_history()
    print("\nPrinting the number of times index 2 occured")
    quote_bot2.print_count_for_num(2)

    #EXTRA POINTS
    #Try telling 500 quotes: Comment in the lines below if you attemp the extra credit!
    # print("\nTesting the five_hundred method")
    # quote_bot2.five_hundred()


# only run the main function if this file is being run (not imported)
if __name__ == "__main__":
    main()
