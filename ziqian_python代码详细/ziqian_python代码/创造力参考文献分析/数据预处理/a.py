

from email import contentmanager
from tracemalloc import start


content="ref1111111111111111111111"
end_index = content.rfind("Appendix")
start_index=content.rfind("ref")
print(end_index)
s=content[start_index:]
print(s)