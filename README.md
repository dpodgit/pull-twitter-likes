Prerequisites: Twitter API credentials

Program prompts user for 1) Twitter user handle, 2) The number of that user's favourite tweets (first most recent) to retrieve. Abiding by the API rate limit, the program pulls the text and a link to those _n_ favourited tweets, and writes them to a JSON file, which is dumped in the working directory.
