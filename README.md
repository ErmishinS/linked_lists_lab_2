# linked_lists_lab_2

## Description  
This project implements a list using Python’s built-in lists and a doubly linked list without relying on built-in collections. It supports essential operations such as appending, inserting, deleting, reversing, and searching within the list. The implementation is paired with a set of unit tests to verify its correctness and reliability. GitHub Actions are set up to automatically execute the tests.

## Variant Info
Variant = 7 mod 4 = **3**
- **Initial Implementation**: A list based on **built-in arrays/lists** in Python (using Python's `list` type).
- **Second Implementation**: A **Doubly Linked List**.

---

## Installation and Usage  

To run this application, you need [Python](https://www.python.org) installed on your system.

### Clone the repository 
```
git clone https://github.com/ErmishinS/linked_lists_lab_2.git
```
```
cd linked_lists_lab_2
```

### Run demonstrative cases
Simply execute the script (for list based on built-in arrays/lists):
```
python3 src/demonstrate_based_list.py 
```
Or execute the script (for a doubly linked list):
```
python3 src/demonstrate_doubly_linked_list.py
```


### Run the tests
Execute this script to run the tests:
```
python3 -m unittest discover tests    
```

## Link to commit with failed tests
[failed commit](https://github.com/ErmishinS/linked_lists_lab_2/commit/39c53aceb8cbefbcc5dd3f0c9965ed64ce13d4aa)

## Conclusions
This project was particularly useful for me as it provided an opportunity to work extensively with unit tests, an area in which I had limited experience before. The process of writing and running unit tests for the first time helped me understand their value in ensuring code reliability and preventing issues during development. Additionally, setting up Continuous Integration (CI) with GitHub Actions was an invaluable learning experience. I had never configured CI before, so it was a great opportunity to automate testing and make the process more efficient. In the end, unit tests and CI were incredibly helpful, and they made the development process smoother and more reliable, which I hadn’t fully appreciated before starting this project.