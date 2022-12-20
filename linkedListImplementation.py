class Node:

	def __init__(self,data):
		self.data = data
		self.nextNode = None

class LinkedList:

	def __init__(self):
		self.head = None
		self.numOfNodes = 0	

	def get_middle_node(self):
		fast_pointer = self.head	
		slow_pointer = self.head

		while fast_pointer.nextNode and fast_pointer.nextNode.nextNode:
			fast_pointer = fast_pointer.nextNode.nextNode
			slow_pointer = slow_pointer.nextNode
		return slow_pointer


	def insert_start(self, data):
		self.numOfNodes += 1
		new_node = Node(data)

		if not self.head:
			self.head = new_node
		else:
			new_node.nextNode = self.head
			self.head = new_node

	def insert_end(self,data):
	
		self.numOfNodes += 1
		new_node = Node(data)

		actual_node = self.head

		while actual_node.nextNode is not None:
			actual_node = actual_node.nextNode				
		actual_node.nextNode = new_node

	def size_of_list(self):
		return self.numOfNodes

	def traverse(self):

		actual_node = self.head

		while actual_node is not None:

			print(actual_node.data)
			actual_node	=  actual_node.nextNode

	def reverseALinkedList(self):
		current_node = self.head
		previous_node = None
		next_node = None

		while current_node is not None:
			next_node = current_node.next_node
			current_node.next_node = previous_node
			previous_node = current_node
			current_node = next_node
		self.head = previous_node			

	def remove(self, data):
		if self.head is None:
			return
		actual_node = self.head
		previous_node = None

		while actual_node is not None and actual_node.data  != data:
			previous_node = actual_node
			actual_node = actual_node.nextNode

		if actual_node is None:
			return 
		if previous_node is None:
			self.head = actual_node.nextNode

		else:
			previous_node.nextNode = actual_node.nextNode
			self.numOfNodes -= 1		
					

linked = LinkedList()
linked.insert_start(4)	
#linked.insert_start("Adam")				
linked.insert_start(2)	
linked.insert_end(1)
#linked.traverse()
#print(linked.size_of_list())
#linked.remove("Adam")
#print(linked.size_of_list())
#print(linked.get_middle_node().data)
linked.traverse()
