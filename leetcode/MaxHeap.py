from dataclasses import dataclass, field
import heapq


@dataclass
class Maxheap:
	data: list = field(default_factory=list)


	def __post_init__(self):
		self.data = [-ele for ele in self.data]
		heapq.heapify(self.data)


	def __bool__(self):
		if self.data:
			return True
		return False


	def __repr__(self):
		return f'{[-value for value in self.data]}'
	
	
	def dump(self)
		ret = []
		while self.data:
			ret.append(self.pop())
		return ret

	def iter_dump(self):
		while self.data:
			yield self.pop()


	def push(self, value):
		heapq.heappush(self.data, -value)


	def push_all(self, values):
		x = [-ele for ele in values]
		heapq.heapify(x)
		merged_heaps = heapq.merge(self.data, x)
		self.data = list(merged_heaps)
		
		
	def pop(self):
		return -heapq.heappop(self.data)


if __name__ == '__main__':
	m = Maxheap([5,10,18,50,1,3, -4])
	print(m)
