def extract_quotes(quotes):
    data = []
    for quote in quotes:
        text = quote.find_element("class name", "text").text
        author = quote.find_element("class name", "author").text
        data.append([text, author])
    return data
