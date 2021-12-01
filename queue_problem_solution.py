clientes_queue = []

# First client arrives to be attended
new_client = "Yang Li"

# Add client to the waiting list
clientes_queue.append(new_client)

# Second client arrives to be attended
new_client = "Liu Zhang"

# Add client to the waiting list
clientes_queue.append(new_client)

# Keep adding clients to list
clientes_queue.append("Wěi qí")
clientes_queue.append("Niàn zhēn")
clientes_queue.append("Hóng tāo")

# As soon as one of the attendents is available send message to user phone
next_client = clientes_queue.pop(0)
print(next_client + " we're ready to attend you.")
