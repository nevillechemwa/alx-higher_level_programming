##Hash tables
##What is a Hash Table Data Structure

Imagine you have a toy box with lots of different toys inside, and you want to find a specific toy quickly without searching through all the toys one by one.
To make it easier, you could put a label on each toy that says what it is, and then create a list of all the toys and their labels. This list is like a dictionary, where you can look up the label and find the corresponding toy.
Now, a HashTable works in a similar way. It's like a special type of dictionary where instead of using words for labels, we use numbers (which we call "keys").
So, for example, if we have a list of people and their phone numbers, we can use their phone numbers as keys in our HashTable. Then, if we want to find a specific person's phone number, we can look up their number in the HashTable and find it quickly, without having to search through the entire list.
Let's say we have a HashTable for fruits, where we use the number of letters in the fruit's name as the key. So, the key for "apple" would be 5, the key for "banana" would be 6, and so on.
If we want to find the fruit with 6 letters in its name, we can simply look up the key "6" in the HashTable and find the corresponding fruit ("banana").

Hash Function
Let's say you have a special toy that you love, and you want to keep it safe. You can put it inside a box and lock it with a secret code (like a password) that only you know. Now no one else can open the box and take your toy.
Similarly, when we use a Hash function, it takes our data (like a word, number or picture) and turns it into a secret code that only we know. This code is called the "hash value", and it's like a password that only works for that specific data.
For example, let's say we have the word "apple". We can put it through a Hash function, which turns it into a secret code like "d5f6a2b1c9". This code is unique to the word "apple" and cannot be used to represent any other word.
Now, when we use a HashTable, we use these hash values as keys to store our data. This makes it very fast to look up our data because we can go directly to the key that we want.
So, when we want to find the word "apple" in our HashTable, we put it through the Hash function again to get its hash value (which is "d5f6a2b1c9"), and then we use this hash value to quickly look up the word "apple" in the HashTable.

##Hash table
A Hash table is a way to store data in a way that makes it easy to find and access.
Imagine you have a big box with many different compartments inside it. Each compartment is labeled with a number, and you can put something inside each compartment. Now, if you want to find something specific inside the box, you just need to remember the number of the compartment where you put it. This makes it easy to find what you need without having to search through the entire box.
Similarly, a Hash table is like a big box with many compartments, but instead of using numbers to label the compartments, we use something called "keys". A key is like a special code that is used to label and find the data that we want to store.
For example, let's say we have a list of people and their phone numbers. We can use each person's name as the key to store their phone number in the Hash table. So, when we want to find a person's phone number, we just need to use their name as the key to look it up in the Hash table.
The Hash table uses a special function called a "Hash function" to convert the key into a unique number. This number is then used to determine the location in the Hash table where the data should be stored. This makes it very fast to find the data we need, even if we have a large amount of data to store.
In summary, a Hash table is a way to store data using keys and a special Hash function, which makes it fast and easy to find the data we need.

##why hash tables and not arrays 

Hash tables have some advantages over arrays in certain situations.
One of the biggest advantages of Hash tables is their ability to quickly search and access data based on a key. When we use an array to store data, we need to know the exact index of the data we want to access. This can be difficult and time-consuming, especially when we have a lot of data to store. However, with a Hash table, we can quickly find the data we need by using its key, which can be much faster and easier than searching through an entire array.
Another advantage of Hash tables is their ability to handle collisions. A collision happens when two pieces of data have the same hash value and need to be stored in the same location in the Hash table. Hash tables use a technique called "chaining" to handle collisions, which allows multiple pieces of data to be stored in the same location while still being easily accessible. Arrays, on the other hand, do not have this ability and would need to be resized if more data needs to be added.
However, there are also situations where arrays may be more useful than Hash tables. For example, when we have a small amount of data to store and we know the exact index of each piece of data, an array can be a simple and efficient way to store and access the data.
In summary, Hash tables and arrays both have their own advantages and disadvantages, and the best choice depends on the specific situation and the requirements of the problem you are trying to solve.

##What are the most common use cases of hash tables
Hash tables are a very versatile data structure and can be used in many different applications. Here are some of the most common use cases for Hash tables:
    1. Caching: Hash tables are often used for caching data in applications where quick access to frequently accessed data is important. For example, a web browser may use a Hash table to cache recently visited web pages for quick access when the user revisits them.
    2. Dictionaries: Hash tables are commonly used to implement dictionaries, where keys and values are stored and accessed by the keys. This is a very efficient way to look up values based on a key.
    3. Database indexing: Hash tables are used in databases to create indexes, which are used to quickly search and retrieve data from large databases.
    4. Counting occurrences: Hash tables can be used to count the occurrences of different elements in a data set. For example, a Hash table could be used to count the number of times each word appears in a text document.
    5. Cryptography: Hash tables can be used in cryptography to store and look up digital signatures, which are used to verify the authenticity and integrity of data.
These are just a few examples of the many applications of Hash tables. Their flexibility and efficiency make them a popular choice for many different types of applications.
