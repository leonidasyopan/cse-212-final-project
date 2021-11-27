# Queues

## What is a Queue?
A queue is a data structure that uses the First In First Out (FIFO) approach (*see image below*) to store items in a linear order. Just like a line in a bank, the first to arrive is the first to be attended, in other words, "the least recently added item is removed first" (1).

![what-is-a-queue](what-is-a-queue.png)

## When to use a Queue?
It's important to first understand that queues are everywhere, we might not notice it due to all the abstraction that we have in our software and programming languages. Here are some examples:
* Scheduling asynchronous threads to be executed (in our applications)
* Operating systems use queues to organize their processes
* Servers receive requests and organize them in queues

In other words, anytime you need to work with things in a first in, first out system, a queue is your data structure to go.

## Options of Queues in Python?
There are many alternatives of approaches to work with Queues in Python, among them the most common are:
* Using Lists
* Using the Collenctions.deque Class
* Creating your own class

Creating your own class is a very cumbursome alternative, despite being very efficient. But since we have simpler alternatives we will dicard this one.

So the suggestion here is to use Deque, since it's an O(1) time complexity alternative, while Lists would have an O(n) time complexity,being less performatic.

### Implementing a Collection Deque Queue
```python
# We will need to import Deque from Collections
from collections import deque

# Then we can initialize our queue
queue = deque()
```
## Enqueue
Adding an item to a queue is called enqueuing. To do it with our Deque class we're going to use the `.append()` method.

```python
from collections import deque

queue = deque()

# Use the 'append()' method to enqueue a new item to the rear of your queue
queue.append("Adam")
queue.append("Brandon")
queue.append("Carl)
```

## Dequeue
Removing an item from a queue is called dequeing. To do it with our Deque class we're going to use the `.popleft()` method.

**Important:** we want to remove the item on the front of our queue, that's why we can't use the `.pop()` method, that would remove the item from the gear - the last one added.

```python
from collections import deque

queue = deque()

queue.append("Adam")
queue.append("Brandon")
queue.append("Carl")

# Use the 'popleft()' method to dequeue an item from the front of your queue
first_client = queue.popleft() # Adam
second_client = queue.popleft() # Brandon
third_client = queue.popleft() # Carl
```


## Length
We can find out the length of our queue by using the `len()` function.

```python
from collections import deque

queue = deque()

print(len(queue)) # Should print 0 (zero)

queue.append("Adam")
queue.append("Brandon")
queue.append("Carl")

print(len(queue)) # Should print 3 (three)
```
## Example
In Brazil, when we go to the doctor (public healthcare) we register our names and general health issues with a receptionist, than we need to wait our names to be called as soon as the doctor is available for us.

We can use Python and queues to implement the system that calls the patient's name, and it could look something like this:


```python
from collections import deque

patients_waiting = deque()

# John arrives to be attended
new_patient = "John Atkins"

# Add John to the waiting list
patients_waiting.append(new_patient)

# Mary arrives to be attended
new_patient = "Mary Benson"

# Add Mary to the waiting list
patients_waiting.append(new_patient)


# A loop would check when the doctor is available
# When that happens, the first in line will be called.
next_patient = patients_waiting.popleft()
print(next_patient + " go to Room #01")  # John should be called first

```

## Problem to Solve
During the Pandemics some stores in China created a digital list of the clients to be attended next and sent them a text message on their phones as soon as it was their time to be attended.

Create a simple program that simulates the behavior of registering a new client and then sending him a message when it's his turn to be attended.


**After you have your own solution you can compare it with the proposed one: [Solution](queue_problem_solution.py)**

## References to Further Study
1. Queue in Python - https://www.geeksforgeeks.org/queue-in-python/
2. Stacks and Queues in Python - https://stackabuse.com/stacks-and-queues-in-python/
3. Queue — A synchronized queue class - https://docs.python.org/3/library/queue.html
4. To Queue Or Not To Queue - https://medium.com/basecs/to-queue-or-not-to-queue-2653bcde5b04

[Back to Welcome Page](0-welcome.md)



