# Boolean Search Model

## Overview

This Boolean Search Model is a reimagination of a Python project developed as part of my Organization and Retrieval of Information university project. The goal of this project was to create a search system that can handle simple queries using Boolean operators, only using AI.

The project was built completely by AI assistent called Codeium, an AI VScode extension. It was responsable for the whole coding, while I just fine tuned a few things in order for it to work. Unfortunately, this AI couldn't do it all by itself – mainly the raw boolean search part – and I have gave it a demo code for it to work on.

## Code Structure

The main code is organized in a file called `modelo_booleano.py`. The core of the code is the `boolean_search` function, which takes three parameters: `query`, `inverted_index`, and `base_path`. This function performs the Boolean search based on the provided query and returns the matching filenames.

## Base File

The search results are connected to their respective filenames using a base file. The base file, named `base.txt`, contains a list of document filenames, with each filename on a separate line. The files that compose the database are inside the `base_samba/` directory 

## Inverted Index

The search system relies on an inverted index, stored in a file called `index.txt`. The inverted index is a data structure that maps each term to the set of documents where it appears. The AI was able to automatically build the inverted index based on the provided documents and I only needed to guide it, showcasing its capabilities.

## Query Handling

The query handling was implemmented by the AI with a little help of mine providing a demo code. Despite that, Codeium extension was not able to fully interpret the query and return the correct results. However, it is important to note that the query handling functionality has some limitations and flaws, especially when it comes to the AND and NOT operators, but I decided to keep them as a showcase of the AI capabilities and to keep loyal to the premise of building the whole project with only AI.

## Querying

To execute a search, create a text file named `query.txt` and input your desired search query. The query should consist of space-separated terms, with support for logical operators such as `&` (AND), `|` (OR), and `!` (NOT). For example, a query could be: `'information & retrieval | !search'`.

## Running the Code

To run the code, execute the `modelo_booleano.py` file. Ensure that `query.txt`, is in the same directory as the script, and the path to `base.txt` is correct. The code will initiate the search based on the query and the base file, and return the corresponding filenames in a file called `answer.txt`, if any. It's important to note that the boolean search code is functional, but it may have some limitations and flaws due to the query handling implementation.

```bash
> python modelo_booleano.py base_samba/base.txt query.txt
```

Feel free to explore the code and experiment with different queries!
